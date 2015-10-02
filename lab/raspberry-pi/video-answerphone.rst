The coffee machine team assistant
=================================

In this tutorial we will look into how turn a Raspberry Pi, a web cam and a speaker into a coffee machine assistant.

The concept
-----------

That concept might be a little obscure!

We were thinking about a funny smart device that a team could use collectively.
Then we thought that it would be great if we someone going to the coffee machine could leave a private message (work related or not) to another member of the team who would come to the coffee machine later. Of course, such a function could be filled up with an app running on a tablet. But we wanted something more 'futuristic'
where no login nor typing on a touch screen is required (cause you are holding your coffee, right!).

What we will build together here is exactly that: a hands free
smart answering machine for team building!

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




Sound out Issue
---------------

When you use PyAudio to play sound directly on the audio output
controlled by the bcm2835, you could have some difficult to
get a clean sound. Check this `thread
<https://github.com/raspberrypi/linux/issues/994>`_ for example.

We have succeeded to fix this issue on our Raspberry Pi by defining a
new alasa output thanks to a local configuration file ``.asoundrc``
(check the `doc
<http://www.alsa-project.org/main/index.php/Asoundrc>`_ for more
information) put in your
home directory or a global setting in ``/etc/asound.conf``:

.. code-block:: bash

    pcm.convert {
         type plug;
         slave {
               pcm default;
               rate 48000;
         }
    }

This piece of code creates a new output device that resamples the input
to fit to 48Khz and send the sound to the standard output (by default
the bcm2835 audio jack output).

Now you can use this new device to play sound and prevent bad quality.

