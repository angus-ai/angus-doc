#!/usr/bin/env python

import angus

conn = angus.connect()
service = conn.services.get_service('age_and_gender_estimation', version=1)
job = service.process({'image': open('./macgyver.jpg')})

print(job.result)
