.. PyWRFKit documentation master file, created by
   sphinx-quickstart on Thu Jun 26 21:46:30 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyWRFKit's documentation!
====================================

A comprehensive Python toolkit for Weather Research and Forecasting (WRF) model data processing, analysis, and visualization.

.. image:: https://badge.fury.io/py/pywrfkit.svg
   :target: https://badge.fury.io/py/pywrfkit
   :alt: PyPI version

.. image:: https://img.shields.io/badge/python-3.8+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python 3.8+

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT

.. image:: https://github.com/ankurk017/pywrfkit/workflows/Test%20Package/badge.svg
   :target: https://github.com/ankurk017/pywrfkit/actions
   :alt: Tests

.. image:: https://github.com/ankurk017/pywrfkit/workflows/Build%20and%20Test/badge.svg
   :target: https://github.com/ankurk017/pywrfkit/actions
   :alt: Build

.. image:: https://github.com/ankurk017/pywrfkit/workflows/Publish%20to%20PyPI/badge.svg
   :target: https://github.com/ankurk017/pywrfkit/actions
   :alt: Publish

Installation
-----------

.. code-block:: bash

   # Install from PyPI
   pip install pywrfkit

   # Install with cartopy support (for visualization modules)
   pip install pywrfkit[cartopy]

   # Or install from source
   git clone https://github.com/ankurk017/pywrfkit.git
   cd pywrfkit
   pip install -e .

Quick Start
----------

.. code-block:: python

   import xarray as xr
   from pywrfkit import wrf, polar, download

   # Load WRF data
   ds = xr.open_dataset('wrf_output.nc')

   # Add coordinate information
   ds_with_coords = wrf.add_coords(ds['T2'], rename=True)

   # Convert to polar coordinates for hurricane analysis
   polar_data = polar.convert_to_polar(
       ds['wind_speed'],
       radius=5,  # degrees
       resolution=0.1
   )

   # Download GFS forecast data
   download.gfs_forecast(
       start_date='2024120100',  # YYYYMMDDHH format
       total_forecast_hours=72
   )

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   modules/index
   examples/index
   api/index
   contributing
   changelog

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
