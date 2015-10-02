Hello Yun
=========

This is a small tutorial about how to use Angus.ai on Arduino Yun. We
will plug a webcam and use face detection in order to print “Hello
you” when people are front of the device.

What is and why arduino Yun ?
-----------------------------

.. _Yun: https://www.arduino.cc/en/Guide/ArduinoYun

What is and why arduino Yun ?
Arduino Yun is the mixture between a CPU (Atheros AR9331) with an OS
(OpenWRT) and a microcontroller (Atmel ATmega32U4). It is a very
interresting platform for the Internet Of Thing projects because you
can control:
 * your electronic/real-time/analogic/thing parts with
   the microcontroller
 * and the communication wifi/ethernet/Internet/web parts with
   the atheros processor.
It's the best of both world ! All integrated in one board and
dedicated libraries.

Introduction
------------

The documentation https://www.arduino.cc/en/Guide/ArduinoYun is very
well done, then we invite you to follow the getting started before
coming back here to test angus.

After configuring the wifi (or ethernet) to put your Yun_ in you local
area network, you can login with ssh from you computer:

.. code-block:: bash

    > ssh root@arduino.local

The available disk storage (8MB) is very low, then you
must expand the disk to work without problem.

.. code-block:: bash

    > df -h
    Filesystem                Size      Used Available Use% Mounted on
    rootfs                    7.0M      3.2M      3.8M  46% /
    /dev/root                 7.5M      7.5M         0 100% /rom
    tmpfs                    29.8M    100.0K     29.7M   0% /tmp
    tmpfs                   512.0K         0    512.0K   0% /dev
    /dev/mtdblock3            7.0M      3.2M      3.8M  46% /overlay
    overlayfs:/overlay        7.0M      3.2M      3.8M  46% /

Please use these `instructions
<https://www.arduino.cc/en/Tutorial/ExpandingYunDiskSpace>`_ to do
that. After putting a new micro-sd card with partitions, it must look like
this:

.. code-block:: bash

    > df -h
    Filesystem                Size      Used Available Use% Mounted on
    rootfs                    7.0M      3.2M      3.8M  46% /
    /dev/root                 7.5M      7.5M         0 100% /rom
    tmpfs                    29.8M    100.0K     29.7M   0% /tmp
    tmpfs                   512.0K         0    512.0K   0% /dev
    /dev/mtdblock3            7.0M      3.2M      3.8M  46% /overlay
    overlayfs:/overlay        7.0M      3.2M      3.8M  46% /
    /dev/sda1                11.8G    384.9M     10.9G   3% /mnt/sda1

Installation
------------

Binary packages
+++++++++++++++

We now install required binary packages from the distribution:

.. code-block:: bash

    > opkg update
    > opkg install python-openssl
    > opkg install wget
    > opkg install tar
    > opkg install bzip2
    > opkg install kmod-video-uvc

SDK environment
+++++++++++++++

Virtualenv is not available as a distribution package, but there is no
problem, we will download it. Move into the mounted disk
(``/mnt/sda1``) and download the package from the python package index
`Pypi <https://pypi.python.org/pypi>`_. Here I download the
``13.1.2``, replace it by last version.


.. code-block:: bash

    > cd /mnt/sda1
    > wget --no-check-certificate https://pypi.python.org/packages/source/v/virtualenv/virtualenv-13.1.2.tar.gz
    > gzip virtualenv-13.1.2.tar.gz
    > tar xvf virtualenv-13.1.2.tar

You can use virtualenv immediately to create a development environment
and jump into it:

.. code-block:: bash

    > cd /mnt/sda1/virtualenv-13.1.2
    > ./virtualenv.py ../devenv
    > cd ..
    > source devenv/bin/activate

Then, you can easily install angus with its dependencies:

.. code-block:: bash

    > pip install angus-sdk-python

Webcam
++++++

We use a uvc compatible webcam. This tutorial was tested with the
`Logitech HD Pro Webcam C920
<http://www.logitech.com/en-hk/product/hd-pro-webcam-c920>`_. Just
plug it on the usb port.


The script
----------

In the getting started of Angus, we use opencv to grab images from the
camera. OpenCV is not available on the Yun_ distribution.
But you can take a picture with the tools ``fswebcam``. Thanks to
Stefano Guglielmetti with its "`You cant touch this
<https://github.com/amicojeko/YouCantTouchThis>`_" project for the
trick.

The minimalist script is now straightforward:

.. code-block:: python

    import angus
    import os
    import subprocess

    # Initialize the sdk
    conn = angus.connect()

    # Get back a reference on the service
    service = conn.services.get_service("face_detection")

    # Open /dev/null for fswebcam stdout and stderr redirection
    FNULL = open(os.devnull, 'w')

    # Just process 20 times
    for i in range(20):
        # Take a picture
        subprocess.call(["fswebcam", "image.png"], stdout=FNULL, stderr=FNULL)
        # Send request to angus
        job = service.process({"image": open("image.png", "rb")})

        if job.result["nb_faces"] > 0:
             print("Hello yun")
