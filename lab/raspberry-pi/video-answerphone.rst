Smart message box
=================

In this tutorial we will look into how turn a Raspberry Pi, a web cam and a speaker into a smart message box.

The concept
-----------

That concept might be a little obscure!

We were thinking about a funny smart device that a team / a family / flatmates could use collectively.
Then we thought that it would be great if we someone going to the coffee machine could leave a private message (work related or not) to another member of the team who would come to the coffee machine later. Of course, such a function could be filled up with an app running on a tablet. But we wanted something more fun
where no login nor typing on a touch screen is required (cause you are holding your coffee, right!).

The control flow is as follows:

 1. The device wait to see a new person in front
 2. If nobody is there, run a small tagline as "come on"
 3. When a face is detected, find the identity of the person
 4. Play all messages for this person (if any)
 5. When no message left, propose to leave a new message
 6. Record the message until "stop" is said
 7. Ask for confirmation
 8. Ask for the recipient's name
 9. Store the identity, the recipient and the date
 10. Say goodbye
 11. Go back to 1 and repeat.

Hardware
--------

The hardware indicated below is only a suggestion, it is possible to build you assistant using different options (as long as you have a video/audio input and en audio output).


* Raspberry Pi Model B/B+/2
* 4GB SD Card
* USB web cam (with a microphone)
* Powered speakers with a 3.5mm jack input

Installation
------------

OpenCV
++++++

OpenCV will be used to retrieve and format the video stream captured by your web cam.
Please follow the steps detailed on opencv installation `guides`_.

Note that on most operating systems, opencv libraries are available as binaries through package managers.
On Ubuntu, typing this command is enough to have OpenCV installed::

	sudo apt-get install python-opencv

.. _guides: http://docs.opencv.org/doc/tutorials/introduction/table_of_content_introduction/table_of_content_introduction.html


PyAudio
+++++++

PyAudio will be used to retrieve audio buffer recorded by your web cam.
As for OpenCV, you can either follow the instructions found `here`_ or look into your operating system package manager.

On Ubuntu, typing this command is enough to have PyAudio installed::

	sudo apt-get install python-pyaudio

.. _here: https://people.csail.mit.edu/hubert/pyaudio/

Angus SDK
+++++++++

We will use Angus API to provide voice and users recognition.
Please refers to these `steps`_ to install the python SDK.

.. _steps: http://angus-doc.readthedocs.org/en/latest/getting-started/python.html#install-the-angus-sdk


Code
++++

Retrieve the code of this project on github::

  git clone https://github.com/angus-ai/angus-smartmessagebox.git



Configuration
-------------

Camera and Mic
++++++++++++++

Face Recognition
++++++++++++++++

Usage
-----

FAQ
---

Licence
-------
 * Sound issues:

	When using PyAudio to play sound directly on the audio output
	controlled by the bcm2835, you may have some difficulties to
	get a clean sound. Check this `thread
	<https://github.com/raspberrypi/linux/issues/994>`_ for example.

	You can fix this issue by defining a
	new alsa output by editing a local configuration file ``.asoundrc``
	(check the `doc
	<http://www.alsa-project.org/main/index.php/Asoundrc>`_ for more
	information) in your
	home directory or a global setting in ``/etc/asound.conf``:

	.. code-block:: bash

	    pcm.convert {
	         type plug;
	         slave {
	               pcm default;
	               rate 48000;
	         }
	    }

	This piece of code creates a new output device that resamples to 48Khz before sending the signal to the standard output (by default
	the bcm2835 audio jack output).


