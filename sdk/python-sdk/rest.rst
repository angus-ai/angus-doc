RESTful framework
=================

angus.rest
++++++++++

.. py:module:: angus.rest

``angus.rest`` provides a simple RESTful framework to manipulates Angus.ai
resources.

Configuration
+++++++++++++

.. py:class:: Configuration
    
    Configure credentials and endpoint.
    
    .. py:attribute:: default_root
    
        This is the default endpoint for Angus.ai (for example https://www.angus.ai).
    
    .. py:method:: set_credential
    
        Set the ``client_id`` and ``access_token``.
    
    .. py:method:: set_ca_path
    
        Path to a file that contains all client side certificate
    
    .. py:method:: do_not_verify
    
        Disable server certificate verification


Resource
++++++++

.. py:class:: Resource

    All server side object are provided as a "resource" according to the 
    RESTful philosophy.
    
    .. py:data:: CREATED
    
        The HTTP code for created status.
    
    .. py:data:: ACCEPTED
    
        The HTTP code for accepted status.
    
    .. py:attribute:: endpoint
    
        This is the absolute web address of the resource. For example 
        https://gate.angus.ai/services/face_detection/1 for version 1 of the 
        face_detection service.
        
    .. py:attribute:: representation
    
        This is the python representation of the resource 
        (convert from json and/or binary format).
        
    .. py:attribute:: conf
    
        Each resource stores a configuration to access the cloud.
    
    .. py:attribute:: status
    
        A resource has a ``status``, this is a HTTP code to provide
        a stage of the process (200, 201 etc...)
    
    .. py:method:: fetch 
        
        Force to re-synchronize the local representation with the cloud.

Collection
++++++++++

.. py:class:: Collection

    A collection is a special resource that contains other resources. It 
    enable creation and listing. By default if the collection endpoint is 
    https://gate.angus.ai/collections, an element of this collection has 
    https://gate.angus.ai/collections/element as endpoint.
    
    .. py:method:: create(parameters, resource_type=Resource)
        
        Create a new element in the collection. ``parameters`` is a python 
        object that is JSON serializable (see official documentation `here 
        <https://docs.python.org/2/library/json.html>`_. These parameters will
        be used by the collection in cloud side to create the new element.

    .. py:method:: list(filters)
    
        List all elements of the collection. `filters` is a dictionary that will
        be send to the cloud as query string.

Service
+++++++

.. py:class:: Service

    A service is a specific resource that contains a job collection and provide
    a description.

    .. py:attribute:: description
    
        This is the description of the service.
    
    .. py:attribute:: jobs

        This is a collection of Job resources.

    .. py:method:: process(parameters=None, async=False, session=None, callback=None)
    
        Shortcut to create an element in jobs collection. `async` option is 
        added to `parameters`, it suggests to the cloud to run the job creation
        asynchronously. The cloud is not obliged, and the client must check the
        result status (201 for created, or 202 if the request is accepted but the
        resource is not created).
        A `Session` object can be used to store the state in client side.
        Finaly, function can be defined in `callback` to be triggered when job is 
        finished. 
        
    .. py:method:: get_description()
    
        Shortcut to get the resource description.
        
    .. py:method:: create_session()
    
        Create a a session object
        
    .. py:method:: enable_session()
    
        A service object in the SDK can store a "default" session.
        
    .. py:method:: disable_session()
    
        Disable the "default" session facility. 
        
        
.. py:class:: Job

    A `Job` is a resource with a shortcut `result` to get its representation
    
    .. py:attribute:: result
        
        A shortcut for representation of the resource.
        
.. py:class:: Session

    A session is a local sdk object to store the client side state.

    .. py:method:: state
        
        Get the representation of the local state.
