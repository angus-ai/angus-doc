Face Recognition
================

This service spots for a specified set of people in images or videos.

To be able to recognize people, this service needs to be first provided with a few pictures of each person's face.

How to prepare face samples?
----------------------------

Here are a few tips to make sure you get the most of Angus ``face_recognition`` service:

* make sure the resolution of these samples is high enough.
* make sure these samples only show a unique face to avoid any ambiguity.
* the service will perform better if you provide more than 1 sample for each person, showing a few different face expressions.


For example, the code sample shown below makes use of the following face sample (only 1 sample per people to recognize is used in that case).

.. image:: aurelien.jpg
    :width: 200 px
.. image:: gwenn.jpg
    :width: 200 px
.. image:: sylvain.jpg
    :width: 200 px

Getting Started
---------------

Using the Angus python SDK:

.. literalinclude:: facerecognition.py


Input
-----

The API takes a stream of 2d still images as input, of format ``jpg`` or ``png``, without constraints on resolution.

Note however that the bigger the resolution, the longer the API will take to process and give a result.

The function ``process()`` takes a dictionary as input formatted as follows:

.. code-block:: javascript

    {
     'image' : file,
     'album' : {"people1": [sample_1, sample_2], "people2" : [sample_1, sample_2]}
    }

* ``image``: a python ``File Object`` as returned for example by ``open()``.
* ``album`` : a dictionary containing samples of the faces that need to be spotted. Samples need to be provided to the service first with the function ``blobs.create()`` as shown in the example above. The more samples the better, but starting with only 1 sample per people is OK.

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
                    "names" : [
                                {
                                  "key" : "jamel",
                                  "confidence" : 0.75
                                },
                                {
                                  "key" : "melissa",
                                  "confidence" : 0.10
                                }
                              ]
                  }
                ]
    }


* ``input_size`` : width and height of the input image in pixels (to be used as reference to ``roi`` output.
* ``nb_faces`` : number of faces detected in the given image
* ``roi`` : contains ``[pt.x, pt.y, width, height]`` where pt is the upper left point of the rectangle outlining the detected face.
* ``roi_confidence`` : an estimate of the probability that a real face is indeed located at the given ``roi``.
* ``key`` : the key identifying a given group of samples (as specified in the ``album`` input).
* ``confidence`` : an estimate of the probability that the corresponding people was spotted in the image / video stream.


Code Sample
-----------

**requirements**: opencv2, opencv2 python bindings

This code sample retrieves the stream of a web cam and display in a GUI the result of the ``face_recognition`` service.

.. literalinclude:: facerecognition_streaming.py
