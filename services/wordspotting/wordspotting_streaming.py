import Queue
import StringIO
import wave
import time
import sys
from pprint import pprint
import pyaudio
import numpy as np
import angus

### Good performances off this script depend a lot on these parameters,
### do not hesitate to experiment with different settings
CHUNK = 16384
RATE = 44100

### Wordspotting service currently only accept 16bit PCM, mono signals.
FORMAT = pyaudio.paInt16
CHANNELS = 1

### Mix index will differ depending on your system
INDEX = 0

p = pyaudio.PyAudio()

conn = angus.connect()
service = conn.services.get_service('word_spotting', version=1)

PATH = "/path/to/samples/"

### French filenames, sorry!
### Here, resources are created on Angus.ai server from your samples
w1_s1 = conn.blobs.create(open(PATH + "allumelesalon.wav", 'rb'))
w1_s2 = conn.blobs.create(open(PATH + "allumelesalon2.wav", 'rb'))
w1_s3 = conn.blobs.create(open(PATH + "allumelesalon3.wav", 'rb'))
w1_s4 = conn.blobs.create(open(PATH + "allumelesalon4.wav", 'rb'))

w2_s1 = conn.blobs.create(open(PATH + "eteintlewifi.wav", 'rb'))
w2_s2 = conn.blobs.create(open(PATH + "eteintlewifi2.wav", 'rb'))
w2_s3 = conn.blobs.create(open(PATH + "eteintlewifi3.wav", 'rb'))
w2_s4 = conn.blobs.create(open(PATH + "eteintlewifi4.wav", 'rb'))

### Specifying the vocabulary at session opening
vocabulary = {'allume le salon': [w1_s1, w1_s2, w1_s3, w1_s4], 'eteint le wifi': [w2_s1, w2_s2, w2_s3, w2_s4]}
service.enable_session({"vocabulary" : vocabulary})

def callback(in_data, frame_count, time_info, status):
    stream_queue.put(in_data)
    return (in_data, pyaudio.paContinue)

stream_queue = Queue.Queue()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=INDEX,
                stream_callback=callback)


stream.start_stream()


def convert(buff_in, rate_in, rate_out):
    # Resample buffer with numpy linear interpolation
    buff_in = np.frombuffer(buff_in, dtype=np.int16)
    srcx = np.arange(0, buff_in.size, 1)
    tgtx = np.arange(0, buff_in.size, float(rate_in) / float(rate_out))
    buff_out = np.interp(tgtx, srcx, buff_in).astype(np.int16)
    return buff_out.tostring()


while True:

    nb_buffer_available = stream_queue.qsize()
    if nb_buffer_available > 0:
        print("nb buffer available = {}".format(nb_buffer_available))
    else:
        time.sleep(0.01)
        continue

    ### Avoiding buffer stacking in case of network lags
    if nb_buffer_available > 5:
        stream_queue.queue.clear()

    data = stream_queue.get()
    data = convert(data, RATE, 16000)

    buff = StringIO.StringIO()

    wf = wave.open(buff, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(16000)
    wf.writeframes(data)
    wf.close()

    job = service.process(
        {'sound': StringIO.StringIO(buff.getvalue()), 'sensitivity': 0.7})

    if "nbests" in job.result:
        pprint(job.result)

stream.stop_stream()
stream.close()
p.terminate()
