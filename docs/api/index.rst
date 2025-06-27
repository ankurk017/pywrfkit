API Reference
============

This section provides detailed API documentation for all PyWRFKit modules and functions.

Core Modules
-----------

.. toctree::
   :maxdepth: 2

   wrf_api
   polar_api
   download_api
   xrvar_api
   params_api
   metrics_api
   norms_api

Optional Modules
---------------

.. toctree::
   :maxdepth: 2

   coast_api
   plot_geog_api
   ahps_api

Package Information
------------------

.. automodule:: pywrfkit
   :members:
   :undoc-members:
   :show-inheritance:

Module Availability
------------------

The following table shows which modules are available based on your installation:

+----------------+------------------+------------------+
| Module         | Core Package     | With Cartopy     |
+================+==================+==================+
| wrf            | ✅               | ✅               |
+----------------+------------------+------------------+
| polar          | ✅               | ✅               |
+----------------+------------------+------------------+
| download       | ✅               | ✅               |
+----------------+------------------+------------------+
| xrvar          | ✅               | ✅               |
+----------------+------------------+------------------+
| params         | ✅               | ✅               |
+----------------+------------------+------------------+
| metrics        | ✅               | ✅               |
+----------------+------------------+------------------+
| norms          | ✅               | ✅               |
+----------------+------------------+------------------+
| coast          | ❌               | ✅               |
+----------------+------------------+------------------+
| plot_geog      | ❌               | ✅               |
+----------------+------------------+------------------+
| ahps           | ❌               | ✅               |
+----------------+------------------+------------------+

Check module availability:

.. code-block:: python

   import pywrfkit
   print(f"Cartopy available: {pywrfkit.CARTOPY_AVAILABLE}") 