Python SDK
==========

Installation
++++++++++++

.. parsed-literal::

   $ pip install angus-sdk-python

Initialisation
++++++++++++++

For simplicity, python angus sdk comes with a script name ``angusme`` that
enables store credentials in developer environment.

.. parsed-literal::

    $ angusme
    Please copy/paste your client_id: 7f5933d2-cd7c-11e4-9fe6-490467a5e114
    Please copy/paste your access_token: db19c01e-18e5-4fc2-8b81-7b3d1f44533b

Get service
+++++++++++

If you init your environment with ``angusme``, you can just call ``connect``
to get a root resource on Angus.ai cloud.

.. code-block:: python

    > import angus
    > conn = angus.connect()
    > dummy_service = conn.services.get_service('dummy', version=1)
   
Version parameter is optional, if not defined, sdk get the last version.

Composite services
++++++++++++++++++

SDK comes with a "composite" service helper to enable request many service at
the same time with the same interface of a single service

To get the dummy service AND the face detection service, both in the first
version:

.. code-block:: python

    > services = conn.services.get_services([('dummy', 1), ('face_detection', 1)])
    
Version can be omitted for the last version:

.. code-block:: python

    > services = conn.services.get_services(['dummy', 'face_detection'])
    
And if you want ALL services available on the Angus.ai cloud:

.. code-block:: python

    > services = conn.services.get_services()

Call service (create a job)
+++++++++++++++++++++++++++

Even if cloud API are asynchronous by default, the SDK work synchronously for
simplicity.

.. code-block:: python

    > job = dummy_service.process({'echo': 'Hello world!'})
    > print(job.result)
    {
      "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca", 
      "status": 201, 
      "echo": "Hello world!"
    }

Session for statefull services
++++++++++++++++++++++++++++++

If you use a statefull service you must enable session before create jobs
(use ``process``).

.. code-block:: python

    > dummy_service.enable_session()
    > dummy_service.process({'echo': 'Hello '})
    > job = dummy_service.process({'echo': 'world !'})
    > dummy_service.disable_session()
    > print(job.result)
    {
      "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca", 
      "status": 201, 
      "echo": "Hello world!"
    }
