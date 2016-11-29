import angus
from pprint import pprint

conn = angus.connect()
service = conn.services.get_service('dummy', version=1)
job = service.process({'echo': 'Hello world'})

pprint(job.result)
