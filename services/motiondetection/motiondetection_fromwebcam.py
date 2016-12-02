import StringIO
import cv2
import numpy as np
import angus

def main(stream_index):
    camera = cv2.VideoCapture(stream_index)
    camera.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
    camera.set(cv2.cv.CV_CAP_PROP_FPS, 10)

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
            x, y = map(int, target['mean_position'])
            vx, vy = map(int, target['mean_velocity'])

            cv2.circle(frame, (x, y), 5, (255,255,255))
            cv2.line(frame, (x, y), (x + vx, y + vy), (255,255,255))

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
