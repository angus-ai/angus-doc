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
    'vocabulary' : {"word1": [sample_1, sample_2], "word2" : [sample_1, sample_2]},
    'sensitivity' : 0.3,
    'lang' : "en_US"}


* ``sound`` : a python ``File Object`` as returned for example by ``open()`` describing a wav file with the following format : ``PCM 16bit, Mono``, without constraints on sample rate.
* ``vocabulary`` : a dictionary containing samples of the words that need to be spotted. Samples need to be provided to the service first with the function ``blobs.create()`` as shown in the example above. The more samples the better, but starting with only 1 sample per word is OK.
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
                    "key" : "turn wifi on",
                    "confidence" : 0.75
                  },
                  {
                    "key" : "turn wifi off",
                    "confidence"   : 0.10
                  }
                ]
    }

* ``utterance_length`` : length of the utterance on which the provided result has been computed (in ``ms``).
* ``key`` : the key identifying a given group of samples (as specified in the ``vocabulary`` input).
* ``confidence`` : an estimate of the probability that the corresponding vocabulary words were spotted in the utterance.



Code Sample
-----------

**requirements**: PyAudio & Sox

This code sample retrieve the audio stream of a web cam / mic and display the result of the ``word_spotting`` service.

.. literalinclude:: wordspotting_streaming.py
