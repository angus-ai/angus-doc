.. _age_and_gender:

Age and Gender Estimation
=========================

How old are people in front of my object?
Are they male or female?

Getting Started
---------------

Using the Python SDK:

.. literalinclude:: agegenderestimation.py


Input
-----

The API takes a stream of 2d still images as input, of format ``jpg`` or ``png``, without constraints on resolution.

Note however that the bigger the resolution, the longer the API will take to process and give a result.

The function ``process()`` takes a dictionary as input formatted as follows:

.. code-block:: javascript

    {'image' : file}

* ``image``: a python ``File Object`` as returned for example by ``open()`` or a ``StringIO`` buffer.

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


Code Sample
-----------

**requirements**: opencv2, opencv2 python bindings

This code sample retrieves the stream of a web cam and display in a GUI the result of the ``age_and_gender_estimation`` service.


.. literalinclude:: agegenderestimation_fromwebcam.py
.. image:: screenshot_agegender.png
