import Queue
import StringIO
import wave

import angus.cloud
import pyaudio
import control
import math


CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000
RECORD_SECONDS = 2
INDEX = 2 # USB Cam
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

print p.get_default_host_api_info()
print
print
print p.get_device_info_by_host_api_device_index(0, INDEX)
print
print

conn = angus.connect()
service = conn.services.get_service('sound_localization', version=1)

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

count = 0

print("* recording")
stream.start_stream()

while(True):
    frames = []

    nb_buffer_available = stream_queue.qsize()

    print "queue size " + str(nb_buffer_available)
    for i in range(nb_buffer_available):
        data = stream_queue.get()
        frames.append(data)

    if nb_buffer_available ==0:
        continue

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    job = service.process({'sound': open(WAVE_OUTPUT_FILENAME), 'baseline':0.14, 'sensitivity':0.5})

    #print job.result
    print job.result['loc']


stream.stop_stream()
print("* done recording")

stream.close()
p.terminate()
