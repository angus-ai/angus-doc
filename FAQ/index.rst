.. angus.ai FAQ

.. _faq:

FAQ
===

|
|
|

Cameras / Images Requirements
-----------------------------

Do I need a specific camera?
++++++++++++++++++++++++++++

No, our solutions are made to work with any cameras (IP cam or USB webcam).
At Angus.ai, we use 50$ Logitech USB webcam on a daily basis, with no problem at all.

What are the supported image formats?
+++++++++++++++++++++++++++++++++++++

The supported formats are: JPEG and PNG.

What image resolution should I use?
+++++++++++++++++++++++++++++++++++

640x480 (aka VGA) images are a good start. Using bigger images will increase the ability of the system to detect faces that are further away from the camera, but will also lead to bigger latencies.

What frame rate should I use?
+++++++++++++++++++++++++++++

To ensure proper analysis from our services, make sure to provide about 10 frames per second.

|
|
|

Angus SDK, Python, OpenCV
-------------------------

What are the requirements to run Angus SDKs?
++++++++++++++++++++++++++++++++++++++++++++

Nothing, the SDKs come with their dependencies (managed by pip).
But, in order to access your webcam stream, you will need a dependency that is not
packaged into our SDK. We tend to use OpenCV a lot to do this (see other questions below).

Is Python SDK Python 3 compatible?
++++++++++++++++++++++++++++++++++

Yes, it is. The documentation code snippets and OpenCV3 are also Python 3.
In case you find any bug regarding compatibility, please contact us at support@angus.ai

How to install OpenCV3 and its Python bindings on major systems (Linux, MacOS, Windows)?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Please, use:

.. code-block:: none

   $ pip install opencv-python

Note that those are unofficial Python bindings. In order to have the
complete version of OpenCV3 please follow the official documentation
`here <http://opencv.org/>`_.

How to install OpenCV3 for other languages?
+++++++++++++++++++++++++++++++++++++++++++

Please follow official documentation `here <http://opencv.org/>`_.
For windows, check the complete guide on this FAQ.

|
|
|

Windows related questions
-------------------------

How can I install Pip in Windows?
+++++++++++++++++++++++++++++++++

Pip is installed by default when you install Python ``2.7.x``, please use the latest Python 2.x version available
or the latest Python 3.x version ``3.6.4``

How can I run all python code snippets on Windows?
++++++++++++++++++++++++++++++++++++++++++++++++++

Please use the latest Python 2.x version (with pip) ``2.7.14`` or the latest Python 3.x version ``3.6.4``
Windows installer puts Python in ``C:\Python27`` (for Python 2) by default, if you choose another directory,
please replace "C:\Python27" by your chosen directory in the following instructions:

In a Command Prompt go to python ``\Scripts`` directory:

.. code-block:: none

   $ cd C:\Python27\Scripts

Install numpy and Angus Python SDK:

.. code-block:: none

   $ pip install numpy angus-sdk-python opencv-python

Configure Angus SDK:

.. code-block:: none

   $ cd C:\Python27
   $ python Scripts\angusme

To install OpenCV, download OpenCV for Windows from http://opencv.org/, execute (or unzip) it.
Copy ``<opencv_directory>\buid\python\2.7\[x86|x64]\cv2.pyd`` in ``C:\Python27\Lib``.

Now you can run all Python snippets of the documentation.


Message "Input does not appear to be valid...." on Windows?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Make sure you use the binary file mode when opening images:

.. code-block:: python

   open("/path/to/your/image.png", "rb")
