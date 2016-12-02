import angus
from pprint import pprint

conn = angus.connect()
service = conn.services.get_service('motion_detection', version=1)

service.enable_session()

for i in range(200):
    job = service.process({'image': open('./photo-{}.jpg'.format(i), 'rb')})
    pprint(job.result)

service.disable_session()
