.. _metrics:

The metrics
===========

1. Passing By
-------------

  * **Keyword**: ``passing_by``
  * **Schema**:

    .. code:: json

      { "value": 0 }

  * **Description**: Count of people who passed (not necessarily stopping or
    looking) in front of the camera during the specified time duration.

2. Interested
-------------

  * **Keyword**: ``interested``
  * **Schema**:

    .. code:: json

      { "value": 0 }

  * **Description**: Count of people who stopped for at least 3 seconds and looked in the direction of the camera more than 1 second.

3. Average stopping time
------------------------

  * **Keyword**: ``stop_time``
  * **Schema**:

    .. code:: json

      { "value": null }

  * **Description**: Average time a person, among the "interested" people (see `above <2. Interested_>`_), stay still in front of the camera. (in second)

4. Average attention time
-------------------------

  * **Keyword**: ``attention_time``
  * **Schema**:

    .. code:: json

      { "value": null }

  * **Description**: Average time a person, among the "interested" people (see `above <2. Interested_>`_), spend looking at the camera. (in second)

5. Category
-----------

  * **Keyword**: ``category``
  * **Schema**:

    .. code:: json

      {
        "senior_female": 0,
        "senior_male": 0,
        "young_female": 0,
        "young_male": 0
      }

  * **Description**: Population segmentation counts of all the "interested" people (see `above <2. Interested_>`_) for each category.

6. Gender
---------

  * **Keyword**: ``gender``
  * **Schema**:

    .. code:: json

      {
        "?": 0,
        "female": 0,
        "male": 0
      }

  * **Description**: The gender repartition of all the "interested" people (see `above <2. Interested_>`_).
