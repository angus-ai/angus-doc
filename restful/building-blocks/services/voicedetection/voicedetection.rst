Voice Detection (Deprecated)
============================

.. warning::

   Voice detection service will be stopped in a near future (2018/05/01).
   Please contact the angus.ai team (contact@angus.ai) if you have questions.

This service takes an audio stream as an input and tries to discriminate what is human voice and what is not.
If detecting noise in general, and not specifically human voice, use :ref:`sound-detection-ref` instead.

Getting Started
---------------

Using the Angus python SDK:

.. literalinclude:: voicedetection.py



Input
-----

.. code-block:: javascript

   {'sound' : file,
    'sensitivity' : 0.3}


* ``sound`` : a python ``File Object`` as returned for example by
  ``open()`` or a ``StringIO`` buffer describing a wav file with the following format : ``PCM 16bit, Mono``, without constraints on sample rate.
* ``sensitivity`` : modifies the ability of the algorithms to detect quiet voices. ``[0, 1]``. The higher the value is, the better the algorithm will detect quiet voices, but the more it will be sensitive to background noise.

Output
------

Events will be pushed to your client following that format:


.. code-block:: javascript

    {
      "voice_activity" : "SILENCE"
    }

* ``voice_activity`` : this field takes 4 different values: ``SILENCE`` when no voice is detected,
  ``VOICE`` when voice is detected, ``ON`` when a transition occurs between ``SILENCE``
  and ``VOICE``, and ``OFF`` when a transition occurs between ``VOICE`` and ``SILENCE``.


Code Sample
-----------

**requirements**: PyAudio

This code sample retrieve the audio stream of a web cam and display the result of the ``voice_detection`` service.

.. literalinclude:: voicedetection_streaming.py
