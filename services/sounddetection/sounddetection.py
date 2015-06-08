#!/usr/bin/env python
# -*- coding: utf-8 -*-

import angus.cloud

conn = angus.connect()

service = conn.services.get_service('sound_detection', version=1)

job = service.process({'sound': open("./sound.wav")})

print job.result
