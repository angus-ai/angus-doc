#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Queue
import StringIO
import wave
import time
import angus
import pyaudio

CHUNK = 8192
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
RECORD_SECONDS = 2

### Index will differ depending on your system
INDEX = 4  # USB Cam


p = pyaudio.PyAudio()

conn = angus.connect()
service = conn.services.get_service('sound_detection', version=1)
service.enable_session()
stream_queue = Queue.Queue()

def callback(in_data, frame_count, time_info, status):
    stream_queue.put(in_data)
    return (in_data, pyaudio.paContinue)

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=INDEX,
                stream_callback=callback)


stream.start_stream()

while(True):

    nb_buffer_available = stream_queue.qsize()
    if nb_buffer_available > 0:
        print "nb buffer available" + str(nb_buffer_available)

    if nb_buffer_available == 0:
        time.sleep(0.01)
        continue

    data = stream_queue.get()

    buff = StringIO.StringIO()

    wf = wave.open(buff, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()

    job = service.process(
        {'sound': StringIO.StringIO(buff.getvalue()), 'sensitivity': 0.7})
    print job.result


stream.stop_stream()
stream.close()
p.terminate()
