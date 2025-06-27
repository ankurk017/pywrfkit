Download Module
==============

The ``download`` module provides utilities for automated downloading of GFS forecast data.

.. automodule:: pywrfkit.download
   :members:
   :undoc-members:
   :show-inheritance:

Functions
---------

gfs_forecast
~~~~~~~~~~~

.. autofunction:: pywrfkit.download.gfs_forecast

download_from_filelist
~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: pywrfkit.download.download_from_filelist

Examples
--------

Download GFS Forecast Data
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from pywrfkit import download

   # Download GFS forecast data
   download.gfs_forecast(
       start_date='2024120100',  # YYYYMMDDHH format
       total_forecast_hours=72
   )

   # This will download files like:
   # gfs.0p25.2024120100.f000.grib2
   # gfs.0p25.2024120100.f003.grib2
   # gfs.0p25.2024120100.f006.grib2
   # ... up to f072

Download from File List
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Download specific files from a list
   filelist = [
       'https://data.rda.ucar.edu/d084001/2024/20241201/gfs.0p25.2024120100.f000.grib2',
       'https://data.rda.ucar.edu/d084001/2024/20241201/gfs.0p25.2024120100.f003.grib2',
       'https://data.rda.ucar.edu/d084001/2024/20241201/gfs.0p25.2024120100.f006.grib2'
   ]
   
   download.download_from_filelist(filelist)

Date Format
~~~~~~~~~~~

The start_date parameter uses the format YYYYMMDDHH:

- YYYY: 4-digit year
- MM: 2-digit month (01-12)
- DD: 2-digit day (01-31)
- HH: 2-digit hour (00-23)

Examples:
- '2024120100' = December 1, 2024 at 00:00 UTC
- '2024120112' = December 1, 2024 at 12:00 UTC
- '2025010106' = January 1, 2025 at 06:00 UTC 