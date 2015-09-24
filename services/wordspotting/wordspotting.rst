Word Spotting (Beta)
====================

This service spots specified words (or group of words) in a complex speech input.

Languages currently supported:

- English (US)
- English (GB)
- German
- Spanish (ES)
- French
- Italian

How does this compare with other ASR services ?
-----------------------------------------------

Good question!

Speech Recognition (ASR) services can be splitted in 2 groups:

* **speech to text**: translate every word contained in a speech signal (in a given language).

 * **pros**: understand everything
 * **cons**: poor reliability under noisy condition (without specific hardware)
 * **use case**: SMS dictation, or vocal interfaces (SIRI) when ``distance(speaker, mic)`` is small (< 1m)
 * **examples**: Google Speech API, Nuance STT API.

* **grammar based ASR**: recognize the exact words & sentences that you specified and will ignore everything else.

 * **pros**: reliable in noisy environment (with the right acoustical model).
 * **cons**: recognition limited to the specified grammar and noise ready acoustical model may be hard to find (especially for non-english languages).
 * **use case**: command & control of various devices (e.g. GPS)
 * **examples**: Sphinx, Kaldi.


Many of us want to talk to machines in real-life environments (``distance(speaker, mic)`` greater than 1m),
without going through the configuration of the great tool suites that are Sphinx and Kaldi or because we lack noise robust acoustical models in a given language.

For this purpose, we have setup a **Grammar based ASR** service specifically designed to only spot specified words / groups of words in a complex speech input, a task known as **word spotting**.

..
    The technology used in this service, different from most currently available ASR service, allow for a good noise and reverberation robustness but requires the vocabulary to be provided as sound samples (and not as bare strings).

    How to prepare samples?
    -----------------------

    The more sample of word or sentence you provide, the better the service will perform.

    To prepare these samples, you can use an audio recording application (like Audacity).

    These samples need to be provided to the service with the following format ``mono, 16kHz, 16bit PCM``.
    In Audacity, go to Edit > Preferences... > Quality, and set the Sampling settings to ``16000Hz`` and ``16-bit``.

    Press ``record`` and pronounce several time each word you want to have recognized. If you want to have multiple people using the service, have the word pronounced by several people.

    Then extract each sample from the signal by using the appropriate selection + export procedure. In Audacity, use the ``File > Export Selected Audio...`` for each sample you want to extract.

    .. image:: audacity.png

Getting Started
---------------

Using the Angus python SDK:

.. literalinclude:: wordspotting.py


Input
-----

.. code-block:: javascript

   {'sound' : file,
    'vocabulary' : [{
                      "words": "hello John",
                      "samples": [s1, s2] //optional
                    },
                    {
                       "words": "goodbye",
                       "samples": [s3, s4] //optional
                    }],
    'sensitivity' : 0.3,
    'lang' : "en_US"}


* ``sound`` : a python ``File Object`` as returned for example by ``open()`` describing a wav file with the following format : ``PCM 16bit, Mono, 16KHz``.
* ``vocabulary`` : a data structure containing information about the words that need to be spotted.

 * ``words``: the group of words that need to be spotted written in the language specified when calling the service.
 * ``samples``: providing samples is currently only required when using ``version=1`` of this service. If you use the default version (``version=2``), you do not need to provide samples.
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

.. literalinclude:: wordspotting_streaming.py
