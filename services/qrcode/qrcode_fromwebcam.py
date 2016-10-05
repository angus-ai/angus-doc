#!/usr/bin/env python
import StringIO

import angus
import cv2
import numpy as np

if __name__ == '__main__':
    ### Web cam index might be different from 0 on your setup.
    stream_index = 0
    cap = cv2.VideoCapture(stream_index)

    if not cap.isOpened():
        print "Cannot open stream of index " + str(stream_index)
        exit(1)

    print "Video stream is of resolution " + str(cap.get(3)) + " x " + str(cap.get(4))

    conn = angus.connect()
    service = conn.services.get_service("qrcode_decoder", version=1)
    service.enable_session()

    while(cap.isOpened()):
        ret, frame = cap.read()
        if frame is None:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, buff = cv2.imencode(".jpg", gray)
        buff = StringIO.StringIO(np.array(buff).tostring())

        job = service.process({"image": buff})

        if "data" in job.result:
            print job.result["data"]

        cv2.imshow('original', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    service.disable_session()

    cap.release()
    cv2.destroyAllWindows()
