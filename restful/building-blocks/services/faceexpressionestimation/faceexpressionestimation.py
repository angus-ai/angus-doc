# -*- coding: utf-8 -*-
from pprint import pprint
import angus.client

conn = angus.client.connect()
service = conn.services.get_service('face_expression_estimation', version=1)
job = service.process({'image': open('./macgyver.jpg', 'rb')})
pprint(job.result)
