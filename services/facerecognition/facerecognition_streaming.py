# -*- coding: utf-8 -*-
import StringIO
import cv2
import numpy as np

import angus.client


def main(stream_index):
    camera = cv2.VideoCapture(stream_index)
    camera.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
    camera.set(cv2.cv.CV_CAP_PROP_FPS, 10)

    if not camera.isOpened():
        print("Cannot open stream of index {}".format(stream_index))
        exit(1)

    print("Input stream is of resolution: {} x {}".format(camera.get(3), camera.get(4)))

    conn = angus.client.connect()
    service = conn.services.get_service("face_recognition", version=1)

    ### Choose here the appropriate pictures.
    ### Pictures given as samples for the album should only contain 1 visible face.
    ### You can provide the API with more than 1 photo for a given person.
    w1_s1 = conn.blobs.create(open("./images/gwenn.jpg", 'rb'))
    w2_s1 = conn.blobs.create(open("./images/aurelien.jpg", 'rb'))
    w3_s1 = conn.blobs.create(open("./images/sylvain.jpg", 'rb'))

    album = {'gwenn': [w1_s1], 'aurelien': [w2_s1], 'sylvain': [w3_s1]}

    service.enable_session({"album" : album})

    while camera.isOpened():
        ret, frame = camera.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, buff = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
        buff = StringIO.StringIO(np.array(buff).tostring())

        job = service.process({"image": buff})
        res = job.result

        for face in res['faces']:
            x, y, dx, dy = face['roi']
            cv2.rectangle(frame, (x, y), (x+dx, y+dy), (0,255,0))

            if len(face['names']) > 0:
                name = face['names'][0]['key']
                cv2.putText(frame, "Name = {}".format(name), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))

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
