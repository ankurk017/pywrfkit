Examples
========

This section provides comprehensive examples of how to use PyWRFKit for various meteorological analysis tasks.

Getting Started
--------------

.. toctree::
   :maxdepth: 2

   basic_usage
   hurricane_analysis
   data_visualization

Workflow Examples
----------------

.. toctree::
   :maxdepth: 2

   wrf_processing
   polar_analysis
   data_download

Advanced Examples
----------------

.. toctree::
   :maxdepth: 2

   statistical_analysis
   custom_plots

Example Gallery
--------------

Basic WRF Data Processing
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import xarray as xr
   from pywrfkit import wrf, polar, metrics

   # Load WRF output
   ds = xr.open_dataset('wrfout_d01_2024-12-01_00:00:00')
   
   # Process temperature data
   temp = wrf.add_coords(ds['T2'], rename=True)
   temp_renamed = wrf.renamelatlon(temp)
   
   print(f"Temperature range: {temp_renamed.min():.2f} to {temp_renamed.max():.2f} K")

Hurricane Analysis
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Convert wind data to polar coordinates
   wind_speed = wrf.add_coords(ds['U10'], rename=True)
   polar_wind = polar.convert_to_polar(
       wind_speed,
       radius=5,  # degrees
       resolution=0.1
   )
   
   # Calculate statistics
   mean_wind = polar_wind.mean()
   max_wind = polar_wind.max()
   
   print(f"Mean wind speed: {mean_wind:.2f} m/s")
   print(f"Maximum wind speed: {max_wind:.2f} m/s")

Data Download and Processing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from pywrfkit import download
   
   # Download GFS forecast data
   download.gfs_forecast(
       start_date='2024120100',
       total_forecast_hours=72
   )
   
   # Process downloaded data
   # (Additional processing code would go here) 