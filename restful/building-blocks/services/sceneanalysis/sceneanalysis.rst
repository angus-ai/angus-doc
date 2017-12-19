.. _scene_analysis:

Scene Analysis
==============

This is Angus.ai main API that is meant to help you leverage your video streams by extracting:

* how many people are visible?
* who is looking at what?
* are people only passing by or do they stop?
* do they look happy?
* what are their age and gender?
* etc...

Besides the code samples provided on this page, you can find a first way to use the API on GitHub
`here <https://github.com/angus-ai/angus-demos>`_

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
      "image" : binary file,
      "timestamp" : "2016-10-26T16:21:01.136287+00:00",
      "camera_position" : "ceiling" or "facing",
      "sensitivity": {
                        "appearance": 0.7,
                        "disappearance": 0.7,
                        "age_estimated": 0.4,
                        "gender_estimated": 0.5,
                        "focus_locked": 0.9,
                        "emotion_detected": 0.4,
                        "direction_estimated" : 0.8
                     },
    }


* ``image``: a python ``File Object`` returned for example by ``open()`` or a ``StringIO`` buffer.
* ``timestamp``: a string formated using the iso 8601 UTC date format.
* ``camera_position``: a preset is a list of parameters set in advance. This list of parameters is used to calibrate the API based on the camera position.
* ``sensitivity``: an optional dictionary that sets the sensitivity (between 0 and 1) of the system regarding each events. For instance, If you feel that the events "appearance" is triggered too often, you can decrease its value.
* ``store``: store process results (not video data) for analytics dashboard (Beta)

Here is the list of the different presets that are available :


* ``ceiling``: this preset has to be used if the camera is a ceiling camera or if it is placed at ceiling height.
* ``facing``: this preset has to be used if the camera is placed at human height.


.. figure:: pic1.png
  :width: 300 px
  :align: center
  :alt: alternate text

  The "facing" preset should be used in this situation

.. figure:: pic2.png
  :width: 300 px
  :align: center
  :alt: alternate text

  The "ceiling" preset should be used in this situation

.. _scene-analysis-api:

Output API
----------

Events will be pushed to your client following that format. Note that if nothing happened, the events list will be empty, but the timestamp will still be updated.



.. code-block:: javascript


    {
      "timestamp" : "2016-10-26T16:21:01.136287+00:00",
      "events" : [
                  {
                    "entity_id" : "16fd2706-8baf-433b-82eb-8c7fada847da",
                    "entity_type" : "human",
                    "type" : "age_estimated",
                    "confidence" : 0.96,
                    "key" : "age"
                  }
                ],
      "entities" : {"16fd2706-8baf-433b-82eb-8c7fada847da":
                             {
                              "face_roi": [339, 264, 232, 232],
                              "face_roi_confidence": 0.71,
                              "full_body_roi": [59, 14, 791, 1798],
                              "full_body_roi_confidence": 0.71,

                              "age": 25,
                              "age_confidence": 0.34,

                              "gender": "male",
                              "gender_confidence": 0.99,

                              "emotion_anger": 0.04,
                              "emotion_surprise": 0.06,
                              "emotion_sadness": 0.14,
                              "emotion_neutral": 0.53,
                              "emotion_happiness": 0.21,
                              "emotion_smiling_degree": 0.42,
                              "emotion_confidence": 0.37,

                              "face_eye": [[414, 346], [499, 339]],
                              "face_mouth": [456, 401],
                              "face_nose": [456, 401],
                              "face_confidence": 0.37,

                              "gaze": [0.02, 0.14],
                              "gaze_confidence": 0.37,

                              "head": [-0.1751, -0.0544, -0.0564]
                              "head_confidence": 0.3765,

                              "direction": "unknown"
                             }
                }
    }


* ``timestamp``: a string formated using the iso 8601 UTC date format.
* ``entity_id`` : id of the human related to the event.
* ``entity_type`` : type of the entity, only "human" is currently supported
* ``type`` : type of the event, a list of event types can be found below.
* ``confidence`` : a value between 0 and 1 which reflects the probability that the event has really occurred in the scene.
* ``key`` : a string which indicates which value has been updated in the attached entities list.

* ``face_roi`` : contains ``[pt.x, pt.y, width, height]`` where pt is the upper left point of the rectangle outlining the detected face.
* ``face_roi_confidence`` : an estimate of the probability that a real face is indeed located at the given ``roi``.
* ``full_body_roi`` : contains ``[pt.x, pt.y, width, height]`` where pt is the upper left point of the rectangle outlining the detected human body.
* ``full_body_roi_confidence`` : an estimate of the probability that a real human body is indeed located at the given ``roi``.

* ``age`` : an age estimate (in years) of the person outlined by ``roi``.
* ``age_confidence`` : an estimate of the probability that the outlined person is indeed of age ``age``.
* ``gender`` : an estimation of the gender of the person outlined by ``roi``. Value is either ``"male"`` or ``"female"``.
* ``gender_confidence`` : an estimate of the probability that the outlined person is indeed of gender ``gender``.

* ``emotion_neutral``, ``emotion_happiness``, ``emotion_surprise``, ``emotion_anger``, ``emotion_sadness`` : a float in ``[0, 1]`` measuring the intensity of the corresponding face expression.
* ``face_eye``, ``face_mouth``, ``face_nose`` : the coordinate of the detected eyes, nose and mouth in pixels.
* ``head`` : head pose orientation (yaw, pitch and roll) in radian
* ``gaze`` : gaze orientation (yaw, pitch) in radian
* ``direction`` : an indication of the average direction of the person. Value is either ``"unknown"``, ``"up"``, ``"right"``, ``"left"`` or ``"down"``.



The list of the possible events :


* ``"appearance"`` : a new human has just been detected.
* ``"disappearance"`` : a known human has just disappeared.
* ``"age_estimated"`` : the age of the corresponding human has just been estimated, (expect 1 or 2 events of this type for each human)
* ``"gender_estimated"`` : gender estimation of the corresponding human. (expect 1 or 2 events of this type for each human)
* ``"focus_locked"`` : if a human look in a specific direction for a significant time, this event is triggered with the pitch and yaw of the gaze registered in the data.
* ``"emotion_detected"`` : if a remarkable emotion peak is detected, the event is triggered with the related emotion type registered in the data.
* ``"direction_estimated"`` : if the human stays enough time in order to determine his average direction.




Code Sample
-------------------


**requirements**: opencv2, opencv2 python bindings


This code sample retrieves the stream of a web cam and display in a GUI the result of the ``scene_analysis`` service.

.. literalinclude:: sceneanalysis_fromwebcam.py
