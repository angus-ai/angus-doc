Optmisation
===========

Motion Detection
++++++++++++++++

The main goal of this optimisation is to send data to Angus.ai only if
there are movements in video stream.

To do this, we can use OpenCV to compute diff between two successive images.

.. literalinclude:: call_optimisation.py


