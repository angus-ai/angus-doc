Sound Localization
==================

Where is the sound coming from?


Getting Started
---------------

Using the Angus python SDK:

.. literalinclude:: soundlocalization.py


Input
-----

.. code-block:: javascript

   {'sound' : file,
    'baseline' : 0.7,
    'sensitivity' : 0.3}


* ``file`` : a python ``File Object`` as returned for example by ``open()`` describing a wav file with the following format: ``PCM 16bit, 48kHz, Stereo``.
* ``baseline`` : distance between the 2 microphones of the array in ``meters``.
* ``sensitivity`` : modifies the ability of the algorithms to locate quiet sounds. ``[0, 1]``. The higher the value is, the better the algorithm will locate quiet sounds, but the more it will be sensitive to background noise.

Output
------

Events will be pushed to your client following that format:


.. code-block:: javascript

    {
      "input_size" : 8192,
      "nb_sources" : 1,
      "sources" : [
                  {
                    "index" : 345,
                    "yaw" : 0.156,
                    "confidence" : 0.53,
                  }
                ]
    }

* ``input_size`` : number of frame given as input (in a stereo file, 1 frame = 1 left sample + 1 right sample).
* ``nb_sources`` : number of sound sources located.
* ``yaw`` : angle of the sound source in radian as shown below:
* ``confidence`` : an estimate of the probability that a real sound source is indeed located at the given ``yaw``.



Code Sample
-----------

This sample assumes that you have a sound card able to record in stereo.

**requirements**: PyAudio

This code sample retrieve the audio stream of a recording device and display the result of the ``sound_localization`` service.

.. literalinclude:: soundlocalization_streaming.py
