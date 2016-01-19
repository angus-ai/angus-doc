Dummy
=====

Is my configuration correct ? I want to make my first call to angus.ai cloud.

Getting Started
---------------

Using Angus python SDK:

.. literalinclude:: dummy.py


Input
-----

The API takes a optional string as parameter and return a result
equals to these string.

The function ``process()`` takes a dictionary as input formatted as follows:

.. code-block:: javascript

    {'echo' : 'Hello world!'}

* ``echo``: a python string or unicode object.

Output
------

The service just return the input parameter if defined or the string
``"echo"`` if no parameter.

.. code-block:: javascript

    {'echo': 'Hello world!'}


* ``echo`` : the copy of the input string or ``"echo"`` if no defined.
