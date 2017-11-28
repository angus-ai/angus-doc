Angus.ai framework
==================

angus.cloud
+++++++++++

.. py:module: angus.cloud

``angus.cloud`` provides the high level object to manipulate Angus.ai specific concept.


CompositeService
++++++++++++++++

.. py:class:: CompositeService

    This is an pure sdk object that wrapped many services. It inherits from
    :py:class:`angus.rest.Service` and provides the same methods.

Root
++++

.. py:class:: Root

    This is the resource starting point for resource construction. It provides transverse
    services and enables service searching.
    
    .. py:attribute:: blobs
        
        This is a collection of undefined resource, that enables binary storage
        see :py:class:`BlobDirectory`.
    
    .. py:attribute:: services
    
        This is a collection of service that enables service retrieving, see
        :py:class:`ServiceDirectory`.


.. py:class:: BlobDirectory

    .. py:method:: create(binary)
    
        Create a new resource in blob storage with binary as content.

.. py:class:: ServiceDirectory

    .. py:method:: get_service(name, version=None, service_class=rest.Service)
    
        Retrieve service with name. If version is not defined, the maximum (last)
        version number is selected.
    
    .. py:method:: get_services(, services=None)

        Retrive many services and return a :py:class:`CompositeService`.
        
        * If services is a list of string, selects services with last version number.
        * If services is a list of ``tuple(name, version)``, selects service with given version.
        * If services is None, select all service with last version.



