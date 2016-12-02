import angus
from pprint import pprint

conn = angus.connect()
service = conn.services.get_service('qrcode_decoder', version=1)
job = service.process({'image': open('./qrcode.jpg', 'rb')})

pprint(job.result)
