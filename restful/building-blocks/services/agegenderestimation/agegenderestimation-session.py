# -*- coding: utf-8 -*-
import angus.client
from pprint import pprint

conn = angus.client.connect()
service = conn.services.get_service('age_and_gender_estimation', version=1)

service.enable_session()
for i in range(200):
    job = service.process({'image': open('./photo-%s.jpg' % (i), 'rb')})
service.disable_session()

pprint(job.result)
