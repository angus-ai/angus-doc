.. _api-reference:

Data API Reference
==================

Get entities
------------

Api endpoint for fetching filtered aggregated data (called ``entities``)

* **URL**

  /api/1/entities

* **Method:**

  `GET`


* **URL Params**

  **Required:**

  * ``metrics=[string]``: a list of desired information from the db (comma separated *WITHOUT WHITESPACES*)

    * Possible values: ``interested``, ``passing_by``, ``stop_time``, ``attention_time``, ``category``, ``gender``, ``satisfaction``
    * Default value: none

  * ``from_date=[iso-date]``: the date to start the search from in **ISO FORMAT URLENCODED** (ex: 2017-09-03T05:45:00+0200 becomes 2017-09-03T05%3A45%3A00%2B0200)

    * Default value: none


  **Optional:**

  * ``to_date=[iso-date]``: the date to end the search to in **ISO FORMAT URLENCODED**

    * Default value: the current date


  * ``time=[string]``: a time bucket to aggregate data into

    * Possible values: ``by_hour``, ``by_day``, ``global``
    * Default value: ``global``

  * ``page=[integer]``: a page if enough results for pagination.

    * Default value: 1


* **Success Response:**

  * **Code:** 200
  * **Json content:**

    * ``entities=[json]``: the actual data returned by the api
    * ``time=[str]``: the actual time bucket used to return data
    * ``from_date=[iso-date]``: the date from which the search has been made
    * ``to_date=[iso-date]``: the date to which the search has been made
    * ``total_results=[integer]``: the total number of results for this search
    * ``nb_of_pages=[integer]``: the total number of pages for paginated results
    * ``page=[integer]``: the current retrieved page
    * ``next_page=[str]``: the complete URL to call to get the results for the next page

  .. code:: json

    {
      "entities": {
        "date1": {
          "metric1": {
            "value": 3
          }
        },
        "date2": {
          "metric1": {
            "value": 5
          }
        },
        ...
        ...
        ...
      },
      "from_date": "2017-09-03T05:45:00+02:00",
      "to_date": "2017-09-14T16:53:11+02:00"
      "time": "by_day",
      "total_results": 63,
      "nb_of_pages": 2,
      "next_page": "https://data.angus.ai/api/1/........&page=2",
      "page": 1,

    }

* **Error Response:**

  * **Code:** 401 UNAUTHORIZED
  * **Explanation:** If no "Authorization" header is provided or
    if there is a problem with the JWT token, the error message will
    explain the problem

  OR

  * **Code:** 400 BAD REQUEST
  * **Explanation:** If the request is not well formatted (for instance,
    a required param is not provided, etc...) or any other kind of problem
    with the request, the error message should be self explicit

* **Sample Call:**

  Here is an example of a request for all the metrics between
  September 3rd 2017, 5:45 GMT+2 until now, using a time bucket of "one day".

  .. code:: bash

    curl -X GET -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImF1cmVsaWVuLm1vcmVhdUBhbmd1cy5haSIsIm9yaWdfaWFfta0IjoxNTA1Mzk4MDM4LCJleHAiOjE1MDU0MTYwMzgsImNsaWVudF9pZCI6IjNiZDk1ZjIwLWM2OWYtMTFlNS1hZWVjLTAyNDJhYzExMDAwMiIsInVzZXJfaWQiOjgyNiwiZW1haWwiOiJhdXJlbGllbi5tb3JlYXVAYW5ndXMuYWkifQ.K70YXQYMAcdeW7dfscFGxUhenoXXGBAQTiWhNv-9cVc' 'https://data.angus.ai/api/1/entities?metrics=satisfaction,gender,category,passing_by,interested&from_date=2017-09-03T05%3A45%3A00%2B0200&time=by_day
