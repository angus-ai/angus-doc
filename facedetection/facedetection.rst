Face Detection
==============

Can my object see any human face? How many? Where?

Code sample
-----------

This sample assumes that you have an image file (where some faces are visible ideally!) ready on your client.


Using the Python SDK:

.. literalinclude:: facedetection.py


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
                    "roi_confidence" : 0.89
                  },
                  {
                    "roi" : [35, 323, 45, 34],
                    "roi_confidence" : 0.56
                  }
                ]
    }


* ``image_size`` : width and height of the input image in pixels (to be used as reference to ``roi`` output.
* ``nb_faces`` : number of faces detected in the given image
* ``roi`` : contains ``[pt.x, pt.y, width, height]`` where pt is the upper left point of the rectangle outlining the detected face.
* ``roi_confidence`` : an estimate of the probability that a real face is indeed located at the given ``roi``.
