Sound Localization
==================

Where is the sound coming from?


Code sample
-----------

Sound Localization on a sound file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This sample assumes that you have a stereo sound file ready on your client.

Using the Python SDK:

.. literalinclude:: soundlocalization.py

Sound Localization on a sound card input stream
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This sample assumes that you have a sound card able to record in stereo.
The API supports currently, PCM 16bits at 48kHz streams.

Using the Python SDK:

.. literalinclude:: soundlocalization_streaming.py


Input
-----
* ``file_path`` : filename of a wav file with the following format : ``PCM 16bit, 48kHz, Stereo``.
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
