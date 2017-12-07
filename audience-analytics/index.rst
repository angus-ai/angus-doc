.. _audience-tuto:

Audience Analytics
==================

Introduction
************

This documentation is meant at developers wanting to install, configure and launch Angus.ai audience analytics application on a personal computer.

What data can be retrieved
--------------------------

Angus.ai anonymous audience analytics solution computes (from each video stream) the following metrics:

- The number of people passing by the camera/device,
- The number of people interested in the camera/device
- The time spent stopped in front of the camera/device
- The time spent looking at the camera/device
- The number of people interested by the camera/device, broken down by
  demographics

  - Age
  - Gender
  - Emotion

For more information about the metrics, see the page dedicated to :ref:`the metrics <metrics>`.

How it works
------------

Angus.ai audience analytics solution is based on a (lightweight) Client / Server architecture as seen on the figure below.
All CPU expensive computation are made on our dedicated servers making it possible to run the solution from about any CPU board that can retrieve a camera stream and connect to a server (eg. Raspberry).

.. image:: archi.jpeg

Once properly installed and configured, this application will interact with Angus.ai cloud based algorithms to provide audience metrics that can be retrieve through a REST API.
This tutorial will show how to do it.

Requirements
------------

As you go through this tutorial, you will need:

- a computer. Every operating system is ok provided that you can configure a Python or Java stack.
- a camera (e.g. webcam) plugged into that computer. USB and IP cameras are supported, although IP cam can be more challenging to interface. If you need help doing so please contact us at support@angus.ai.
- a working internet connection. An upload bandwidth of about 400ko/sec is advised. If this is a problem, we are able to provide an "hybrid" version of our solution, where part of the CPU expensive computation is done locally, alleviating connection bandwidth requirements. Please contact us at support@angus.ai.

Configure your player
*********************

Create an account
-----------------

.. include:: ../console/create-account.rst
  :start-after: after-title

Get credentials for your camera
-------------------------------

.. include:: ../console/create-stream.rst
  :start-after: after-title


Download and configure the SDK
------------------------------

.. include:: ../restful/sdk/python.rst
  :start-after: after-title
  :end-before: stop-here


Download and launch the client application
------------------------------------------

.. include:: python-app.rst
  :start-after: after-title

Online Dashboard
****************

Check that metrics are correctly collected server side
------------------------------------------------------

.. include:: dashboard.rst
  :start-after: after-title

Retrieve your Data
******************

Here is a short section to help you get started in retrieving your audience data programmatically. Check our API reference for further details. (:ref:`data-api`)

Getting your JWT Token
++++++++++++++++++++++

You need a JSON Web Token ("JWT") token in order to securely call the data
api endpoint. Your personal JWT is provided by programmatically calling the
appropriate endpoint documented below.

Please use your angus.ai:

- Angus.ai login (email adress)
- Stream client_id
- Stream acccess_token

in the command below:

**Request:**

   .. code:: bash

     curl -X POST -H "Content-Type: application/json" -d '{"username": "aurelien.moreau@angus.ai", "client_id": "xxxxx-xxxx-xxxx-xxxx-xxxxxxxxx", "access_token": "xxxxx-xxxx-xxxx-xxxx-xxxxxxxxx"}' https://console.angus.ai/api-token-authstream/

You should get a response as shown below, if this is not the case, contact us.

**Response:**

   .. code:: json

     {
       "token": "eyJhbGciOiJIUzI2NiIsInR5dCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImF1cmVsaWVuLm1vcmVhdUBhbmd1cy5haSIsIm9yaWdfaWF0IjoxNTA1Mzk4MDM4LCJleHAiOjE1D8DU0MTYwMzgsImNsaWVudF9pZCI6IjNiZDk1ZjIwLWM2OWYtMTFlNS1hZWVjLTAyNDJhYzExMDAwMiIsInVzZXJfaWQiOjgyNiwiZW1haWwiOiJhdXJlbGllbi5tb3JlYXVAYW5ndXMuYWkifQ.K70YXQYMAcdeW7dfscFGxUhenoXXGBAQTiWhNv-9cVc"
     }


Once you obtained your personal JWT, you can start retrieving your data by calling the API endpoints documented in the :ref:`api-reference` page.

Example
+++++++

Here is an example of a request for all entities from 5:45 GMT+2, the 2017, September the 3rd until now, using a time bucket of “one day”.

*Request:*

  .. code:: bash

    curl -X GET -H 'Authorization: Bearer eyJhbGciOiJIUzI2NiIsInR5dCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImF1cmVsaWVuLm1vcmVhdUBhbmd1cy5haSIsIm9yaWdfaWFfta0IjoxNTA1Mzk4MDM4LCJleHAiOjE1MDU0MTYwMzgsImNsaWVudF9pZCI6IjNiZDk1ZjIwLWM2OWYtMTFlNS1hZWVjLTAyNDJhYzExMDAwMiIsInVzZXJfaWQiOjgyNiwiZW1haWwiOiJhdXJlbGllbi5tb3JlYXVAYW5ndXMuYWkifQ.K70YXQYMAcdeW7dfscFGxUhenoXXGBAQTiWhNv-9cVc' 'https://data.angus.ai/api/1/entities?metrics=satisfaction,gender,category,passing_by,interested&from_date=2017-09-03T05%3A45%3A00%2B0200&time=by_day

*Response:*

  .. code:: json

    {
        "entities": {
            "2017-09-03T00:00:00+00:00": {
                "category": {
                    "senior_female": 0,
                    "senior_male": 0,
                    "young_female": 0,
                    "young_male": 0
                },
                "gender": {
                    "?": 0,
                    "female": 0,
                    "male": 0
                },
                "interested": {
                    "value": 0
                },
                "passing_by": {
                    "value": 0
                },
            },
            "2017-09-04T00:00:00+00:00": {
                "category": {
                    "senior_female": 0,
                    "senior_male": 0,
                    "young_female": 0,
                    "young_male": 8
                },
                "gender": {
                    "?": 0,
                    "female": 0,
                    "male": 10
                },
                "interested": {
                    "value": 10
                },
                "passing_by": {
                    "value": 18
                },
            },
            "2017-09-05T00:00:00+00:00": {
                "category": {
                    "senior_female": 0,
                    "senior_male": 0,
                    "young_female": 4,
                    "young_male": 52
                },
                "gender": {
                    "?": 0,
                    "female": 4,
                    "male": 56
                },
                "interested": {
                    "value": 60
                },
                "passing_by": {
                    "value": 152
                },
            },
            "2017-09-06T00:00:00+00:00": {
                "category": {
                    "senior_female": 0,
                    "senior_male": 0,
                    "young_female": 0,
                    "young_male": 3
                },
                "gender": {
                    "?": 0,
                    "female": 0,
                    "male": 4
                },
                "interested": {
                    "value": 4
                },
                "passing_by": {
                    "value": 20
                },
            },
            …
            …
            ...
            "2017-09-13T00:00:00+00:00": {
                "category": {
                    "senior_female": 0,
                    "senior_male": 0,
                    "young_female": 0,
                    "young_male": 0
                },
                "gender": {
                    "?": 0,
                    "female": 0,
                    "male": 0
                },
                "interested": {
                    "value": 0
                },
                "passing_by": {
                    "value": 0
                },
            },
            "2017-09-14T00:00:00+00:00": {
                "category": {
                    "senior_female": 0,
                    "senior_male": 0,
                    "young_female": 0,
                    "young_male": 43
                },
                "gender": {
                    "?": 1,
                    "female": 0,
                    "male": 59
                },
                "interested": {
                    "value": 60
                },
                "passing_by": {
                    "value": 153
                },
            }
        },
        "from_date": "2017-09-03T05:45:00+02:00",
        "total_results": 12,
        "nb_of_pages": 1,
        "next_page": "",
        "page": 1,
        "time": "by_day",
        "to_date": "2017-09-14T16:53:11+02:00"
    }



What next?
**********

You have a running installation of Angus.ai audience analytics solution. Congratulations!

- When time comes, you can plug more cameras by creating additional stream as shown here (:ref:`create-stream`).
- If you need to deploy your system in a situation where internet bandwidth is a problem, please contact us at support@angus.ai.

For any issues please contact Angus.ai team at: support@angus.ai, and if possible,
please specify your operating system, python or java version, as well as the error backtrace if any. Thanks!
