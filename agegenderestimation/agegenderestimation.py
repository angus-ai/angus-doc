#!/usr/bin/env python

import angus

conn = angus.connect()
service = conn.services.get_service('agegender_estimation', version=1)
job = service.process({'image': open('./macgyver.jpg')})
print job.result['faces']
