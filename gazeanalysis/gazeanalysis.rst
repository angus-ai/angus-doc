Gaze Analysis
=============

What are people in front of my object looking at?


Code sample
-----------

This sample assumes that you have an image file (where some faces are visible idealy!) ready on you client.


Using the Python SDK:

.. literalinclude:: gazeanalysis.py


Input
-----

The API takes still images as input.


Output
------

Events will be pushed to your client following that format:


.. code-block:: javascript

    {
      "input_size" : [480, 640],
      "nb_faces" : 1,
      "faces" : [
                  {
                    "roi" : [250, 142, 232, 232],
                    "roi_confidence" : 0.89,
                    "head_yaw" : 0.03,
                    "head_pitch"   : 0.23,
                    "head_roll"  : 0.14,
                    "gaze_yaw"    : 0.05,
                    "gaze_pitch"  : 0.12
                  }
                ]
    }

* ``input_size`` : width and height of the input image in pixels (to be used as reference to ``roi`` output.
* ``nb_faces`` : number of faces detected in the given image
* ``roi`` : contains ``[pt.x, pt.y, width, height]`` where pt is the upper left point of the rectangle outlining the detected face.
* ``roi_confidence`` : an estimate of the probability that a real face is indeed located at the given ``roi``.
* ``head_yaw``, ``head_pitch``, ``head_roll`` : head pose orientation in radian as follows:
* ``gaze_yaw``, ``gaze_pitch`` : gaze (eyes) orientation in radian as follows:
