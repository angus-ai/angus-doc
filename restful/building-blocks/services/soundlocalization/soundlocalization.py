# -*- coding: utf-8 -*-
import angus.client
from pprint import pprint

conn = angus.client.connect()
service = conn.services.get_service('sound_localization', version=1)
job = service.process({'sound': open("./sound.wav", 'rb'), 'baseline' : 0.7, 'sensitivity:0.5'})

pprint(job.result)
