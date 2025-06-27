WRF Module
=========

The ``wrf`` module provides utilities for handling WRF coordinate systems and data array manipulations.

.. automodule:: pywrfkit.wrf
   :members:
   :undoc-members:
   :show-inheritance:

Functions
---------

add_coords
~~~~~~~~~~

.. autofunction:: pywrfkit.wrf.add_coords

renamelatlon
~~~~~~~~~~~

.. autofunction:: pywrfkit.wrf.renamelatlon

Examples
--------

Basic Usage
~~~~~~~~~~

.. code-block:: python

   import xarray as xr
   from pywrfkit import wrf

   # Load WRF data
   ds = xr.open_dataset('wrf_output.nc')

   # Add coordinate information
   ds_with_coords = wrf.add_coords(ds['T2'], rename=True)

   # Rename coordinates
   ds_renamed = wrf.renamelatlon(ds_with_coords)

Coordinate Handling
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Process temperature data
   temp_data = ds['T2']
   temp_with_coords = wrf.add_coords(temp_data, rename=True)
   
   # The coordinates are now properly named
   print(temp_with_coords.coords) 