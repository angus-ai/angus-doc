#!/usr/bin/env python

import angus

conn = angus.connect()
service = conn.services.get_service('qrcode_decoder', version=1)
job = service.process({'image': open('./qrcode.jpg')})
print job.result
