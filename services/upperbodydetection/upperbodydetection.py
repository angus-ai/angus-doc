# -*- coding: utf-8 -*-
import angus.client
from pprint import pprint

conn = angus.client.connect()
service = conn.services.get_service('upper_body_detection', version=1)
job = service.process({'image': open('./macgyver.jpg', 'rb')})
pprint(job.result)
