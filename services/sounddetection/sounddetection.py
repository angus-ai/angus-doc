import angus
from pprint import pprint

conn = angus.connect()
service = conn.services.get_service('sound_detection', version=1)
job = service.process({'sound': open("./sound.wav", 'rb'), 'sensitivity':0.7})

pprint(job.result)
