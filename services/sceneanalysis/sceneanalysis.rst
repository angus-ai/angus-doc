Scene analysis (Beta)
=====================


Someone has just entered the room ? Who is he ? What is he doing ?


Getting Started
---------------


Using the Python SDK:

.. literalinclude:: sceneanalysis.py

Input
-----


The API takes a stream of 2d still images as input, of format "jpg" or "png", without constraints on resolution.
However, 640p x 480p tends to be a good trade-off for both precision/recall and latencies.


Note also that the bigger the resolution, the longer the API will take to process and give a result.
The function ``process()`` takes a dictionary as input formatted as follows:


.. code-block:: javascript


    {
      'image' : binary file
      'timestamp' : "2016:10:24 18:56:23.000011"
      'camera_position' : 'ceiling' or 'facing'
      'sensitivity' : {'[event_name]' : 0.24}
    }


* ``image``: a python ``File Object`` returned for example by ``open()`` or a ``StringIO`` buffer.
* ``timestamp``: a string formated as follows "YYYY:MM:DD HH:MM:SS.MICROS".
* ``camera_position``: a preset is a list of parameters set in advance. This list of parameters is used to calibrate the API based on the camera position.
* ``sensitivity``: an optional dictionary that sets the sensitivity of the system regarding each events. For instance, If you feel that the events "appearance" is triggered too often, you can decrease its value.




Here is the list of the different presets that are available :


* ``ceiling``: this preset has to be used if the camera is a ceiling camera or if it is placed at ceiling height.
* ``facing``: this preset has to be used if the camera is placed at human height.


.. figure:: pic1.png
  :width: 300 px
  :align: center
  :alt: alternate text

  The 'facing' preset should be used in this situation

.. figure:: pic2.png
  :width: 300 px
  :align: center
  :alt: alternate text

  The 'ceiling' preset should be used in this situation












Output
----------


Events will be pushed to your client following that format. Note that if nothing happened, the events list will be empty, but the timestamp will still be updated.




.. code-block:: javascript


    {
      "timestamp" : "2016:10:24 18:56:23.000018",
      "events" : [
                  {
                    "id" : "16fd2706-8baf-433b-82eb-8c7fada847da",
                    "type" : 'appearance',
                    "confidence" : 0.96
                  }
                  {
                    "id" : "16fd2706-8baf-433b-82eb-8c7fada847da",
                    "type" : 'age',
                    "data" : 25,
                    "confidence" : 0.91
                  }
                ]
    }


* ``id`` : id of the human related to the event.
* ``type`` : type of the event, a list of event types can be found below.
* ``data`` : some event types can have a corresponding data.
* ``confidence`` : a value between 0 and 1 which reflects the probability that the event has really occurred in the scene.


The list of the possible events :


* ``'appearance'`` : a new human has just been detected.
* ``'disappearance'`` : a known human has just disappeared.
* ``'age`` : the age of the corresponding human has just been estimated, (expect 1 or 2 events of this type for each human)
* ``'gender`` : gender estimation of the corresponding human. (expect 1 or 2 events of this type for each human)
* ``'trajectory'`` : average trajectory estimation, the direction is expressed in degree (0 to 360°) with 0° as up, 90° as right, 180° as down and 270° as left.
* ``focus`` : if a human look in a specific direction for a significant time, this event is triggered with the pitch and yaw of the gaze registered in the data.
* ``'emotion'`` : if a remarkable emotion peak is detected, the event is triggered with the related emotion type registered in the data.




Code Sample
-------------------


**requirements**: opencv2, opencv2 python bindings


This code sample retrieves the stream of a web cam and display in a GUI the result of the ``scene_analysis`` service.

.. literalinclude:: sceneanalysis_fromwebcam.py
