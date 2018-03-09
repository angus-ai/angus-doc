# -*- coding: utf-8 -*-
from six.moves import queue, input
from io import BytesIO
import wave
import time
import sys
from pprint import pprint
import pyaudio
import numpy as np
import angus.client

CHUNK = 8192
PYAUDIO_FORMAT = pyaudio.paInt16
NUMPY_FORMAT = np.int16
TARGET_RATE = 48000
TARGET_CHANNELS = 2

def list_inputs():
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if info['maxInputChannels'] > 0:
            print("Device index={} name={}".format(info['index'], info['name']))

def prepare(in_data, channels, rate):
    # Extract first channel
    in_data = np.fromstring(in_data, dtype=NUMPY_FORMAT)
    in_data = np.reshape(in_data, (CHUNK, channels))

    # Re-sample if needed
    srcx = np.arange(0, CHUNK, 1)
    tgtx = np.arange(0, CHUNK, float(rate) / float(TARGET_RATE))

    print ((in_data[:,0]).size)

    left = np.interp(tgtx, srcx, in_data[:,0]).astype(NUMPY_FORMAT)
    right = np.interp(tgtx, srcx, in_data[:,1]).astype(NUMPY_FORMAT)

    print(left.size)
    print(CHUNK)

    c = np.empty((left.size + right.size), dtype=NUMPY_FORMAT)
    c[0::2] = left
    c[1::2] = right
    return c.tostring()

def main(stream_index):
    p = pyaudio.PyAudio()

    # Device configuration
    conf = p.get_device_info_by_index(stream_index)
    channels = int(conf['maxInputChannels'])
    if channels < TARGET_CHANNELS:
        raise RuntimeException("Bad device, no input channel")

    rate = int(conf['defaultSampleRate'])

    # Angus
    conn = angus.client.connect()
    service = conn.services.get_service('sound_localization', version=1)
    service.enable_session()

    # Record Process
    stream_queue = queue.Queue()
    def chunk_callback(in_data, frame_count, time_info, status):
        in_data = prepare(in_data, channels, rate)
        stream_queue.put(in_data)
        return (in_data, pyaudio.paContinue)
    stream = p.open(format=PYAUDIO_FORMAT,
                channels=channels,
                rate=rate,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=stream_index,
                stream_callback=chunk_callback)
    stream.start_stream()

    while True:
        nb_buffer_available = stream_queue.qsize()
        if nb_buffer_available > 0:
            print("nb buffer available = {}".format(nb_buffer_available))

        if nb_buffer_available == 0:
            time.sleep(0.01)
            continue

        data = stream_queue.get()

        buff = BytesIO()

        wf = wave.open(buff, 'wb')
        wf.setnchannels(TARGET_CHANNELS)
        wf.setsampwidth(p.get_sample_size(PYAUDIO_FORMAT))
        wf.setframerate(TARGET_RATE)
        wf.writeframes(data)
        wf.close()

        job = service.process(
            {'sound': BytesIO(buff.getvalue()), 'baseline': 0.14, 'sensitivity': 0.7})
        pprint(job.result['sources'])


    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        list_inputs()
        INDEX = input("Please select a device number:")
    else:
        INDEX = sys.argv[1]
    try:
        main(int(INDEX))
    except ValueError:
        print("Not a valid index")
        exit(1)
