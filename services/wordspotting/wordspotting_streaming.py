#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Queue
import StringIO
import wave
import time
import angus
import pyaudio
from os import system
import operator

### Good performances off this script depend a lot on these parameters, 
### do not hesitate to experiment with different settings
CHUNK = 16384
RATE = 44100

### Wordspotting service currently only accept 16bit PCM, mono signals.
FORMAT = pyaudio.paInt16
CHANNELS = 1

### Mix index will differ depending on your system
INDEX = 0
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

conn = angus.connect()
service = conn.services.get_service('word_spotting', version=1)

PATH = "/path/to/samples/"

### French filenames, sorry!
### Here, resources are created on Angus.ai server from your samples
w1_s1 = conn.blobs.create(open(PATH + "allumelesalon.wav"))
w1_s2 = conn.blobs.create(open(PATH + "allumelesalon2.wav"))
w1_s3 = conn.blobs.create(open(PATH + "allumelesalon3.wav"))
w1_s4 = conn.blobs.create(open(PATH + "allumelesalon4.wav"))

w2_s1 = conn.blobs.create(open(PATH + "eteintlewifi.wav"))
w2_s2 = conn.blobs.create(open(PATH + "eteintlewifi2.wav"))
w2_s3 = conn.blobs.create(open(PATH + "eteintlewifi3.wav"))
w2_s4 = conn.blobs.create(open(PATH + "eteintlewifi4.wav"))

### Specifying the vocabulary at session opening
vocabulary = {'allume le salon': [w1_s1, w1_s2, w1_s3, w1_s4], 'eteint le wifi': [w2_s1, w2_s2, w2_s3, w2_s4]}
service.enable_session({"vocabulary" : vocabulary})

stream_queue = Queue.Queue()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=INDEX,
                stream_callback=callback)


stream.start_stream()

def callback(in_data, frame_count, time_info, status):
    stream_queue.put(in_data)
    return (in_data, pyaudio.paContinue)

def convert(filename, filename2):
    system("sox %s -r 16000 %s" % (filename, filename2))

while(True):

    nb_buffer_available = stream_queue.qsize()
    if nb_buffer_available > 0:
        print "nb buffer available" + str(nb_buffer_available)

    if nb_buffer_available == 0:
        time.sleep(0.01)
        continue

    ### Avoiding buffer stacking in case of network lags
    if nb_buffer_available > 5:
        stream_queue.queue.clear()

    data = stream_queue.get()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()

    ### This step is only needed if your mic does not work at 16kHz
    convert(WAVE_OUTPUT_FILENAME, "test.wav")
    
    job = service.process({'sound': open("test.wav"), 'sensitivity':0.7})
    
    if job.result['Result'] != 'None':
        print job.result


stream.stop_stream()
stream.close()
p.terminate()