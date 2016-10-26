#!/usr/bin/env python
import StringIO

import angus
import cv2
import numpy as np
import datetime
import pytz

if __name__ == '__main__':
    ### Web cam index might be different from 0 on your setup.
    STREAM_INDEX = 0
    cap = cv2.VideoCapture(STREAM_INDEX)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

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

            t = datetime.datetime.now(pytz.utc)
            job = service.process({'image': buff,
                                   'timestamp' : str(t),
                                   'camera_position': 'facing',
                                   'sensitivity': {
                                                    'appearance': 0.7,
                                                    'disappearance': 0.7,
                                                    'age_estimated': 0.6,
                                                    'gender_estimated': 0.6,
                                                    'focus_locked': 0.9,
                                                    'emotion_detected': 0.4,
                                                  }
                                  })
            res = job.result

            # This parses the events
            if "events" in res:
                if res["events"] != []:
                    for event in res["events"]:
                        print "New Event : " + event["type"]
            elif "error" in res:
                print res["error"]

            # This parses the entities data
            for key, val in res["entities"].iteritems():
                roi = val['face_roi']
                cv2.rectangle(frame, (int(roi[0]), int(roi[1])),
                                     (int(roi[0] + roi[2]), int(roi[1] + roi[3])),
                                     (0,255,0), 2)


            cv2.imshow('original', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    service.disable_session()

    cap.release()
    cv2.destroyAllWindows()
