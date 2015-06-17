#!/usr/bin/env python
import cv2

if __name__ == '__main__':
    ### Web cam index might be different from 0 on your setup.
    stream_index = 0 
    cap = cv2.VideoCapture(stream_index)

    if not cap.isOpened():
        print "Cannot open stream of index " + str(stream_index)
        exit(1)

    print "Video stream is of resolution " + str(cap.get(3)) + " x " + str(cap.get(4))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not frame == None:
            cv2.imshow('original', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
