#!/usr/bin/env python
import angus

conn = angus.connect()
service = conn.services.get_service('scene_analysis', version=1)

service.enable_session()

while True:
    job = service.process({'image': open('./image.jpg'),
                           'timestamp' : "2016-10-26T16:21:01.136287+00:00",
                           'camera_position': 'ceiling',
                           'sensitivity': {
                                            'appearance': 0.2,
                                            'disappearance': 0.5,
                                            'age_estimated': 0.2,
                                            'gender_estimated': 0.2,
                                            'focus_locked': 0.2,
                                            'focus_unlocked': 0.2,
                                            'emotion_detected': 0.2,
                                          }
                          })
print job.result


service.disable_session()
