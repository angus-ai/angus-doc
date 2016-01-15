RESTful API Reference
=====================


.. |client_id| replace:: 7f5933d2-cd7c-11e4-9fe6-490467a5e114
.. |access_token| replace:: db19c01e-18e5-4fc2-8b81-7b3d1f44533b

Introduction and RESTful architecture
-------------------------------------

Angus.ai provides a RESTful API for its services. That implies:

* Use of HTTP protocol
* A standard protocol for encryption: ssl (HTTPs)
* A resource oriented programmation style
* A common resource representation: JSON
* A linked resources approach

In the rest of this documentation, we will use command line curl to
interact with Angus.ai gateway and present you each of these features
one by one.

Encryption and Authentication
-----------------------------

All requests to an angus.ai gateway must be done through `Basic
Authentication <https://en.wikipedia.org/wiki/Basic_access_authentication>`_
and https protocol (http over ssl).
You must signup at http://www.angus.ai/developers/ to get your credentials

These credentials are the equivalent of login/password but is for a device.
For example, for your first requests, you can use the free access:

* client id: |client_id|
* access token: |access_token|

To check your credentials you can make a simple **GET** request on
service list resource https://gate.angus.ai/services (we will see the
content of this resource in `Service directory`_). Curl accepts the
option ``-u`` that computes the value for the ``Authorization`` HTTP
header in order to conform to Basic Authentication protocol.

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
   > -s -o /dev/null -w "%{http_code}" \
   > https://gate.angus.ai/services
   200

You just made your first call to Angus.ai cloud and got the
response code ``200``. All communications was encrypted (because we
use https protocol) and you are authenticated thanks to your credentials.

Resources
---------

Angus.ai provides a "resource oriented" API. Each asset is represented as a
resource with at least one URL. Currently, most of Angus.ai resources
have only a JSON representation,
that means when you get a resource (with **GET**) from Angus.ai,
you can only specify the value ``application/json`` for the HTTP header ``Accept``.
The response body is a JSON object.

With the last resource (service list), we can display the response
content by removing extra options from curl command line:

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
   > https://gate.angus.ai/services
   {
      "services": {
         "dummy": {
            "url": "/services/dummy"
         },

	 (...)
	 
         "face_detection": {
            "url": "/services/face_detection"}
         }
    }

The response is a `JSON <https://en.wikipedia.org/wiki/JSON>`_ object,
the content is not important right now, we will describe it in the next
section.


Service directory
-----------------

Angus.ai cloud chooses follow the `HATEOAS
<https://en.wikipedia.org/wiki/HATEOAS>`_ constraint by linking
resources and not provide an a priori description of all resources
with their URLs.

But you must have an entry point to start the navigation. The entry
point for services is https://gate.angus.ai/services, this resource
describes a service directory. By requesting it, you get back a list
of available services provide by the targeted cloud.

.. code-block:: console
   
   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
   > https://gate.angus.ai/services
   {
     "services": {
         "face_expression_estimation": {
            "url": "/services/face_expression_estimation"
         },
         "dummy": {
            "url": "/services/dummy"
         },
         "gaze_analysis": {
            "url": "/services/gaze_analysis"
         },
         "motion_detection": {
            "url": "/services/motion_detection"
         },
         "age_and_gender_estimation": {
            "url": "/services/age_and_gender_estimation"
         },
         "sound_localization": {
            "url": "/services/sound_localization"
         },
         "face_detection": {
            "url": "/services/face_detection"
         }
      }
    }

Thanks to this request you discover the service ``dummy``. As all other asset
of the cloud, a service is a resource, let's get it:

.. code-block:: console
   
   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
   > https://gate.angus.ai/services/dummy
   {
      "versions": {
         "1": {"url": "/services/dummy/1"}
      }
   }

This response informs us that there are only one version. Let's continue and get it:

.. code-block:: console
  
   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
   > https://gate.angus.ai/services/dummy/1
   {
      "url": "https://gate.angus.ai/sevices/dummy/1",
      "version": 1,
      "description": "A simple echo service",
      "jobs": "https://gate.angus.ai/services/dummy/1/jobs",
   }

We start at the entry endpoint of service directory and finaly get
an endpoint on a "jobs" resource. 
In the next section we will see how to use this resource to request
new compute to the Angus.ai cloud.

Jobs (compute)
--------------

Job is a specific resource, it enables calling some service in a
RESTful way.
The previous "jobs" resource is a collection of job resources, then you
can create a new job just by using a **POST** operation on the
collection resource.
To make a valid request you must conform to some constraints:

* the body of the request must be a JSON message conform to the
  documentation of the service
* you must specify the Content-Type header of the request to
  application/json
* you must specify the type of creation: synchronous or asynchronous
  style. Please see `Asynchronous call`_ for more details

With curl the new command is as follow.

.. code-block:: console
		
   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
   > -H "Content-Type: application/json" \
   > -d '{ "echo": "Hello world!", "async": false}' \
   > https://gate.angus.ai/services/dummy/1/jobs
   {
      "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca",
      "status": 201,
      "echo": "Hello world!"
   }

The response contains an absolute url on the resource (the job), the status,
here 201 (**CREATED**), because a synchronous call was requested.

You can get back the resource with the new replied url.

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
   > https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca
   {
      "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca",
      "status": 201,
      "echo": "Hello world!"
   }

Asynchronous call
-----------------

All job requests are asynchronous by default if no ``async`` parameter is
define.

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
   > -H "Content-Type: application/json" \
   > -d '{ "echo": "Hello world!"}' \
   > https://gate.angus.ai/services/dummy/1/jobs
   {
      "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca",
      "status": 202,
   }

The response status is ``202`` for HTTP status code **ACCEPTED**, and the
replied url allows to get back the result in future. 

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
   > https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca
   {
      "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca",
      "status": 200,
      "echo": "Hello world!"
   }

If you want a synchronous job with the result, you must specify ``async`` as
``false``.

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
   > -H "Content-Type: application/json" \
   > -d '{ "echo": "Hello world!", "async": false}' \
   > https://gate.angus.ai/services/dummy/1/jobs
   {
      "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca",
      "status": 201,
      "echo": "Hello world!"
   }


Binary attachment
-----------------

With Angus.ai, you will want to send binary files for sound, images,
videos or other raw data from sensors. Angus.ai provide two ways to
upload them:

* attached in the request
* by creating a new resource


Make a request with an attached binary file
+++++++++++++++++++++++++++++++++++++++++++

You must create a multipart request to send binary file to the
cloud:

* the name of the binary part must follow the pattern ``attchment://<name_of_the_resource>``
* the name of the JSON body part must be ``meta``
* use the name ``attchment://<name_of_the_resource`` in JSON body part to refer to the resource

For example, the service face_detection requests an
image. You can upload it as atachment to the request as follow:
		   
.. code-block:: console
		
   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b  \
   > -F "attachment://bar=@macgyver.jpg;type=image/jpg" \
   > -F 'meta={"async" : false, "image": "attachment://bar"};type=application/json' \
   > https://gate.angus.ai/services/face_detection/1/jobs
   {
      "url": "https://gate.angus.ai/services/face_detection/1/jobs/1944556c-baf8-11e5-85c3-0242ac110001", 
      "status": 201, 
      "input_size": [480, 640], 
      "nb_faces": 1, 
      "faces": [{"roi": [262, 76, 127, 127], "roi_confidence": 0.8440000414848328}]
   }

 
Create a binary resource
++++++++++++++++++++++++

Angus.ai provides a blob storage to upload once and use it in many
services. This service is available at
https://gate.angus.ai/blobs. You must send binaries as previously, by
attaching it to the request. Blob storage request a message with a
``content`` parameter linked with the uploaded file.

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
   > -F "attachment://bar=@macgyver.jpg;type=image/jpg" \
   > -F 'meta={"async": false, "content": "attachment://bar"};type=application/json' \
   > https://gate.angus.ai/blobs
   {
      "status": 201, 
      "url": "https://gate.angus.ai/blobs/a5bca2da-baf6-11e5-ad97-0242ac110001"
   }

The response contains the url of the new blob resource. You can use it
in all service in your request message for new job:

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
   > -F 'meta={"async": false, "image": "https://gate.angus.ai/blobs/a5bca2da-baf6-11e5-ad97-0242ac110001"};type=application/json' \
   > https://gate.angus.ai/services/face_detection/1/jobs
   {
      "url": "http://localhost/services/face_detection/1/jobs/1944556c-baf8-11e5-85c3-0242ac110001", 
      "status": 201, 
      "input_size": [480, 640], 
      "nb_faces": 1, 
      "faces": [{"roi": [262, 76, 127, 127], "roi_confidence": 0.8440000414848328}]
   }

Session / State
---------------

Even if Angus.ai API is RESTful and then the services aim to be stateless,
some service are statefull for them first version.
Anyway, the state must be keep by the client and attach with each request in a
``state`` JSON parameter. For the statefull services, then states are just a
session_id in the format **uuid1** generated client side.

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
   > -H "Content-Type: application/json" \
   > -d '{ "echo": "Hello world!", "async": false}' \
   > https://gate.angus.ai/services/dummy/1/jobs
   {
      "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca",
      "state" {
         "session_id": "714f0416-0de0-11e5-ab02-eca86bfe9d03"
      },
      "status": 201,
      "echo": "Hello world!"
   }
