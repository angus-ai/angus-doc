import StringIO

import angus
import cv2
import numpy as np

if __name__ == '__main__':
    ### Retrieve web cam video stream
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Cannot open stream of index {}".format(stream_index))
        exit(1)

    print("Input stream is of resolution: {} x {}".format(camera.get(3), camera.get(4)))

    conn = angus.connect()
    service = conn.services.get_service("motion_detection", 1)

    service.enable_session()

    while camera.isOpened():
        ret, frame = camera.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, buff = cv2.imencode(".jpg", gray, [cv2.IMWRITE_JPEG_QUALITY, 80])
        buff = StringIO.StringIO(np.array(buff).tostring())

        job = service.process({"image": buff})
        res = job.result

        for target in res['targets']:
            x, y = target['mean_position']
            vx, vy = target['mean_velocity']

            cv2.circle(frame, (x, y), 5, (255,255,255))
            cv2.line(frame, (x, y), (x + vx, y + vy), (255,255,255))

        cv2.imshow('original', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    service.disable_session()

    camera.release()
    cv2.destroyAllWindows()
