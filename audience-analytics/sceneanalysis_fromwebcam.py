# -*- coding: utf-8 -*-

import cv2

import numpy as np
import StringIO
import datetime
import pytz
from math import cos, sin
import angus.client

def main(stream_index):
    camera = cv2.VideoCapture(stream_index)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    camera.set(cv2.CAP_PROP_FPS, 10)

    if not camera.isOpened():
        print("Cannot open stream of index {}".format(stream_index))
        exit(1)

    print("Video stream is of resolution {} x {}".format(camera.get(3), camera.get(4)))

    conn = angus.client.connect()
    service = conn.services.get_service("scene_analysis", version=1)
    service.enable_session()

    while camera.isOpened():
        ret, frame = camera.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, buff = cv2.imencode(".jpg", gray,  [cv2.IMWRITE_JPEG_QUALITY, 80])
        buff = StringIO.StringIO(np.array(buff).tostring())

        t = datetime.datetime.now(pytz.utc)
        job = service.process({"image": buff,
                               "timestamp" : t.isoformat(),
                               "store" : True
        })
        res = job.result

        if "error" in res:
            print(res["error"])
        else:
            # This parses the entities data
            for key, val in res["entities"].iteritems():
                # display only gaze vectors
                # retrieving eyes points
                eyel, eyer = val["face_eye"]
                eyel = tuple(eyel)
                eyer = tuple(eyer)

                # retrieving gaze vectors
                psi = 0
                g_yaw, g_pitch = val["gaze"]
                theta = - g_yaw
                phi = g_pitch

                # Computing projection on screen
                # and drawing vectors on current frame
                length = 150
                xvec = int(length * (sin(phi) * sin(psi) - cos(phi) * sin(theta) * cos(psi)))
                yvec = int(- length * (sin(phi) * cos(psi) - cos(phi) * sin(theta) * sin(psi)))
                cv2.line(frame, eyel, (eyel[0] + xvec, eyel[1] + yvec), (0, 140, 0), 3)

                xvec = int(length * (sin(phi) * sin(psi) - cos(phi) * sin(theta) * cos(psi)))
                yvec = int(- length * (sin(phi) * cos(psi) - cos(phi) * sin(theta) * sin(psi)))
                cv2.line(frame, eyer, (eyer[0] + xvec, eyer[1] + yvec), (0, 140, 0), 3)

        cv2.imshow('original', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    service.disable_session()

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    ### Web cam index might be different from 0 on your setup.
    ### To grab a given video file instead of the host computer cam, try:
    ### main("/path/to/myvideo.avi")
    main(0)
