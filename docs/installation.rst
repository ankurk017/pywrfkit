Installation Guide
=================

PyWRFKit can be installed from PyPI or from source. The package supports both core functionality and optional cartopy-dependent features.

From PyPI
--------

The simplest way to install PyWRFKit is using pip:

.. code-block:: bash

   pip install pywrfkit

For full functionality including cartopy-dependent modules (coast, plot_geog, ahps):

.. code-block:: bash

   pip install pywrfkit[cartopy]

From Source
----------

Clone the repository and install in development mode:

.. code-block:: bash

   git clone https://github.com/ankurk017/pywrfkit.git
   cd pywrfkit
   pip install -e .

For development with cartopy support:

.. code-block:: bash

   pip install -e .[dev]

Dependencies
-----------

Core Dependencies
~~~~~~~~~~~~~~~~

These dependencies are automatically installed with PyWRFKit:

- `xarray >= 2023.1.0` - Multi-dimensional array handling
- `numpy >= 1.21.0` - Numerical computing
- `matplotlib >= 3.5.0` - Plotting and visualization
- `scipy >= 1.9.0` - Scientific computing
- `pandas >= 1.5.0` - Data manipulation
- `pyproj >= 3.4.0` - Cartographic projections

Optional Dependencies
~~~~~~~~~~~~~~~~~~~~

- `cartopy >= 0.21.0` - Geographic plotting (required for coast, plot_geog, and ahps modules)

Development Dependencies
~~~~~~~~~~~~~~~~~~~~~~~

For development and testing:

- `pytest >= 7.0.0` - Testing framework
- `pytest-cov >= 4.0.0` - Coverage reporting
- `black >= 22.0.0` - Code formatting
- `flake8 >= 5.0.0` - Linting
- `twine >= 4.0.0` - Package uploading
- `build >= 0.10.0` - Package building

System Requirements
------------------

- Python 3.8 or higher
- For cartopy support: Additional system libraries may be required depending on your platform

Troubleshooting
--------------

Cartopy Installation Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you encounter issues installing cartopy:

1. **Ubuntu/Debian:**
   .. code-block:: bash

      sudo apt-get install libproj-dev proj-data proj-bin
      sudo apt-get install libgeos-dev
      pip install cartopy

2. **macOS:**
   .. code-block:: bash

      brew install proj geos
      pip install cartopy

3. **Windows:**
   Use conda for easier installation:
   .. code-block:: bash

      conda install -c conda-forge cartopy

4. **Alternative:** Install without cartopy for core functionality only:
   .. code-block:: bash

      pip install pywrfkit

Verification
-----------

After installation, verify that PyWRFKit is working correctly:

.. code-block:: python

   import pywrfkit
   print(f"PyWRFKit version: {pywrfkit.__version__}")
   print(f"Cartopy available: {pywrfkit.CARTOPY_AVAILABLE}")

   # Test core modules
   from pywrfkit import wrf, polar, download, xrvar, params, metrics, norms
   print("Core modules imported successfully")

   # Test cartopy-dependent modules (if cartopy is installed)
   try:
       from pywrfkit import coast, plot_geog, ahps
       print("Cartopy-dependent modules imported successfully")
   except ImportError:
       print("Cartopy not available, skipping cartopy-dependent modules") 