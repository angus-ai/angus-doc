# -*- coding: utf-8 -*-
import StringIO

import angus.client
import cv2
import numpy as np
import datetime
import pytz

def main(stream_index):
    camera = cv2.VideoCapture(stream_index)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    camera.set(cv2.CAP_PROP_FPS, 10)

    if not camera.isOpened():
        print("Cannot open stream of index {}".format(stream_index))
        exit(1)

    print("Input stream is of resolution: {} x {}".format(camera.get(3), camera.get(4)))

    conn = angus.client.connect()
    service = conn.services.get_service("scene_analysis", version=1)
    service.enable_session()

    while camera.isOpened():
        ret, frame = camera.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, buff = cv2.imencode(".jpg", gray, [cv2.IMWRITE_JPEG_QUALITY, 80])
        buff = StringIO.StringIO(np.array(buff).tostring())

        t = datetime.datetime.now(pytz.utc)
        job = service.process({"image": buff,
                               "timestamp" : t.isoformat(),
                               "camera_position": "facing",
                               "sensitivity": {
                                   "appearance": 0.7,
                                   "disappearance": 0.7,
                                   "age_estimated": 0.4,
                                   "gender_estimated": 0.5,
                                   "focus_locked": 0.9,
                                   "emotion_detected": 0.4,
                                   "direction_estimated": 0.8
                               },
        })
        res = job.result

        if "error" in res:
            print(res["error"])
        else:
            # This parses the events
            if "events" in res:
                for event in res["events"]:
                    value = res["entities"][event["entity_id"]][event["key"]]
                    print("{}| {}, {}".format(event["type"],
                                              event["key"],
                                              value))

            # This parses the entities data
            for key, val in res["entities"].iteritems():
                x, y, dx, dy = map(int, val["face_roi"])
                cv2.rectangle(frame, (x, y), (x+dx, y+dy), (0, 255, 0), 2)

        cv2.imshow("original", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    service.disable_session()

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    ### Web cam index might be different from 0 on your setup.
    ### To grab a given video file instead of the host computer cam, try:
    ### main("/path/to/myvideo.avi")
    main(0)
