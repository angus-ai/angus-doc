#!/usr/bin/env python
import angus

conn = angus.connect()
service = conn.services.get_service('scene_analysis', version=1)

service.enable_session()

while True:
    job = service.process({'image': open('./image.jpg'),
                           'timestamp' : "2016:10:24 18:56:23.000011",
                           'camera_position': 'ceiling',
                           'sensitivity': {
                                            'appearance': 0.2,
                                            'disappearance': 0.5,
                                            'age': 0.2,
                                            'gender': 0.2,
                                            'trajectory': 0.2,
                                            'focus': 0.2,
                                            'emotion': 0.2,
                                          }
                          })
print job.result


service.disable_session()
