.. angus.ai FAQ

.. _faq:
   
FAQ
===

What do I need to use Angus SDKs ?
++++++++++++++++++++++++++++++++++

Nothing, the SDKs come with their dependencies (managed by pip for python, or embeded for java).
But, in order to run more advanced examples, you would install OpenCV,
or PyAudio for example (see relative questions for help).

Is Python SDK Python 3 compatible ?
+++++++++++++++++++++++++++++++++++

Yes, it is. But the documentation code snippets and OpenCV2 are only Python 2.
Sorry for the inconvenience, the Python 3 documentation would arrive soon.

How install OpenCV2 and python bindings on debian-like systems ?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Please, use:

.. code-block:: none
   
   $ apt-get install python-opencv

How install OpenCV2 on other systems ?
++++++++++++++++++++++++++++++++++++++

Please follow official documentation `here <http://opencv.org/>`_.
For windows, check the complete guide on this FAQ.

What are the supported image formats ?
++++++++++++++++++++++++++++++++++++++

The supported formats are: JPEG and PNG.

What is the best resolution for Angus.ai services ?
+++++++++++++++++++++++++++++++++++++++++++++++++++

Many services use only 640x480 images. You can send bigger images but without improvements.

What is the best frame rate for Angus.ai services ?
+++++++++++++++++++++++++++++++++++++++++++++++++++

The target fps for realtime analytics of your video would be 10fps.

How can I install Pip in Windows ?
++++++++++++++++++++++++++++++++++

Pip is installed by default with python ``2.7.12``, please use the last python version.

How can I run all python code snippets on windows ?
+++++++++++++++++++++++++++++++++++++++++++++++++++

Please use last python 2 version (with pip) ``2.7.12``.
Windows installer put python in ``C:\Python27`` by default, if you choose an other directory,
please replace it in the following instructions.

In a Command Prompt go to python ``\Scripts`` directory:

.. code-block:: none
   
   $ cd C:\Python27\Scripts

Install numpy and angus python sdk:

.. code-block:: none

   $ pip install numpy angus-sdk-python

Configure angus:

.. code-block:: none
		
   $ cd C:\Python27
   $ python Scripts\angusme

To install opencv, download opencv for windows from http://opencv.org/, execute (or unzip) it.   
Copy ``<opencv_directory>\buid\python\2.7\[x86|x64]\cv2.pyd`` in ``C:\Python27\Lib``.

Now you can run all python snippets of the documentation.


