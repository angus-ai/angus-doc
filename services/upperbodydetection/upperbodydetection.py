import angus
from pprint import pprint

conn = angus.connect()
service = conn.services.get_service('upper_body_detection', version=1)
job = service.process({'image': open('./macgyver.jpg')})
pprint(job.result)
