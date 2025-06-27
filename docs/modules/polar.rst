Polar Module
===========

The ``polar`` module provides utilities for converting Cartesian coordinates to polar coordinates for hurricane analysis.

.. automodule:: pywrfkit.polar
   :members:
   :undoc-members:
   :show-inheritance:

Functions
---------

convert_to_polar
~~~~~~~~~~~~~~~

.. autofunction:: pywrfkit.polar.convert_to_polar

get_polar_from_file
~~~~~~~~~~~~~~~~~~

.. autofunction:: pywrfkit.polar.get_polar_from_file

Examples
--------

Basic Polar Conversion
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import xarray as xr
   from pywrfkit import polar

   # Load hurricane data
   ds = xr.open_dataset('hurricane_data.nc')

   # Convert to polar coordinates
   polar_data = polar.convert_to_polar(
       ds['wind_speed'],
       radius=5,  # degrees
       resolution=0.1
   )

   print(f"Polar data shape: {polar_data.shape}")
   print(f"Radius range: {polar_data.radius.min():.2f} to {polar_data.radius.max():.2f} km")

Processing Entire Dataset
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Process entire dataset with multiple models and times
   polar_dataset = polar.get_polar_from_file(
       'hurricane_data.nc',
       radius=5,
       resolution=0.1
   )

   # Access polar data
   model_outputs_polar = polar_dataset['model_outputs_polar']
   observations_polar = polar_dataset['merra_pcp_polar']

   print(f"Model outputs shape: {model_outputs_polar.shape}")
   print(f"Observations shape: {observations_polar.shape}")

Hurricane Analysis Workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Complete hurricane analysis workflow
   import numpy as np
   import matplotlib.pyplot as plt
   from pywrfkit import polar, wrf

   # Load and process WRF data
   ds = xr.open_dataset('wrfout_d01_2024-12-01_00:00:00')
   wind_speed = wrf.add_coords(ds['U10'], rename=True)

   # Convert to polar coordinates
   polar_wind = polar.convert_to_polar(
       wind_speed,
       radius=5,  # 5 degrees radius
       resolution=0.1
   )

   # Plot polar wind data
   plt.figure(figsize=(10, 8))
   plt.pcolormesh(polar_wind.angle, polar_wind.radius, polar_wind.values)
   plt.colorbar(label='Wind Speed (m/s)')
   plt.xlabel('Angle (radians)')
   plt.ylabel('Radius (km)')
   plt.title('Hurricane Wind Speed in Polar Coordinates')
   plt.show() 