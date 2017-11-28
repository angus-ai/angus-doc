# -*- coding: utf-8 -*-
import angus.client.cloud
from pprint import pprint

conn = angus.client.connect()
service = conn.services.get_service('word_spotting', version=2)
vocabulary = [{"words" : "bonjour"},
              {"words" : "eteint le salon"},
              {"words" : "stop"}]

job = service.process({'sound': open("./sound.wav", 'rb'), 'sensitivity': 0.7, 'lang': "en-US", 'vocabulary': vocabulary})

pprint(job.result)
