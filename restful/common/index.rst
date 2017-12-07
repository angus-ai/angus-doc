.. _http-api:

Main API Reference
==================


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
interact with angus.ai gateway and present each of these features, one by one.

Encryption and Authentication
-----------------------------

All requests to an angus.ai gateway needs to be done through `Basic
Authentication <https://en.wikipedia.org/wiki/Basic_access_authentication>`_
and https protocol (http over ssl).

As a user, you need to signup first at https://console.angus.ai/register to get your credentials.

These credentials are an equivalent of a login/password but for a device.

If you do not have your credentials yet, you can use the following ones for this tutorial:

* client id: |client_id|
* access token: |access_token|

To check your credentials you can make a simple **GET** request on
service list resource https://gate.angus.ai/services (we will see the
content of this resource in `Service directory`_). Curl accepts the
option ``-u`` that computes the value for the ``Authorization`` HTTP
header in order to conform to Basic Authentication protocol.

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
     -s -o /dev/null -w "%{http_code}" \
     https://gate.angus.ai/services

   > 200

You just made your first call to angus.ai and got the
response code ``200``. All communications were encrypted (because we
use https protocol) and you were authenticated thanks to your credentials.

Resources
---------

Angus.ai provides a "resource oriented" API. Each image, piece of
sound, document and other assets are represented as a
resource with at least one URL. Currently, most angus.ai resources
only have a JSON representation.

This means that when you get a resource (with **GET**) from angus.ai,
only the value ``application/json`` is available for the HTTP header ``Accept``.
The response body will be a JSON object.

You can have a look at the body of a response by, for example, using the previous curl command
and removing the extra options:

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
     https://gate.angus.ai/services

   > {
        "services": {
           "dummy": {
              "url": "/services/dummy"
           },

          (...)

           "face_detection": {
              "url": "/services/face_detection"}
           }
      }

This response body is a `JSON <https://en.wikipedia.org/wiki/JSON>`_ object,
its content is not important right now, we will describe it in the next
sections.


Service directory
-----------------

We chose to follow the `HATEOAS
<https://en.wikipedia.org/wiki/HATEOAS>`_ constraints by linking
resources via URLs provided dynamically instead of providing an a priori description of all resources
with their URLs.

But you must have an entry point to start the navigation. The entry
point for angus.ai services is https://gate.angus.ai/services. This resource
describes a service directory. By requesting it, you get back a list
of available services provided by angus.ai.

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
     https://gate.angus.ai/services

   > {
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

This request reveals for example a service named ``dummy``.
A service is a resource too, so let's ``get`` it:

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
     https://gate.angus.ai/services/dummy

   > {
        "versions": {
           "1": {"url": "/services/dummy/1"}
        }
     }

The response shows that there is only one version of the dummy service. Let's continue and ``get`` the new given url:

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
     https://gate.angus.ai/services/dummy/1

   > {
        "url": "https://gate.angus.ai/services/dummy/1",
        "version": 1,
        "description": "\nA simple dummy service. You can send {\"echo\": \"Hello world\"} to get back the\nmessage \"Hello world\" as result. Moreover, the dummy service enables statefull\nfeatures",
        "jobs": "https://gate.angus.ai/services/dummy/1/jobs",
     }

We started at the entry endpoint of service directory and finaly got
an endpoint on a "jobs" resource.

In the next section we will see how to use this resource to request
new compute to angus.ai.

Jobs (compute)
--------------

The previous "jobs" resource is a collection of job resources.

As a user, you can create a new job by using a **POST** request on it.

To make a valid request you must comply with these constraints:

* the body of the request must be a JSON message whose format matches the
  documentation of the service
* the ``Content-Type`` header of the request must be set to ``application/json``
* you must specify the synchronous or asynchronous type of request you wish to make. Please see `Asynchronous call`_ for more details

The new curl command is as follows:

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
     -H "Content-Type: application/json" \
     -d '{ "echo": "Hello world!", "async": false}' \
     https://gate.angus.ai/services/dummy/1/jobs

   > {
       "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca",
       "status": 201,
       "echo": "Hello world!"
     }

The response contains an absolute url on the resource (the job), its status (201 : **CREATED**),
and its result as a synchronous job has been requested.

Note that an new url is provided to get back later on the job (accessing its result in an async way for example).

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
     https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca

   > {
        "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca",
        "status": 201,
        "echo": "Hello world!"
     }

Asynchronous call
-----------------

All job requests are asynchronous by default if no ``async`` parameter is
set.

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
     -H "Content-Type: application/json" \
     -d '{ "echo": "Hello world!"}' \
     https://gate.angus.ai/services/dummy/1/jobs

   > {
        "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca",
        "status": 202,
     }

The response status is ``202`` for HTTP status code **ACCEPTED**, and the
replied url allows to get back to the result in the future.

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
     https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca

   > {
        "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca",
        "status": 200,
        "echo": "Hello world!"
     }

If you want a synchronous job with the result, you must specify ``async`` as
``false``.

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
     -H "Content-Type: application/json" \
     -d '{ "echo": "Hello world!", "async": false}' \
     https://gate.angus.ai/services/dummy/1/jobs

   > {
        "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca",
        "status": 201,
        "echo": "Hello world!"
     }


Binary attachment
-----------------

Most requesta to angus.ai will need you to attach binary files for sound, images,
videos or other raw data from various sensors. Angus.ai provides two ways to
upload them:

* attached in the request
* or by referring to a previously created resource


Make a request with an attached binary file
+++++++++++++++++++++++++++++++++++++++++++

You need to create a multipart request to send binary file to angus.ai as follows:

* the name and type of the binary part are specified with: ``attachment://<name_of_the_resource>``
* the JSON body part is prefixed with ``meta``
* the JSON body part refers to the attachement ``attachment://<name_of_the_resource``

For example, the service ``face_detection`` must be provided an
image as input. You can upload it as an attachment as follows:

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b  \
     -F "attachment://bar=@macgyver.jpg;type=image/jpg" \
     -F 'meta={"async" : false, "image": "attachment://bar"};type=application/json' \
     https://gate.angus.ai/services/face_detection/1/jobs

   > {
        "url": "https://gate.angus.ai/services/face_detection/1/jobs/1944556c-baf8-11e5-85c3-0242ac110001",
        "status": 201,
        "input_size": [480, 640],
        "nb_faces": 1,
        "faces": [{"roi": [262, 76, 127, 127], "roi_confidence": 0.8440000414848328}]
     }


Create a binary resource
++++++++++++++++++++++++

Angus.ai provides a "blob storage" to upload a binary resource once and use it later for one or more
services. This service is available at https://gate.angus.ai/blobs.

Binaries need to be sent as an attachement to the request (as shown above), made on the "blob storage" resource.
The JSON body part needs to contain a key ``content`` whose value matches the attached file.

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
     -F "attachment://bar=@macgyver.jpg;type=image/jpg" \
     -F 'meta={"async": false, "content": "attachment://bar"};type=application/json' \
     https://gate.angus.ai/blobs

   > {
        "status": 201,
        "url": "https://gate.angus.ai/blobs/a5bca2da-baf6-11e5-ad97-0242ac110001"
     }

The response contains the url of the new blob resource created.
You can now use this (binary) resource it in all angus.ai services by referring to it in your requests:

.. code-block:: console

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
     -F 'meta={"async": false, "image": "https://gate.angus.ai/blobs/a5bca2da-baf6-11e5-ad97-0242ac110001"};type=application/json' \
     https://gate.angus.ai/services/face_detection/1/jobs

   > {
        "url": "http://localhost/services/face_detection/1/jobs/1944556c-baf8-11e5-85c3-0242ac110001",
        "status": 201,
        "input_size": [480, 640],
        "nb_faces": 1,
        "faces": [{"roi": [262, 76, 127, 127], "roi_confidence": 0.8440000414848328}]
     }

Session / State
---------------

Despite angus.ai API aiming at RESTful and hence stateless services,
some services can currently and optionally be made statefull.

In that case, the state is kept by the client and attached with each request in a
``state`` JSON parameter. For the statefull services, states are currently represented as
``session_id`` generated on the client side.

In followed example, we generate a uuid session id with the ``uuidgen``
linux tool and we loop 4 times over the same image that contains a
face and send it to the face detection service.

.. code-block:: console

   > export SESSION=`uuidgen`
   > for i in `seq 1 4`; do
   >   curl -su 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
   >        -F "attachment://bar=@macgyver.jpg;type=image/jpg" \
   >        -F 'meta={"async" : false, "image": "attachment://bar", "state": { "session_id": "'$SESSION'"}};type=application/json' \
   >        https://gate.angus.ai/services/face_detection/1/jobs | python -m json.tool | grep "nb_faces"
   > done;
       "nb_faces": 0,
       "nb_faces": 0,
       "nb_faces": 0,
       "nb_faces": 1,

When a session is
requested, the service try to track faces in sucessive images but
returns no result at first time. Then, we can notice, the three first
calls have 0 face result but the fourth one (for the same image) find
a face. That validates the session id parameter is taken into account.
