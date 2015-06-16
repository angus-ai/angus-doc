Motion Detection
================

Is there anything moving in front of my object? Where exactly?

Getting Started
---------------

Using Angus python SDK:

.. literalinclude:: motiondetection.py


Input
-----

The API takes a stream of 2d still images as input, of format ``jpg`` or ``png``, without constraints on resolution.

Note however that the bigger the resolution, the longer the API will take to process and give a result.

The function ``process()`` takes a dictionary as input formatted as follows:

.. code-block:: javascript

    {'image' : file}

* ``file``: a python ``File Object`` as returned for example by ``open()``.

Output
------

Events will be pushed to your client following that format:


.. code-block:: javascript


    {

      "input_size" : [480, 640],
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


* ``input_size`` : width and height of the input image in pixels.
* ``mean_position`` : ``[pt.x, pt.y]`` where ``pt`` is the center of gravity of the moving pixels.
* ``mean_velocity`` : ``[v.x, v.y]`` where ``v`` is the average velocity of the moving pixels.
* ``confidence`` : in ``[0,1]`` measures how significant the motion is (a function of the number of keypoints moving in the same direction).


Code Sample
-----------

**requirements**: opencv2, opencv2 python bindings

This code sample retrieves the stream of a web cam and display in a GUI the result of the ``motion_detection`` service.


.. literalinclude:: motiondetection_fromwebcam.py
