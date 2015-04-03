Sound Detection
===============

Is there any noticeable sound?


Code sample
-----------

Sound Localization on a sound file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make sure you have a sound file ready on your pc.

Using the Python SDK:

.. literalinclude:: sounddetection.py

Sound Localization on a sound card input stream
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the Python SDK:

.. literalinclude:: sounddetection_streaming.py


Input
-----
* ``file_path`` : filename of a wav file with the following format :
  * ``PCM 16bit, 48kHz, Stereo``
  * ``PCM 16bit, 48kHz, Mono``
  * ``PCM 16bit, 16kHz, Stereo``
  * ``PCM 16bit, 16kHz, Mono``

Output
------

Events will be pushed to your client following that format:


.. code-block:: javascript

    {
      "input_size" : 8192,
      "nb_sources" : 1,
      "sources" : [
                  {
                    "index" : 3454,
                    "energy"   : 0.23
                  },
                  {
                    "index" : 6544,
                    "energy"   : 0.56
                  }
                ]
    }

* ``input_size`` : number of frame given as input (in a stereo file, 1 frame = 1 left sample + 1 right sample).
* ``nb_sources`` : number of sound sources located.
* ``energy`` : the energy in ``[0, 1]`` of the sound measured in the given ``yaw`` direction.
