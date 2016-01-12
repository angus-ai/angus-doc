#!/usr/bin/env python
import StringIO

import sys
import math as m
import cv2
import operator
import numpy as np
import angus

if __name__ == '__main__':
    
    ### To grab a given video file instead of the host computer cam, try:
    ### cap = cv2.VideoCapture("/path/to/myvideo.avi")
    cap = cv2.VideoCapture(0)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640);
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480);

    print "Input stream is of resolution: " + str(cap.get(3)) + " x " + str(cap.get(4))

    conn = angus.connect()
    service = conn.services.get_service('face_expression_estimation', 1)
    service.enable_session()
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if(frame != None):
            ### angus.ai computer vision services require gray images right now.
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            ret, buff = cv2.imencode(".png", gray)
            buff = StringIO.StringIO(np.array(buff).tostring())

            job = service.process({"image": buff})
            res = job.result

            print "---------- Raw answer from Angus.ai -----------" 
            print res
            print "-----------------------------------------------" 

            
            if res['nb_faces'] > 0:
                for i in range(0,res['nb_faces']):
                    roi = res['faces'][i]['roi']
                    cv2.rectangle(frame, (int(roi[0]), int(roi[1])), 
                                         (int(roi[0] + roi[2]), int(roi[1] + roi[3])),
                                         (0,255,0))
                    face = res['faces'][i]
                    ### Sorting of the 5 expressions measures
                    ### to display the most likely on the screen
                    exp = {'sadness':face['sadness'],
                           'happiness':face['happiness'],
                           'neutral':face['neutral'],
                           'surprise':face['surprise'],
                           'anger':face['anger']}
                    exp_sorted = sorted(exp.items(), key=operator.itemgetter(1))    
                    exp_sorted.reverse()
                    max_exp = exp_sorted[0]                    
                    
                    cv2.putText(frame, 
                                str(max_exp[0]), 
                                (int(roi[0]), int(roi[1])), 
                                cv2.FONT_HERSHEY_SIMPLEX, 
                                1, 
                                (255, 255, 255))
                    
            cv2.imshow('original', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print "None image read"


    ### Disabling session on the server
    service.disable_session()

    cap.release()
    cv2.destroyAllWindows()
