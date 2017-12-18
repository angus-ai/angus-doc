.. _dashboard:

Online dashboard
================
.. after-title

The client app you just ran is now feeding a personal and secured database with audience analytics data that you can check by following the steps below.


How to view your dashboard
--------------------------

The collected data are meant to be collected programmatically through Angus.ai Data API (see :ref:`data-api`).
But for demonstration purposes, we have put together a standard dashboard that allows for a simple visualization over your collected data.

We will use this default dashboard to check that your installation is properly set and that your data are properly stored.
But you can also use it for demonstration and even for real world deployment purposes, if it suits your needs.

To view your dashboard:

1. Go back to your personal account here: https://console.angus.ai/
2. Click on the “Show Dashboard” button on the stream you created above.
3. You should see a page showing a dashboard (see example below). If you just launch the client app as explained here (:ref:`apps`), your dashboard might still be empty.
   Indeed there is about 1min time delay between what happen in front of your camera and the dashboard refreshing for these data. After waiting for the next automatic refresh
   (see the watch icon on the top right hand corner), your first collected data should appear (as shown on the screenshot below).
4. If your don’t see data appear, please try to get out of the camera field of view and re-enter again.

.. image:: ../images/dashboard.png

What are these metrics?
-----------------------

**People passing by**:
Count of people who passed (not necessarily stopping or looking) in front of the camera for at least 1 second.

**People Interested**:
Count of people who stopped for at least 3 seconds and looked in the direction of the camera more than 1 second, during the specified time duration.

**Average stopping time**:
Average time a person, among the “interested” people (see above), stay still in front of the camera (in second).

**Average attention time**:
Average time a person, among the “interested” people (see above), spend looking at the camera (in second).

**Age Pie Chart**:
Population segmentation counts of all the “interested” people (see above) for each category.

**Gender Chart**:
The gender repartition of all the “interested” people (see above).


Congratulations, you now have a properly running installation of our audience analytics solution.

If you want to retrieve these data programmatically (for further integration into your own dashboard for example), you have got one more step to go.
