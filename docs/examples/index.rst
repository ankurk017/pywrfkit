Examples
========

This section provides examples of how to use pywrfkit for various tasks.

.. toctree::
   :maxdepth: 2

Basic Usage Examples
-------------------

.. code-block:: python

   # Import pywrfkit modules
   from pywrfkit import wrf, polar, download
   
   # Basic WRF coordinate handling
   import xarray as xr
   ds = xr.open_dataset('wrf_output.nc')
   ds_with_coords = wrf.add_coords(ds)
   
   # Polar coordinate conversion for hurricane analysis
   polar_data = polar.convert_to_polar(ds, center_lat=25.0, center_lon=-80.0)
   
   # Download GFS forecast data
   download.gfs_forecast('20240101', '20240102', output_dir='./gfs_data')

Hurricane Analysis Example
-------------------------

.. code-block:: python

   from pywrfkit import polar
   import xarray as xr
   
   # Load WRF output data
   ds = xr.open_dataset('hurricane_simulation.nc')
   
   # Convert to polar coordinates around hurricane center
   polar_ds = polar.convert_to_polar(
       ds, 
       center_lat=25.0, 
       center_lon=-80.0,
       radius=500000  # 500 km radius
   )
   
   # Analyze wind patterns
   wind_speed = polar_ds['U10']**2 + polar_ds['V10']**2
   wind_speed = wind_speed**0.5

Data Download Example
--------------------

.. code-block:: python

   from pywrfkit import download
   
   # Download GFS forecast data for a specific date range
   download.gfs_forecast(
       start_date='20240101',
       end_date='20240103',
       output_dir='./gfs_forecasts',
       variables=['TMP', 'RH', 'UGRD', 'VGRD']
   ) 