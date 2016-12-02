# -*- coding: utf-8 -*-
import Queue
import StringIO
import wave
import time
import angus
import pyaudio
import sys
import numpy as np


CHUNK = 8192
PYAUDIO_FORMAT = pyaudio.paInt16
NUMPY_FORMAT = np.int16

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
    in_data = in_data[:,0]

    # Down sample if needed
    srcx = np.arange(0, in_data.size, 1)
    tgtx = np.arange(0, in_data.size, float(rate) / float(16000))

    in_data = np.interp(tgtx, srcx, in_data).astype(NUMPY_FORMAT)
    return in_data


def main(stream_index):

    p = pyaudio.PyAudio()

    # Device configuration
    conf = p.get_device_info_by_index(stream_index)
    channels = int(conf['maxInputChannels'])
    if channels < 1:
        raise RuntimeException("Bad device, no input channel")

    rate = int(conf['defaultSampleRate'])
    if rate < 16000:
        raise RuntimeException("Bad device, sample rate is too low")


    # Angus
    conn = angus.connect()
    service = conn.services.get_service('voice_detection', version=1)
    service.enable_session()

    # Record Process
    stream_queue = Queue.Queue()
    def chunk_callback(in_data, frame_count, time_info, status):
        in_data = prepare(in_data, channels, rate)
        stream_queue.put(in_data.tostring())
        return (in_data, pyaudio.paContinue)

    stream = p.open(format=PYAUDIO_FORMAT,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=stream_index,
                    stream_callback=chunk_callback)
    stream.start_stream()

    # Get data and send to Angus.ai
    while True:
        nb_buffer_available = stream_queue.qsize()

        if nb_buffer_available == 0:
            time.sleep(0.01)
            continue

        data = stream_queue.get()
        buff = StringIO.StringIO()

        wf = wave.open(buff, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(PYAUDIO_FORMAT))
        wf.setframerate(16000)
        wf.writeframes(data)
        wf.close()

        job = service.process(
            {'sound': StringIO.StringIO(buff.getvalue()), 'sensitivity': 0.2})

        res = job.result["voice_activity"]

        if res == "VOICE":
            print "\033[A                                             \033[A"
            print "***************************"
            print "*****   VOICE !!!!   ******"
            print "***************************"


    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        list_inputs()
        index = raw_input("Please select a device number:")
    else:
        index = sys.argv[1]

    try:
        index = int(index)
        main(index)
    except ValueError:
        print("Not a valid index")
        exit(1)
