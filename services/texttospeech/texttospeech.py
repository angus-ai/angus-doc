#!/usr/bin/env python
# -*- coding: utf-8 -*-

import angus

conn = angus.connect()
service = conn.services.get_service('text_to_speech', version=1)
job = service.process({'text': "Hi guys, how are you today?", 'lang' : "en-US"})

### The output wav file is available as compressed (zlib), base64 string.
sound = job.result["sound"]
