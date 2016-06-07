How to setup an Angus box (on premise)
**************************************

This tutorial will guide you through the process of installing and running your ``Angus box`` on your PC/Server.

The PC/Server where to install the ``Angus box`` should meet the following minimal requirements:

``pre-requisites``:
 * Processor: 1 Core (1Ghz), Architecture x86
 * RAM: 2GB
 * Hard disk space: 1GB (the footpring of the ``Angus box`` is actually ~750MB)
 * OS : Linux, 64bits

|
|

1. Install Docker
+++++++++++++++++

To deploy and run your ``Angus box``, you need to install Docker first.

The procedure depends on your Linux distribution, please refer to the appropriate section in the `Docker documentation <https://docs.docker.com/installation/>`_.

The procedure should look like this (Ubuntu 15.04LTS):

.. code-block:: python

   $ sudo apt-get update
   $ sudo apt-get install wget
   $ wget -qO- https://get.docker.com/ | sh

To check that ``Docker`` is correctly installed:

.. code-block:: python

   $ sudo docker run hello-world

|
|

2. Download your Angus Box
++++++++++++++++++++++++++

The Angus.ai team should have sent you a link to download your ``Angus box``.
If this is not the case, contact us at: contact@angus.ai

In this document the path to your downloaded ``Angus box`` will be refered to as  ``/path/to/angus.box.prod.tgz``.

|
|

3. Run your Angus Box
+++++++++++++++++++++

Load the box
------------

To load your ``Angus box``, type in a terminal (the commands below launch background executables, your terminal will stay active afterwards):

.. code-block:: python

   sudo docker load < /path/to/angus.box.prod.tgz

Start the box
-------------

.. code-block:: python

   ID = $(sudo docker run -d -p 0.0.0.0:80:80 -t angus.box:prod)

You can check that the image is running with ``sudo docker ps`` (listing the running Docker images).

Please note that the last command will have your ``Angus box`` listen to external requests received by the host PC on port 80.

If this configuration does not suit your needs,
please refer to the `Docker documentation <https://docs.docker.com/userguide/dockerlinks/>`_ to adapt the ``docker run`` command.

Stop the box
------------

The ``Angus box`` can be stopped at any time by typing:

.. code-block:: python

   sudo docker stop $ID


Unload the box
--------------

You can totally remove the ``Angus box`` from your system by typing:

.. code-block:: python

   sudo docker rmi angus.box:prod

You can check that the ``Angus box`` is not loaded anymore with ``sudo docker images`` (listing the loaded Docker images).

|
|

4. Test your Angus Box
++++++++++++++++++++++

Install the Angus SDK
---------------------

If you haven't done so, please install one of the Angus SDKs, and configure it as described `here <http://angus-doc.readthedocs.org/en/latest/getting-started/python.html>`_.

In most use cases, the SDK will be installed on a different device than the Angus box but for the purpose of testing your Angus box,
you can install the SDK on the same device.

If you had previously installed the SDK, make sure you get the last version:

.. code-block:: python

  $ pip install angus-sdk-python --upgrade

Configure the Angus SDK
-----------------------

By default, your SDK is configured to send its requests to the servers hosted by Angus.

To redirect these requests to your newly installed ``Angus box``, open the configuration file located at ``/home/<your_username>/.angusdk/config.json``, and replace ``https://gate.angus.ai`` by ``http://<Server IP>``.

The modified file should look like this:

.. include:: config.json
   :literal:

To check that the SDK is correctly configured, use the following command:

.. code-block:: python

   $ angusme -t

The result should look like:

.. code-block:: python

   $ Server: http://10.1.31.4
   $ Status: OK


Make sure that the server address matches the address of the PC where you installed the ``Angus box``.

Send a first request to your Angus box
--------------------------------------

You are now all set, and should be able to run the code sample provided `here <http://angus-doc.readthedocs.org/en/latest/getting-started/python.html#send-your-first-request>`_.

|
|

5. Troubleshooting
++++++++++++++++++

If you encounter any problem, do not hesitate to contact us immediately at contact@angus.ai
or +33 (0)6.01.73.01.85.
