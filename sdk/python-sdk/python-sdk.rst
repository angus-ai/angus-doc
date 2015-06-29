Python SDK
==========

Quick links
+++++++++++

 * Download last version: `0.0.5 <https://github.com/angus-ai/angus-sdk-python/archive/0.0.5.tar.gz>`_
 * `Source <https://github.com/angus-ai/angus-sdk-python>`_

Hello World
+++++++++++

.. code-block:: python

    > import angus
    > conn = angus.connect()
    > dummy_service = conn.services.get_service('dummy', version=1)
    > job = dummy_service.process({'echo': 'Hello world!'})
    > print(job.result)
    {
      "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca", 
      "status": 201, 
      "echo": "Hello world!"
    }


Installation
++++++++++++

Angus-sdk is listed in PyPI and can be installed with pip or easy_install.

.. parsed-literal::

   $ pip install angus-sdk-python

Documentation
+++++++++++++

.. toctree::
   :maxdepth: 2

   guide
   rest
   cloud

