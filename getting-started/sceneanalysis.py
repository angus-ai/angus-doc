# -*- coding: utf-8 -*-
import angus.client
from pprint import pprint

conn = angus.client.connect()
service = conn.services.get_service("scene_analysis", version=1)

service.enable_session()

while True:
    job = service.process({"image": open("./image.jpg", 'rb'),
                           "timestamp" : "2016-10-26T16:21:01.136287+00:00",
                           "camera_position": "ceiling",
                           "sensitivity": {
                                            "appearance": 0.7,
                                            "disappearance": 0.7,
                                            "age_estimated": 0.4,
                                            "gender_estimated": 0.5,
                                            "focus_locked": 0.9,
                                            "emotion_detected": 0.4,
                                            "direction_estimated" : 0.8
                                          },
                           "store": False
                          })
    pprint(job.result)


service.disable_session()
