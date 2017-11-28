# -*- coding: utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

################################################################################
# Send image for age and gender computation only if there are
# some movement into the video stream.
################################################################################

import cv2
import numpy as np
import angus.client
import StringIO
from pprint import pprint

# Threshold 1: how many gray level diff is needed for a pixel "change": 0-255
t1 = 10
# Threshold 2: how many changed pixel are needed for considering the image
t2 = 50*50 # square of 50x50 pixels

# Read input webcam at 2 fps
cam = cv2.VideoCapture(0)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)
cam.set(cv2.cv.CV_CAP_PROP_FPS, 2)

win_diff = "Movement"
win_sent = "Sent"
cv2.namedWindow(win_diff, cv2.CV_WINDOW_AUTOSIZE)
cv2.namedWindow(win_sent, cv2.CV_WINDOW_AUTOSIZE)

# Read consecutive images
img1 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
img2 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

# Connect to Angus.ai
conn = angus.client.connect()
serv = conn.services.get_service("age_and_gender_estimation")

# Main loop
while True:
  # Compute the difference between two consecutive images
  diff_img = cv2.absdiff(img1, img2)
  # Threshold the value
  ret, view = cv2.threshold(diff_img, t1, 255, cv2.THRESH_BINARY)

  # Display the diff
  cv2.imshow(win_diff, view)

  # If there are enough difference in the image, send it to Angus.ai
  if np.sum(view)/255 > t2:
    # Display last sent image
    cv2.imshow(win_sent, img2)
    ret, buff = cv2.imencode(".jpg", gray, [cv2.IMWRITE_JPEG_QUALITY, 80])
    buff = StringIO.StringIO(np.array(buff).tostring())
    job = serv.process({"image": buff})
    pprint(job.result)

  # Read the next image
  img1 = img2
  img2 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

  # Wait key and exit if necessary
  if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyWindow(win_diff)
    cv2.destroyWindow(win_sent)
    break
