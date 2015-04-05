Face Expression Estimation
==========================

Are people in front looking happy or surprised?

Code sample
-----------

This sample assumes that you have an image file (where some faces are visible ideally!) ready on your client.


Using the Python SDK:

.. literalinclude:: faceexpressionestimation.py


Input
-----

The API takes still images as input.


Output
------

Events will be pushed to your client following that format:


.. code-block:: javascript

    {
      "image_size" : [480, 640],
      "nb_faces" : 2,
      "faces" : [
                  {
                    "roi" : [345, 223, 34, 54],
                    "roi_confidence" : 0.89,
                    "neutral" : 0.1,
                    "happiness" : 0.2,
                    "surprise" : 0.7,
                    "anger" : 0.01,
                    "sadness" : 0.1,
                  }
                ]
    }


* ``image_size`` : width and height of the input image in pixels (to be used as reference to ``roi`` output.
* ``nb_faces`` : number of faces detected in the given image
* ``roi`` : contains ``[pt.x, pt.y, width, height]`` where pt is the upper left point of the rectangle outlining the detected face.
* ``roi_confidence`` : an estimate of the probability that a real face is indeed located at the given ``roi``.
* ``neutral``, ``happiness``, ``surprise``, ``anger``, ``sadness`` : a float in ``[0, 1]`` measuring the intensity of the corresponding face expression.
