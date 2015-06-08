.. angus.ai documentation master file, created by
   sphinx-quickstart on Fri Apr  3 10:50:35 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Angus.ai documentation (Beta)
=============================

.. |client_id| replace:: 7f5933d2-cd7c-11e4-9fe6-490467a5e114
.. |access_token| replace:: db19c01e-18e5-4fc2-8b81-7b3d1f44533b

Cloud API
+++++++++

General
-------

Angus.ai provides a "resource oriented" API, each asset is represented as a
resource. It enables a good RESTful architecture.
Resources provide a JSON representation. The minimal field are:

.. code-block:: javascript

   {
      "url": "https://gate.angus.ai/path_to_my_resource"
   }

The url must be absolute and provides a way to recover the resource in the
future with **GET** operation. Other operations (**POST**, **DELETE** or **PUT**)
are available depends of resource type.

Authentication
--------------
All APIs must be access through basic authentication. You must get back your
credentials here: http://www.angus.ai/developers/.
If your credentials are ``7f5933d2-cd7c-11e4-9fe6-490467a5e114`` and
``db19c01e-18e5-4fc2-8b81-7b3d1f44533b``, the list of services
provided by the Angus.ai cloud are available at https://gate.angus.ai/services
like this:

.. parsed-literal::

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b https://gate.angus.ai/services
   {
      "url": "https://gate.angus.ai/services",
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
            "url": "/services/face_detection"}
         }
    }

This resource is a collection. A collection is a set of sub-resources.
Collections could enable **POST** operations to create a new sub-resources,
and **GET** to list the content. In this case (services) the collection are
immutable, then **POST** operation return 405 error code (Method not allowed).

Services is an other specific resources, it contains 2 sub-resources, a description
and a collections of jobs.
For example, the service ``dummy`` can be access through
https://gate.angus.ai/services/dummy/1 for version 1.
Then, two resources are immediatly available:
 * https://gate.angus.ai/services/dummy/1/description
 * https://gate.angus.ai/services/dummy/1/jobs.

.. parsed-literal::

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b https://gate.angus.ai/services/dummy/1/description


Job is a specific resource, it enables calling some service in a RESTful way.
To create a job just use a **POST** operation on jobs collection, the json body
of the input message is specific for each service. For ``dummy`` service, we
specify a ``echo`` parameter,
and request a synchronous job (see `Asynchronous call`_).

.. parsed-literal::

   > curl -H "Content-Type: application/json" -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b -d '{ "echo": "Hello world!", "async": false}' https://gate.angus.ai/services/dummy/1/jobs
   {
      "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca", 
      "status": 201, 
      "echo": "Hello world!"
   }
 
The response contains an absolute url on the resource, the status,
here 201 (**CREATED**), because a synchronous call was requested, and the
``echo`` variable documented in dummy service documentation.

Binary attachment
-----------------

Attachment and resources

Asynchronous call
-----------------

All job requests are asynchronous by default if no ``async`` parameter is
define.

.. parsed-literal:: 

   > curl -H "Content-Type: application/json" -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b -d '{ "echo": "Hello world!"}' https://gate.angus.ai/services/dummy/1/jobs 
   { 
      "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca",
      "status": 202, 
   }

The response status is 202 for HTTP statuc code **CREATED**, and the
reply url enables get back the result in future.

.. parsed-literal:: 

   > curl -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca 
   { 
      "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca",
      "status": 200,
      "echo": "Hello world!" 
   }

If you want a synchronous job with the result, you must specify ``async`` as
``false``.

.. parsed-literal:: 

   > curl -H "Content-Type: application/json" -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b -d '{ "echo": "Hello world!", "async": false}' https://gate.angus.ai/services/dummy/1/jobs 
   { 
      "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca",
      "status": 201, 
      "echo": "Hello world!" 
   }

Session / State
---------------

Even if Angus.ai API is RESTful and then the services aim to be stateless,
some service are statefull for them first version.
Anyway, the state must be keep by the client and attach with each request in a
``state`` json parameter. For the statefull services, then states are just a
session_id in the format **uuid1** generated client side.

.. parsed-literal:: 

   > curl -H "Content-Type: application/json" -u 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b -d '{ "echo": "Hello world!", "async": false}' https://gate.angus.ai/services/dummy/1/jobs 
   { 
      "url": "https://gate.angus.ai/services/dummy/1/jobs/db77e78e-0dd8-11e5-a743-19d95545b6ca",
      "state" {
         "session_id": "714f0416-0de0-11e5-ab02-eca86bfe9d03"
      },
      "status": 201, 
      "echo": "Hello world!"
   }


SDKs
++++

.. toctree::
   :maxdepth: 2

   python-sdk/python-sdk
   java-sdk/java-sdk


Services
++++++++

.. toctree::
   :maxdepth: 2

   motiondetection/motiondetection
   facedetection/facedetection
   agegenderestimation/agegenderestimation
   gazeanalysis/gazeanalysis
   faceexpressionestimation/faceexpressionestimation
   soundlocalization/soundlocalization

