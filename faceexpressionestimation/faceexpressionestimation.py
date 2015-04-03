#!/usr/bin/env python

import angus

conn = angus.connect()
service = conn.services.get_service('face_expression_estimation', version=1)
job = service.process({'image': open('./macgyver.jpg')})
print job.result['faces']
