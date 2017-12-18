.. _apps:

Client apps
+++++++++++
.. after-title

Our client apps are lightweight, open source scripts or executable, that you will need to install, configure and run on a your computer.

They perform two basic tasks:

1. retrieve a valid video stream. By default, one of the connected USB camera will be chosen, but you can easily modify the client app to open a different camera and even open a video file.

2. package and sent the video stream over http to our computation servers. This part can also be optimized for your needs (image resolution, frame rate, etc...).

If you need help to perform these optimizations, please contact us at support@angus.ai.


**Prerequisite**

- you have a working webcam plugged into your PC
- you have installed **OpenCV2** and **OpenCV2** python bindings. Please refer to `OpenCV documentation <http://opencv.org/>`_ to proceed, or check :ref:`faq` chapter.

On Debian-like platform, **OpenCV2** comes pre-installed, you just need to run

.. parsed-literal::

   $ sudo apt-get install python-opencv

Note also that OpenCV2 is not an absolute pre-requisite, the following code sample can easily be adapted to be used with any other way of retrieving successive frames from a video stream. If you need assistance, please contact us at contact@angus.ai

**Client Application**

Please copy/paste the following code sample in a file and run it.

.. literalinclude:: sceneanalysis_fromwebcam.py

To run this python app:

.. parsed-literal::

  $ python yourcopiedfile.py


You should see two green vectors showing what your are looking displayed on your screen:

.. image:: gwenn_onwebcam_sceneanalysis.png

The application displays by default a live view of your stream, with gaze vectors super-imposed. If you need it, it is also possible to display in real time, age, gender, emotion, etc... Please refers to the app real-time API here : (:ref:`scene-analysis-api`).
