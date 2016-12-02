# -*- coding: utf-8 -*-
import angus
import base64
import zlib
import subprocess

def decode_output(sound, filename):
	sound = base64.b64decode(sound)
	sound = zlib.decompress(sound)
	with open(filename, "wb") as f:
	    f.write(sound)

conn = angus.connect()
service = conn.services.get_service('text_to_speech', version=1)

job = service.process({'text': "Hi guys, how are you today?", 'lang' : "en-US"})

### The output wav file is available as compressed (zlib), base64 string.
### Here, the string is decoded and played back by Linux "aplay".
decode_output(job.result["sound"], "output.wav")
subprocess.call(["/usr/bin/aplay", "./output.wav"])
