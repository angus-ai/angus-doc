.. _wordspotting_v2:

Word Spotting (version 2)
=========================

This service spots specified words (or group of words) in a complex speech input.

Languages currently supported:

- English (US)
- English (GB)
- German
- Spanish (ES)
- French
- Italian

Getting Started
---------------

Using the Angus python SDK:

.. literalinclude:: wordspotting_v2.py


Input
-----

.. code-block:: javascript

   {'sound' : file,
    'vocabulary' : [{
                      "words": "hello John"
                    },
                    {
                       "words": "goodbye"
                    }],
    'sensitivity' : 0.3,
    'lang' : "en_US"}


* ``sound`` : a python ``File Object`` as returned for example by ``open()`` describing a wav file with the following format : ``PCM 16bit, Mono, 16KHz``.
* ``vocabulary`` : a data structure containing information about the words that need to be spotted.

 * ``words``: the group of words that need to be spotted written in the language specified when calling the service.
* ``sensitivity`` : modifies the ability of the algorithms to detect quiet sounds. ``[0, 1]``. The higher the value is, the better the algorithm will detect quiet sounds, but the more it will be sensitive to background noise.
* ``lang``: the code of the language to be used for recognition. Languages currently available are:

  - English (US) : ``en-US``
  - English (GB) : ``en-GB``
  - German       : ``de-DE``
  - Spanish (ES) : ``es-ES``
  - French       : ``fr-FR``
  - Italian      : ``it-IT``

Output
------

Events will be pushed to your client following that format:


.. code-block:: javascript

    {
      "utterance_length" : 1230,
      "nbests" : [
                  {
                    "words" : "hello John",
                    "confidence" : 0.75
                  }
                ]
    }

* ``utterance_length`` : length of the utterance on which the provided result has been computed (in ``ms``).
* ``words`` : the words spotted in the the given audio stream (among those specified in the ``vocabulary``).
* ``confidence`` : an estimate of the probability that the corresponding vocabulary words were spotted in the utterance.



Code Sample
-----------

**requirements**: PyAudio & Sox

This code sample retrieve the audio stream of a web cam / mic and display the result of the ``word_spotting`` service.

.. literalinclude:: wordspotting_streaming_v2.py
