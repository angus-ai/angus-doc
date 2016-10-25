#!/usr/bin/env python
import StringIO

import angus
import cv2
import numpy as np
import datetime

if __name__ == '__main__':
    ### Web cam index might be different from 0 on your setup.
    STREAM_INDEX = 0
    cap = cv2.VideoCapture(STREAM_INDEX)

    if not cap.isOpened():
        print "Cannot open stream of index " + str(STREAM_INDEX)
        exit(1)

    print "Video stream is of resolution " + str(cap.get(3)) + \
     " x " + str(cap.get(4))

    conn = angus.connect()
    service = conn.services.get_service("scene_analysis", version=1)
    service.enable_session()

    while cap.isOpened():
        ret, frame = cap.read()
        if not frame == None:

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret, buff = cv2.imencode(".png", gray)
            buff = StringIO.StringIO(np.array(buff).tostring())

            t = datetime.datetime.now()
            job = service.process({'image': buff,
                                   'timestamp' : str(t),
                                   'camera_position': 'ceiling',
                                   'sensitivity': {
                                                    'appearance': 0.7,
                                                    'disappearance': 0.7,
                                                    'age': 0.6,
                                                    'gender': 0.6,
                                                    'trajectory': 0.5,
                                                    'focus': 0.9,
                                                    'emotion': 0.4,
                                                  }
                                  })
            res = job.result


            if "events" in res:
                if res["events"] != []:
                    for event in res["events"]:
                        if "data" in event:
                            print event["type"] + " : " + str(event["data"]) + \
                            " with confidence: " + str(event["confidence"])
                        else:
                            print event["type"] + " with confidence: " \
                            + str(event["confidence"])
            elif "error" in res:
                print res["error"]


            cv2.imshow('original', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    service.disable_session()

    cap.release()
    cv2.destroyAllWindows()
