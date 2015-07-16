#!/usr/bin/env python

import sys
import math as m
import cv2

import numpy as np
import angus

if __name__ == '__main__':
    
    ### To grab the host computer web cam instead of a given file, try:
    ### cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640);
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480);

    print "Input stream is of resolution: " + str(cap.get(3)) + " x " + str(cap.get(4))

    conn = angus.connect()
    service = conn.services.get_service('gaze_analysis', 1)
    service.enable_session()
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if(frame != None):
            ### angus.ai computer vision services require gray images right now.
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite("image.png", gray)

            ### jpg, png images are currently supported        
            job = service.process({"image": open('image.png')})
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

                    roll = res['faces'][i]['head_roll']
                    yaw = res['faces'][i]['head_yaw']
                    pitch = res['faces'][i]['head_pitch']
                    
                    center = (int(roi[0] + 0.5*roi[2]), int(roi[1] + 0.5*roi[3]))
                        
                    phi = pitch
                    psi = roll
                    theta = - yaw
                    
                    length = 150
                    ### See here for details : https://en.wikipedia.org/wiki/Rotation_formalisms_in_three_dimensions
                    xvec = length*(m.sin(phi)*m.sin(psi) - m.cos(phi)*m.sin(theta)*m.cos(psi))
                    yvec = - length*(m.sin(phi)*m.cos(psi) - m.cos(phi)*m.sin(theta)*m.sin(psi))
                    vec = (int(xvec), int(yvec))

                    cv2.line(frame, center, (center[0]+vec[0], center[1]+vec[1]), (255, 0, 0), 3)
            

            cv2.imshow('original', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print "None image read"


    ### Disabling session on the server
    service.disable_session()

    cap.release()
    cv2.destroyAllWindows()
