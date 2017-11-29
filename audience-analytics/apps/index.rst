.. _apps:

Client apps
+++++++++++

Our client apps are lightweight, open source scripts or executable, that you will need to install, configure and run on a your computer.
They perform two basic tasks:

1. retrieve a valid video stream. By default, one of the connected USB camera will be chosen, but you can easily modify the client app to open a different camera and even open a video file.
2. package and sent the video stream over http to our computation servers. This part can also be optimized for your needs (image resolution, frame rate, etc...).

If you need help to perform these optimizations, please contact us at support@angus.ai.

Before you proceed, please make sure you went through these steps:

+------+---------------------------------------+----------------------------+
|Steps                                         |Links                       |
+------+---------------------------------------+----------------------------+
|1     | Create an account                     |:ref:`create-account`       |
+------+---------------------------------------+----------------------------+
|2     | Get credentials for your camera       |:ref:`create-stream`        |
+------+---------------------------------------+----------------------------+
|3     | Download and configure the SDK        |:ref:`sdk`                  |
+------+---------------------------------------+----------------------------+


Then pick the language of your choice:

.. toctree::
   :maxdepth: 2

   python-app
   java-app

Don't find your preferred language? Please contact us at support@angus.ai. 
