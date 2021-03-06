.. _sdk:

Python SDK
----------

Our SDK are here to help you call Angus.ai http API easily, without drafting the appropriate HTTP request yourself.
Installing and configuring one of our SDKs is needed to run:

- the audience analytics client applications shown here (:ref:`apps`)
- and/or the building blocks code samples documented here (:ref:`buidling-blocks`)

**Don't want to use Python?**

If the SDK in the language of your choice is not provided here, you can:

- contact us at support@angus.ai.
- or use our http API directly by referring to our full API reference (:ref:`http-api`)

.. after-title

**Requirements**

- The SDK is Python3 compatible but the documentation code snippets are only Python2 compatible.

- Also, you might want (not mandatory) to create a python virtual environnement with **virtualenv** in order to install the sdk in there.
To do so, please refer to the following `virtualenv guide <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_ for more information.

Install the SDK
+++++++++++++++

Open a terminal and install the angus python sdk with pip. If you do not use **virtualenv** you may need to be root, administrator or super user depending on your platform (use sudo on linux platform).

.. parsed-literal::

        $ pip install angus-sdk-python

Configure your SDK
++++++++++++++++++

You must configure your sdk with the keys you received by creating a stream `here <https://console.angus.ai/>`__.
These keys are used to authenticate the requests you are about to send.

Your API credentials can be retrieved by clicking on "Show details" on the stream you just created.

In a terminal, type:

.. parsed-literal::

   $ angusme
   Please choose your gateway (current: https://gate.angus.ai):
   Please copy/paste your client_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   Please copy/paste your access_token: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

Fill in the "client_id" prompt with the "login" given on the interface and
the "access_token" prompt with the "password" given on the interface.

On **Windows** system, if angusme does not work, please refer to the :ref:`faq` for more details.

You can check this setup went well by typing the following command and checking that our server sees you:

.. parsed-literal::

   $ angusme -t
   Server: https://gate.angus.ai
   Status: OK

If this command gives you an error, check that you enter the right "client_id" and "acccess_token".
You can do this by re-typing "angusme" in a command prompt.

If you need help, contact us here : support@angus.ai !

.. stop-here

Access your sensor stream
+++++++++++++++++++++++++

Angus.ai API is specifically designed to process a video stream. This section will show you a way to access the stream of a webcam plugged to your computer by using OpenCV2.

Note that the following code sample can be adapted to process a video file instead.

Note also that OpenCV2 is not an absolute pre-requisite, the following code sample can easily be adapted to be used with any other way of retrieving successive frames from a video stream. If you need assistance, please contact us at support@angus.ai

*Prerequisite*

- you have a working webcam plugged into your PC
- you have installed **OpenCV2** and **OpenCV2** python bindings. Please refer to `OpenCV documentation <http://opencv.org/>`_ to proceed, or check :ref:`faq` chapter.

On Debian-like platform, **OpenCV2** comes pre-installed, you just need to run

.. parsed-literal::

   $ sudo apt-get install python-opencv

Then copy this code snippet in a file and run it.

.. literalinclude:: stream_fromwebcam.py


.. parsed-literal::

  $ python yourcopiedfile.py

Check that your web cam video stream is correctly displayed on your screen.

.. image:: gwenn_onwebcam.png

You are setup to start using Angus.ai services:

- our plug and play audience analytics solution here (:ref:`audience-tuto`).
- one of our building blocks here (:ref:`buidling-blocks`).
