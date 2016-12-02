import angus.cloud

conn = angus.connect()

service = conn.services.get_service('voice_detection', version=1)

job = service.process({'sound': open("./sound.wav", 'rb'), 'sensitivity':0.7})

print job.result
