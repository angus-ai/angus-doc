# -*- coding: utf-8 -*-
import angus.client
from pprint import pprint

conn = angus.client.connect()
service = conn.services.get_service('dummy', version=1)
job = service.process({'echo': 'Hello world'})

pprint(job.result)
