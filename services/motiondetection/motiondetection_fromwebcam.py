#!/usr/bin/env python

import cv2
import angus

if __name__ == '__main__':
    ### Retrieve web cam video stream
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print "Cannot open webcam \"0\" stream."

    print "Video stream is of resolution " + str(cap.get(3)) + " x " + str(cap.get(4))

    conn = angus.connect()
    service = conn.services.get_service("motion_detection", 1)

    service.enable_session()

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not frame == None:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite("image.png", gray)

            job = service.process({"image": open("image.png")})
            res = job.result

            if res['nb_targets'] > 0:
                mp = res['targets'][0]['mean_position']
                v = res['targets'][0]['mean_velocity']
                cv2.circle(frame, (int(mp[0]), int(mp[1])), 5, (255,255,255))
                cv2.line(frame,
                         (int(mp[0]), int(mp[1])),
                         (int(mp[0]) + int(v[0]), int(mp[1]) + int(v[1])),
                         (255,255,255))


            cv2.imshow('original', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    service.disable_session()

    cap.release()
    cv2.destroyAllWindows()
