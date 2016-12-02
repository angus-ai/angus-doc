# -*- coding: utf-8 -*-
import StringIO
import math as m
import cv2
import numpy as np
import angus

def main(stream_index):
    camera = cv2.VideoCapture(0)
    camera.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640);
    camera.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480);
    camera.set(cv2.cv.CV_CAP_PROP_FPS, 10)

    if not camera.isOpened():
        print("Cannot open stream of index {}".format(stream_index))
        exit(1)

    print("Input stream is of resolution: {} x {}".format(camera.get(3), camera.get(4)))

    conn = angus.connect()
    service = conn.services.get_service('gaze_analysis', 1)
    service.enable_session()

    while camera.isOpened():
        ret, frame = camera.read()
        if not ret:
            break

        ### angus.ai computer vision services require gray images right now.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, buff = cv2.imencode(".jpg", gray, [cv2.IMWRITE_JPEG_QUALITY, 80])
        buff = StringIO.StringIO(np.array(buff).tostring())

        job = service.process({"image": buff})
        res = job.result

        for face in res['faces']:
            x, y, dx, dy = map(int, face['roi'])
            cv2.rectangle(frame, (x, y), (x+dx, y+dy), (0,255,0))

            psi = face['head_roll']
            theta = - face['head_yaw']
            phi = face['head_pitch']

            cx = int(x + 0.5*dx)
            cy = int(y + 0.5*dy)

            length = 150
            ### See here for details : https://en.wikipedia.org/wiki/Rotation_formalisms_in_three_dimensions
            xvec = int(length*(m.sin(phi)*m.sin(psi) - m.cos(phi)*m.sin(theta)*m.cos(psi)))
            yvec = int(- length*(m.sin(phi)*m.cos(psi) - m.cos(phi)*m.sin(theta)*m.sin(psi)))

            cv2.line(frame, (cx, cy), (cx+xvec, cy+yvec), (255, 0, 0), 3)


        cv2.imshow('original', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    ### Disabling session on the server
    service.disable_session()

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    ### Web cam index might be different from 0 on your setup.
    ### To grab a given video file instead of the host computer cam, try:
    ### main("/path/to/myvideo.avi")
    main(0)
