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
------

Events will be pushed to your client following that format. Note that if nothing happened, the events list will be empty, but the timestamp will still be updated.



.. code-block:: javascript


    {
      "timestamp" : "UTC-2016-10-24 18:56:23.000018+4",
      "events" : [
                  {
                    "entity_id" : "16fd2706-8baf-433b-82eb-8c7fada847da",
                    "entity_type" : 'human',
                    "type" : 'age_estimated',
                    "confidence" : 0.96
                  }
                ],
      "entities" : {"16fd2706-8baf-433b-82eb-8c7fada847da": {
                                                                'face_roi': [339, 264, 232, 232],
                                                                'face_roi_confidence': 0.7132946138717671,
                                                                'full_body_roi': [59.43999999999994,
                                                                                  14.599999999999909,
                                                                                  791.1200000000001,
                                                                                  1798.0],
                                                                'full_body_roi_confidence': 0.7132946138717671,

                                                                'age': 25,
                                                                'age_confidence': 0.34,

                                                                'gender': "male",
                                                                'gender_confidence': 0.9999379577720902,

                                                                'emotion_anger': 0.04,
                                                                'emotion_surprise': 0.06563202096657506,
                                                                'emotion_sadness': 0.142974245872324,
                                                                'emotion_neutral': 0.5381274632225086,
                                                                'emotion_happiness': 0.2116314775603314,
                                                                'emotion_smiling_degree': 0.42685544831147126,
                                                                'emotion_confidence': 0.37659382447418466,

                                                                'face_eye_left': [414, 346],
                                                                'face_eye_right': [499, 339],
                                                                'face_mouth': [456, 401],
                                                                'face_nose': [456, 401],
                                                                'face_confidence': 0.37659382447418466,

                                                                'gaze_confidence': 0.37659382447418466,
                                                                'gaze_pitch': 0.023609825318146704,
                                                                'gaze_yaw': 0.14999280047675256,

                                                                'head_pitch': -0.0544808106511141,
                                                                'head_roll': -0.056476524426443575,
                                                                'head_yaw': -0.17511312320692696,
                                                                'head_confidence': 0.37659382447418466,

                                                                'displacement': [0.06296296296296296, -0.10555555555555556]
                                                            }
                }
    }


* ``entity_id`` : id of the human related to the event.
* ``entity_type`` : type of the entity, only "human" are currently supported
* ``type`` : type of the event, a list of event types can be found below.
* ``confidence`` : a value between 0 and 1 which reflects the probability that the event has really occurred in the scene.


The list of the possible events :


* ``'appearance'`` : a new human has just been detected.
* ``'disappearance'`` : a known human has just disappeared.
* ``'age_estimated`` : the age of the corresponding human has just been estimated, (expect 1 or 2 events of this type for each human)
* ``'gender_estimated`` : gender estimation of the corresponding human. (expect 1 or 2 events of this type for each human)
* ``focus_locked`` : if a human look in a specific direction for a significant time, this event is triggered with the pitch and yaw of the gaze registered in the data.
* ``focus_unlocked`` : if a human look in a specific direction for a significant time, this event is triggered with the pitch and yaw of the gaze registered in the data.
* ``emotion_detected`` : if a remarkable emotion peak is detected, the event is triggered with the related emotion type registered in the data.




Code Sample
-------------------


**requirements**: opencv2, opencv2 python bindings


This code sample retrieves the stream of a web cam and display in a GUI the result of the ``scene_analysis`` service.

.. literalinclude:: sceneanalysis_fromwebcam.py
