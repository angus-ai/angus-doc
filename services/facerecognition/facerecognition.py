import angus
from pprint import pprint

conn = angus.connect()
service = conn.services.get_service('face_recognition', version=1)

PATH = "/path/to/your/face/samples/"

w1_s1 = conn.blobs.create(open(PATH + "jamel/1.jpeg"))
w1_s2 = conn.blobs.create(open(PATH + "jamel/2.jpg"))
w1_s3 = conn.blobs.create(open(PATH + "jamel/3.jpg"))
w1_s4 = conn.blobs.create(open(PATH + "jamel/4.jpg"))

w2_s1 = conn.blobs.create(open(PATH + "melissa/1.jpg"))
w2_s2 = conn.blobs.create(open(PATH + "melissa/2.jpg"))
w2_s3 = conn.blobs.create(open(PATH + "melissa/3.jpg"))
w2_s4 = conn.blobs.create(open(PATH + "melissa/4.jpg"))

album = {'jamel': [w1_s1, w1_s2, w1_s3, w1_s4], 'melissa': [w2_s1, w2_s2, w2_s3, w2_s4]}

job = service.process({'image': open(PATH + "melissa/5.jpg"), "album" : album})
pprint(job.result)
