Motion Detection
================

Is there anything moving in frontof my object? Where exactly?

Code sample
-----------

This sample assumes that you have an image file (where some faces are visible ideally!) ready on your client.


Using the Python SDK:

.. literalinclude:: motiondetection.py


Input
-----

The API takes still images as input.


Output
------

Events will be pushed to your client following that format:


.. code-block:: javascript


    {

      "image_size" : [480, 640],
      "nb_targets": 1
      "targets":
                [
                  {
                    "mean_position" : [34, 54],
                    "mean_velocity" : [5, 10],
                    "confidence" : 45
                  }
                ]
    }


* ``image_size`` : width and height of the input image in pixels.
* ``mean_position`` : ``[pt.x, pt.y]`` where ``pt`` is the center of gravity of the moving pixels in the image.
* ``mean_velocity`` : ``[v.x, v.y]`` where ``v`` is the average velocity of the moving pixels in the image.
* ``confidence`` : in ``[0,1]`` measures how significant is the motion in the image (is a function of the number of keypoints moving in the image).
