.. _sound-detection-ref:

Sound Detection
===============

Is there any noticeable sound?


Getting Started
---------------

Using the Angus python SDK:

.. literalinclude:: sounddetection.py



Input
-----

.. code-block:: javascript

   {'sound' : file,
    'sensitivity' : 0.3}


* ``sound`` : a python ``File Object`` as returned for example by
  ``open()`` or a ``StringIO`` buffer describing a wav file with the following format : ``PCM 16bit, Mono``, without constraints on sample rate.
* ``sensitivity`` : modifies the ability of the algorithms to detect quiet sounds. ``[0, 1]``. The higher the value is, the better the algorithm will detect quiet sounds, but the more it will be sensitive to background noise.

Output
------

Events will be pushed to your client following that format:


.. code-block:: javascript

    {
      "input_size" : 8192,
      "nb_events" : 2,
      "events" : [
                  {
                    "index" : 3454,
                    "type"   : 'sound_on'
                  },
                  {
                    "index" : 6544,
                    "type"   : 'sound_off'
                  }
                ]
    }

* ``input_size`` : number of frame given as input (eg. in a stereo file, 1 frame = 1 left sample + 1 right sample).
* ``nb_events`` : number of events detected in the given input buffer.
* ``index`` : the frame index in the given input buffer where the event has been detected.
* ``type`` : ``sound_on`` if the beginning of a sound is detected. ``sound_off`` if the end of a sound is detected. Note that an event of type ``sound_on`` is always followed by an event of type ``sound_off``.



Code Sample
-----------

**requirements**: PyAudio

This code sample retrieve the audio stream of a web cam and display the result of the ``sound_detection`` service.

.. literalinclude:: sounddetection_streaming.py
