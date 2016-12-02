import angus
from pprint import pprint

conn = angus.connect()
service = conn.services.get_service('age_and_gender_estimation', version=1)
job = service.process({'image': open('./macgyver.jpg', 'rb')})

pprint(job.result)
