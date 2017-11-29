.. _audience-tuto:

Tutorial
========

This documentation is meant at developers wanting to install, configure and launch Angus.ai audience analytics application on a personal computer.

What data can be retrieved
--------------------------

Angus.ai anonymous audience analytics solution computes (from each video stream) the following metrics:

- The number of people passing by the camera/device,
- The number of people interested in the camera/device
- The time spent stopped in front of the camera/device
- The time spent looking at the camera/device
- The number of people interested by the camera/device, broken down by
  demographics

  - Age
  - Gender
  - Emotion

For more information about the metrics, see the page dedicated to :ref:`the metrics <metrics>`.

How it works
------------

Angus.ai audience analytics solution is based on a (lightweight) Client / Server architecture as seen on the figure below.
All CPU expensive computation are made on our dedicated servers making it possible to run the solution from about any CPU board that can retrieve a camera stream and connect to a server (eg. Raspberry).

.. image:: archi.jpeg

Once properly installed and configured, this application will interact with Angus.ai cloud based algorithms to provide audience metrics that can be retrieve through a REST API.
This tutorial will show how to do it.

Requirements
------------

As you go through this tutorial, you will need:

- a computer. Every operating system is ok provided that you can configure a Python or Java stack.
- a camera (e.g. webcam) plugged into that computer. USB and IP cameras are supported, although IP cam can be more challenging to interface. If you need help doing so please contact us at support@angus.ai.
- a working internet connection. An upload bandwidth of about 400ko/sec is advised. If this is a problem, we are able to provide an "hybrid" version of our solution, where part of the CPU expensive computation is done locally, alleviating connection bandwidth requirements. Please contact us at support@angus.ai.

Step by step instructions
-------------------------

We have done our best to help you through these steps.
If you encounter any issues, please contact us at support@angus.ai, or just chat with us by clicking on the smiling face icon at the bottom right hand corner of this page.

+------+---------------------------------------+----------------------------+
|Steps                                         |Links                       |
+------+---------------------------------------+----------------------------+
|1     | Create an account                     |:ref:`create-account`       |
+------+---------------------------------------+----------------------------+
|2     | Get credentials for your camera       |:ref:`create-stream`        |
+------+---------------------------------------+----------------------------+
|3     | Download and configure the SDK        |:ref:`sdk`                  |
+------+---------------------------------------+----------------------------+
|4     | Download and launch the               |:ref:`apps`                 |
|      | client application                    |                            |
+------+---------------------------------------+----------------------------+
|5     | Check that metrics are correctly      |:ref:`dashboard`            |
|      | collected server side                 |                            |
+------+---------------------------------------+----------------------------+
|6     | Retrieve programmatically your metrics|:ref:`data-api`             |
+------+---------------------------------------+----------------------------+

What next?
----------

You have a running installation of Angus.ai audience analytics solution. Congratulations!

- When time comes, you can plug more cameras by creating additional stream as shown here (:ref:`create-stream`).
- If you need to deploy your system in a situation where internet bandwidth is a problem, please contact us at support@angus.ai.

For any issues please contact Angus.ai team at: support@angus.ai, and if possible,
please specify your operating system, python or java version, as well as the error backtrace if any. Thanks!
