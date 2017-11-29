Getting started
===============

This documentation is aimed at developers wanting to retrieve programmatically the data computed
by Angus.ai audience analytics solution through our Data REST API (see diagram below).

.. image:: ../../archi.jpeg

**Prerequisite**

This procedure requires that you already have a properly configured audience analytics client application running on your device.
If this is not the case, please follow our step by step instruction here: (:ref:`audience-tuto`).

API Authentication
------------------

Info
****

You need a JSON Web Token ("JWT") token in order to securely call the data
api endpoint. Your personal JWT is provided by programmatically calling the
appropriate endpoint documented below.

Endpoint and parameters
***********************

To retrieve a JWT token, you have to make a ``POST`` request to:

``https://console.angus.ai/api-token-authstream``

* **Description**: retrieve a JWT token associated to
* **Authentication**: none
* **Parameters**:

  - ``username``: your console login (email)
  - ``client_id``: the client_id associated with your stream
  - ``access_token``: the access_token associated with your stream
* **Response Code**: 200 OK
* **Response**: JSON

Example
*******

   *Request:*

   .. code:: bash

     curl -X POST -H "Content-Type: application/json" -d '{"username": "aurelien.moreau@angus.ai", "client_id": "3bd15f50-c69f-11e5-ae3c-0242ad110002", "access_token": "543eb007-1bfe-89d7-b092-e127a78fe91c"}' https://console.angus.ai/api-token-authstream/


   *Response:*

   .. code:: json

     {
       "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImF1cmVsaWVuLm1vcmVhdUBhbmd1cy5haSIsIm9yaWdfaWF0IjoxNTA1Mzk4MDM4LCJleHAiOjE1D8DU0MTYwMzgsImNsaWVudF9pZCI6IjNiZDk1ZjIwLWM2OWYtMTFlNS1hZWVjLTAyNDJhYzExMDAwMiIsInVzZXJfaWQiOjgyNiwiZW1haWwiOiJhdXJlbGllbi5tb3JlYXVAYW5ndXMuYWkifQ.K70YXQYMAcdeW7dfscFGxUhenoXXGBAQTiWhNv-9cVc"
     }

Once provided, you will need to put this token as a HTTP header
``Authorization: Bearer [YOURJWTTOKEN]`` (see the Python example in `Retrieving the data`_) in every
HTTP requests you make.


Retrieving the data
-------------------

Once you obtained your personal JWT, you can start retrieving your data by calling the endpoint
documented in the :ref:`api-reference` page.

Python example
**************

For this example, you will need to install ``requests`` and ``pytz`` modules

.. code:: python

  import requests
  import pytz
  import datetime
  import json


  def get_token():
    data = {
      "username": "test@example.com",
      "client_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "access_token": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    }

    req = requests.post('https://console.angus.ai/api-token-authstream/', json=data)
    req.raise_for_status()
    req = req.json()

    return req['token']


  def get(token, metrics, from_date, to_date, size):
    entities_url = 'https://data.angus.ai/api/1/entities'
    params = {
      "metrics": ",".join(metrics),
      "from_date": from_date.isoformat(),
      "to_date": to_date.isoformat(),
      "time": size,
    }

    headers = {
      "Authorization": "Bearer {}".format(token)
    }

    req = requests.get(entities_url, params=params, headers=headers)
    req.raise_for_status()
    req = req.json()

    return req


  def get_overall(token):
    to_date = datetime.datetime.now(pytz.UTC)
    from_date = to_date - datetime.timedelta(hours=24)

    metrics = [
      "passing_by",
      "interested",
      "stop_time",
      "attention_time",
    ]

    return get(token, metrics, from_date, to_date, "global")


  def main():
    token = get_token()
    overall = get_overall(token)
    print(json.dumps(overall, indent=2))


  if __name__ == "__main__":
    main()
