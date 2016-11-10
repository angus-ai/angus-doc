#!/usr/bin/env python

import angus

conn = angus.connect()
service = conn.services.get_service('upper_body_detection', version=1)
job = service.process({'image': open('./macgyver.jpg')})
print job.result
