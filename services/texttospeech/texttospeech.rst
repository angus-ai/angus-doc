Text To Speech
==============

This service generates a sound file (".wav") from a any given text in the following languages:

- English (US)
- English (GB)
- German
- Spanish (ES)
- French
- Italian


Getting Started
---------------

Using Angus python SDK:

.. literalinclude:: texttospeech.py


Input
-----

The function ``process()`` takes a dictionary formatted as follows:

.. code-block:: javascript

    {'text' : "Hello guys",
     'lang' : "en-US"}

* ``text``: a string containing the text to be syntesized.
* ``lang``: the code of the language to be used for synthesis. Languages currently available are:

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
      "status" : 201,
      "sound" : "'eJzsvHdUFNm6N1yhEzQ ... jzf//+T/jj/A8b0r/9"
    }

* ``status``: the http status code of the request.
* ``sound`` : contains the synthesized sound file (.wav) as a compressed (zlib), base64 string. See the code sample below for an example of how to decode it in Python.


Code Sample
-----------


This code sample uses Angus ``text_to_speech`` service to synthesize "hi guys, how are you today?".

.. literalinclude:: texttospeech_example.py
