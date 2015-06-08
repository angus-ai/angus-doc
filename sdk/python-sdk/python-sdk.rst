Python SDK
==========

Installation
++++++++++++

.. parsed-literal::

   $ pip install angus-sdk-python

Authentication
++++++++++++++

The angus.ai python sdk comes with a script called ``angusme`` that is used to authenticate 
the http requests sent to angus.ai server from a specific device.

.. parsed-literal::

    $ angusme
    Please copy/paste your client_id: 7f5933d2-cd7c-11e4-9fe6-490467a5e114
    Please copy/paste your access_token: db19c01e-18e5-4fc2-8b81-7b3d1f44533b

Use your first angus.ai service
+++++++++++++++++++++++++++++++

With your environment correctly setup using the script ``angusme`` as described above, 
you can now call your first service. 

.. code-block:: python

    > import angus
    > conn = angus.connect()
    > dummy_service = conn.services.get_service('dummy', version=1)
   
Version parameter is optional, if not defined, sdk get the last version.


Composite services
++++++++++++++++++

The SDK allows to call multiple services at the same time:

For example, to call the motion detection AND the face detection services at the same time, using version 1 for both:

.. code-block:: python

    > services = conn.services.get_services([('motion_detection', 1), ('face_detection', 1)])
    
If version is omitted, last stable version of the service is used:

.. code-block:: python

    > services = conn.services.get_services(['motion_detection', 'face_detection'])
    
And if you want ALL services available on the Angus.ai to be called on the given input:

.. code-block:: python

    > services = conn.services.get_services()

Create a job on a service
+++++++++++++++++++++++++

Even if our API are asynchronous by default, the SDK work synchronously for
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

Most angus.ai can be either use in a stateless (every given inputs are processed independently) or in a stateful way (previous calls are remembered and use to improve the accuracy of the output).

By default all API behave in a stateless manner. To enable the stateful behavior, you need to call ``enable_session()`` before calling ``process``.

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
