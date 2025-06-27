Modules
=======

PyWRFKit is organized into several modules, each providing specific functionality for WRF data processing and analysis.

Core Modules
-----------

These modules provide essential functionality and are always available:

.. toctree::
   :maxdepth: 2

   wrf
   polar
   download
   xrvar
   params
   metrics
   norms

Optional Modules
---------------

These modules require cartopy to be installed:

.. toctree::
   :maxdepth: 2

   coast
   plot_geog
   ahps

Module Overview
--------------

Core Modules
~~~~~~~~~~~

- **wrf**: WRF coordinate handling and data array manipulations
- **polar**: Convert Cartesian coordinates to polar for hurricane analysis
- **download**: Automated GFS forecast data retrieval
- **xrvar**: Utilities for exploring xarray datasets
- **params**: Configure matplotlib plotting parameters
- **metrics**: Various statistical metrics for data comparison
- **norms**: Mathematical norms for data analysis

Optional Modules (require cartopy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **coast**: Cartopy-based mapping and coastline utilities
- **plot_geog**: Geographic plotting and visualization
- **ahps**: Advanced Hydrologic Prediction Service data processing

Usage Examples
-------------

.. code-block:: python

   # Core functionality (always available)
   from pywrfkit import wrf, polar, download, metrics
   
   # Optional functionality (requires cartopy)
   try:
       from pywrfkit import coast, plot_geog, ahps
   except ImportError:
       print("Cartopy not available") 