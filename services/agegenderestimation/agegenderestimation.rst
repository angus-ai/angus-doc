Age and Gender Estimation
=========================

How old are people in front of my object?
Are they male or female?

Code sample
-----------

This sample assumes that you have an image file (where some faces are visible ideally!) ready on your client.


Using the Python SDK:

.. literalinclude:: agegenderestimation.py


Input
-----

The API takes still images as input.

.. code-block:: javascript

    {
        "image": "attachment://image.png",
        "state": {
            "session_id": "714f0416-0de0-11e5-ab02-eca86bfe9d03"
        }
    }

* ``image`` : image in png or jpg format posted in the message as multipart with name "image.png"

Output
------

Events will be pushed to your client following that format:


.. code-block:: javascript

    {
      "input_size" : [480, 640],
      "nb_faces" : 1,
      "faces" : [
                  {
                    "roi" : [345, 223, 34, 54],
                    "roi_confidence" : 0.89,
                    "age" : 32,
                    "age_confidence" :0.87,
                    "gender" : "male",
                    "gender_confidence" : 0.95
                  }
                ]
    }


* ``input_size`` : width and height of the input image in pixels (to be used as reference to ``roi`` output.
* ``nb_faces`` : number of faces detected in the given image
* ``roi`` : contains ``[pt.x, pt.y, width, height]`` where pt is the upper left point of the rectangle outlining the detected face.
* ``roi_confidence`` : an estimate of the probability that a real face is indeed located at the given ``roi``.
* ``age`` : an age estimate (in years) of the person outlined by ``roi``.
* ``age_confidence`` : an estimate of the probability that the outlined person is indeed of age ``age``.
* ``gender`` : an estimation of the gender of the person outlined by ``roi``. Value is either ``"male"`` or ``"female"``.
* ``gender_confidence`` : an estimate of the probability that the outlined person is indeed of gender ``gender``.

Session
-------

This service can also be called in a statefull manner, allowing overall better performances as previous calls are use to refine the result. 

.. literalinclude:: agegenderestimation-session.py
