import angus
from pprint import pprint

conn = angus.connect()
service = conn.services.get_service('sound_localization', version=1)
job = service.process({'sound': open("./sound.wav"), 'baseline' : 0.7, 'sensitivity:0.5'})

pprint(job.result)
