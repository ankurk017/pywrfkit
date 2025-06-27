Changelog
=========

All notable changes to PyWRFKit will be documented in this file.

Version 0.1.5 (2025-06-26)
--------------------------

**Added**
- Optional cartopy dependency support
- Graceful handling of cartopy-dependent modules
- Updated package configuration for optional dependencies
- Enhanced test suite with optional cartopy testing
- GitHub badges in README

**Changed**
- Moved cartopy from core to optional dependencies
- Updated installation instructions for optional cartopy support
- Modified module imports to handle cartopy availability

**Fixed**
- Improved error handling for cartopy-dependent modules
- Updated GitHub Actions workflows for optional cartopy testing

Version 0.1.4 (2025-06-26)
--------------------------

**Changed**
- Commented out GDAL imports in plot_geog.py
- Updated version numbers across all configuration files

Version 0.1.3 (2025-06-26)
--------------------------

**Changed**
- Commented out GDAL imports in plot_geog.py
- Updated version numbers across all configuration files

Version 0.1.2 (2025-06-26)
--------------------------

**Removed**
- GDAL dependency completely
- geog.py module (GDAL-dependent)

**Changed**
- Updated all configuration files to remove GDAL references
- Simplified imports and dependencies
- Updated README to reflect GDAL removal

Version 0.1.1 (2025-06-26)
--------------------------

**Added**
- Initial PyPI release
- Core WRF utilities (wrf module)
- Polar coordinate transformations (polar module)
- Data downloading utilities (download module)
- Statistical analysis tools (metrics, norms modules)
- Data exploration utilities (xrvar module)
- Plotting parameters (params module)
- Geographic plotting (coast, plot_geog modules)
- AHPS data processing (ahps module)

**Features**
- WRF coordinate handling and data manipulation
- Hurricane analysis with polar coordinate transformations
- Automated GFS forecast data downloading
- Cartopy-based mapping and visualization
- Statistical metrics and norms for data comparison
- Comprehensive documentation and examples 