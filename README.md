[![PyPI version](https://badge.fury.io/py/pywrfkit.svg)](https://badge.fury.io/py/pywrfkit)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/ankurk017/pywrfkit/workflows/Test%20Package/badge.svg)](https://github.com/ankurk017/pywrfkit/actions)
[![Build](https://github.com/ankurk017/pywrfkit/workflows/Build%20and%20Test/badge.svg)](https://github.com/ankurk017/pywrfkit/actions)
[![Publish](https://github.com/ankurk017/pywrfkit/workflows/Publish%20to%20PyPI/badge.svg)](https://github.com/ankurk017/pywrfkit/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)
[![Issues](https://img.shields.io/github/issues/ankurk017/pywrfkit)](https://github.com/ankurk017/pywrfkit/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/ankurk017/pywrfkit)](https://github.com/ankurk017/pywrfkit/pulls)

# PyWRFKit

A comprehensive Python toolkit for Weather Research and Forecasting (WRF) model data processing, analysis, and visualization. This toolkit provides utilities for handling WRF coordinate transformations, data downloading, plotting, and various meteorological analysis tasks.

## Features

- **WRF Data Processing**: Coordinate handling and data manipulation for WRF model outputs
- **Polar Coordinate Transformations**: Convert Cartesian coordinates to polar for hurricane analysis
- **Data Downloading**: Automated GFS forecast data retrieval
- **Visualization**: Cartopy-based mapping and plotting utilities
- **Statistical Analysis**: Various metrics and norms for data comparison
- **AHPS Data Processing**: Advanced Hydrologic Prediction Service data handling

## Installation

```bash
# Install from PyPI
pip install pywrfkit

# Install with cartopy support (for visualization modules)
pip install pywrfkit[cartopy]

# Or install from source
git clone https://github.com/ankurk017/pywrfkit.git
cd pywrfkit
pip install -e .

# Install with cartopy support from source
pip install -e .[cartopy]
```

### Dependencies

**Core Dependencies:**
- `xarray` - Multi-dimensional array handling
- `numpy` - Numerical computing
- `matplotlib` - Plotting and visualization
- `scipy` - Scientific computing
- `pandas` - Data manipulation
- `pyproj` - Cartographic projections

**Optional Dependencies:**
- `cartopy` - Geographic plotting (required for `coast`, `plot_geog`, and `ahps` modules)

**Note:** The `coast`, `plot_geog`, and `ahps` modules require cartopy. If cartopy is not installed, these modules will raise an ImportError when used. Install with `pip install pywrfkit[cartopy]` to include cartopy support.

## Documentation

Comprehensive documentation is available at: **https://ankurk017.github.io/pywrfkit/**

### Building Documentation Locally

To build the documentation locally:

```bash
# Install documentation dependencies
pip install pywrfkit[docs]

# Build documentation
cd docs
make html

# Or use the build script
python build_docs.py
```

The documentation will be available at `docs/_build/html/index.html`.

### Documentation Features

- **API Reference**: Complete function and module documentation
- **Installation Guide**: Detailed setup instructions
- **Examples**: Practical usage examples and workflows
- **Contributing Guidelines**: How to contribute to the project
- **Changelog**: Version history and changes

## Modules Overview

### Core WRF Utilities (`wrf.py`)

Handles WRF coordinate systems and data array manipulations.

```python
import xarray as xr
from pywrfkit import wrf

# Load WRF data
ds = xr.open_dataset('wrf_output.nc')

# Add coordinate information
ds_with_coords = wrf.add_coords(ds['T2'], rename=True)

# Rename coordinates
ds_renamed = wrf.renamelatlon(ds_with_coords)
```

### Polar Coordinate Transformations (`polar.py`)

Converts Cartesian coordinates to polar coordinates for hurricane analysis.

```python
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

# Process entire dataset
polar_dataset = polar.get_polar_from_file(
    'hurricane_data.nc',
    radius=5,
    resolution=0.1
)
```

### Data Downloading (`download.py`)

Automated downloading of GFS forecast data.

```python
from pywrfkit import download

# Download GFS forecast data
download.gfs_forecast(
    start_date='2024120100',  # YYYYMMDDHH format
    total_forecast_hours=72
)

# Download from file list
filelist = [
    'https://data.rda.ucar.edu/d084001/2024/20241201/gfs.0p25.2024120100.f000.grib2',
    'https://data.rda.ucar.edu/d084001/2024/20241201/gfs.0p25.2024120100.f003.grib2'
]
download.download_from_filelist(filelist)
```

### Visualization Utilities (`coast.py`, `plot_geog.py`)

Cartopy-based mapping and geographic plotting.

```python
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from pywrfkit import coast, plot_geog

# Create a map with coastlines
fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': ccrs.PlateCarree()})
gl = coast.plot_coast(ax, color='blue', linewidth=1.5, states=True)

# Plot geographic data
plot_geog.plot_lulc_geogrid(
    'geo_em.d01.nc_2001',
    label='LULC 2001',
    legend=True,
    axes=ax
)
plt.show()
```

### AHPS Data Processing (`ahps.py`)

Process Advanced Hydrologic Prediction Service data.

```python
from pywrfkit import ahps

# Read AHPS data
lon, lat, obs = ahps.read_ahps('ahps_data.nc')

# Data is automatically converted to Plate Carree projection
# and invalid values are replaced with NaN
print(f"Longitude range: {lon.min():.2f} to {lon.max():.2f}")
print(f"Latitude range: {lat.min():.2f} to {lat.max():.2f}")
print(f"Observation shape: {obs.shape}")
```

### Statistical Analysis (`metrics.py`, `norms.py`)

Various statistical metrics and norms for data comparison.

```python
import numpy as np
from pywrfkit import metrics, norms

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1.1, 2.2, 2.8, 4.1, 5.2])

# Calculate metrics
l1_error = metrics.l1(x, y)
l2_error = metrics.l2(x, y)
sup_error = metrics.sup(x, y)

print(f"L1 error: {l1_error:.3f}")
print(f"L2 error: {l2_error:.3f}")
print(f"Sup error: {sup_error:.3f}")

# Calculate norms
l1_norm = norms.l1(x)
l2_norm = norms.l2(x)
sup_norm = norms.sup(x)

print(f"L1 norm: {l1_norm:.3f}")
print(f"L2 norm: {l2_norm:.3f}")
print(f"Sup norm: {sup_norm:.3f}")
```

### Data Exploration (`xrvar.py`)

Utilities for exploring xarray datasets.

```python
import xarray as xr
from pywrfkit import xrvar

# Load dataset
ds = xr.open_dataset('wrf_output.nc')

# List variables with attributes
var_info = xrvar.varlist(ds, ['units', 'long_name'])
print(var_info)
```

### Plotting Parameters (`params.py`)

Configure matplotlib plotting parameters.

```python
from pywrfkit import params

# Update plotting parameters
params.get_params()

# Now all plots will use the updated settings
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
plt.show()
```

## Complete Example: Hurricane Analysis Workflow

```python
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from pywrfkit import wrf, polar, coast, download, params

# Set up plotting parameters
params.get_params()

# Download GFS data for hurricane analysis
download.gfs_forecast('2024120100', 72)

# Load WRF output data
ds = xr.open_dataset('wrfout_d01_2024-12-01_00:00:00')

# Process wind data
wind_speed = wrf.add_coords(ds['U10'], rename=True)

# Convert to polar coordinates for hurricane analysis
polar_wind = polar.convert_to_polar(
    wind_speed,
    radius=5,  # 5 degrees radius
    resolution=0.1
)

# Create visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), 
                               subplot_kw={'projection': ccrs.PlateCarree()})

# Plot original data
coast.plot_coast(ax1)
ax1.pcolormesh(wind_speed.longitudes, wind_speed.latitudes, wind_speed.values)
ax1.set_title('Wind Speed (Cartesian)')

# Plot polar data
ax2.pcolormesh(polar_wind.angle, polar_wind.radius, polar_wind.values)
ax2.set_title('Wind Speed (Polar)')
ax2.set_xlabel('Angle (radians)')
ax2.set_ylabel('Radius (km)')

plt.tight_layout()
plt.show()
```

## File Structure

```
pywrfkit/
├── README.md           # This file
├── LICENSE            # License information
├── __init__.py        # Package initialization
├── wrf.py             # WRF coordinate utilities
├── polar.py           # Polar coordinate transformations
├── download.py        # Data downloading utilities
├── coast.py           # Coastline plotting utilities
├── plot_geog.py       # Geographic plotting functions
├── ahps.py            # AHPS data processing
├── xrvar.py           # xarray variable utilities
├── params.py          # Plotting parameters
├── metrics.py         # Statistical metrics
└── norms.py           # Mathematical norms
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the terms specified in the LICENSE file.

## Citation

If you use this toolkit in your research, please cite:

```bibtex
@software{pywrfkit,
  title={PyWRFKit: A Python Toolkit for WRF Data Processing and Analysis},
  author={Ankur Kumar},
  year={2024},
  url={https://github.com/ankurk017/pywrfkit}
}
```

## Support

For questions, issues, or contributions, please open an issue on the GitHub repository or contact the maintainer at ankurk017@gmail.com.

## Acknowledgments

- WRF Development Team for the Weather Research and Forecasting model
- Cartopy developers for geographic plotting capabilities
- xarray developers for multi-dimensional array handling
- The scientific Python community for the excellent ecosystem of tools
