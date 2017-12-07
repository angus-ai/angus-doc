# -*- coding: utf-8 -*-
import StringIO
import cv2
import numpy as np
import angus.client

def main(stream_index):
    camera = cv2.VideoCapture(stream_index)
    camera.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640);
    camera.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480);
    camera.set(cv2.cv.CV_CAP_PROP_FPS, 10)

    if not camera.isOpened():
        print("Cannot open stream of index {}".format(stream_index))
        exit(1)

    print("Input stream is of resolution: {} x {}".format(camera.get(3), camera.get(4)))

    conn = angus.client.connect()
    service = conn.services.get_service('face_expression_estimation', 1)
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
            x, y, dx, dy = face['roi']
            cv2.rectangle(frame, (x, y), (x+dx, y+dy), (0,255,0))

            ### Sorting of the 5 expressions measures
            ### to display the most likely on the screen
            exps = [(face[exp], exp) for exp in
                    ['sadness', 'happiness', 'neutral', 'surprise', 'anger']]
            exps.sort()
            max_exp = exps[-1]

            cv2.putText(frame, str(max_exp[1]), (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))

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
