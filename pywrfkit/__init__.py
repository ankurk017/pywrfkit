"""
PyWRFKit: A comprehensive Python toolkit for Weather Research and Forecasting (WRF) model data processing, analysis, and visualization.

This package provides utilities for:
- WRF coordinate handling and data manipulation
- Geographic data processing (LULC, NDVI)
- Polar coordinate transformations for hurricane analysis
- Data downloading from meteorological sources
- Visualization and plotting utilities
- Statistical analysis and metrics
- AHPS data processing
"""

__version__ = "0.1.1"
__author__ = "Ankur Kumar"
__email__ = "ankurk017@gmail.com"

# Import core modules (always available)
from . import wrf
from . import polar
from . import download
from . import coast
from . import plot_geog
from . import xrvar
from . import params
from . import metrics
from . import norms

# Import GDAL-dependent modules (optional)
try:
    from . import geog
    from . import ahps
    _GDAL_AVAILABLE = True
except ImportError as e:
    _GDAL_AVAILABLE = False
    print(f"⚠ GDAL-dependent modules (geog, ahps) not available: {e}")
    print("  Install with: pip install pywrfkit[full]")

# Define what gets imported with "from pywrfkit import *"
__all__ = [
    'wrf',
    'polar',
    'download',
    'coast',
    'plot_geog',
    'xrvar',
    'params',
    'metrics',
    'norms',
]

# Add GDAL-dependent modules to __all__ if available
if _GDAL_AVAILABLE:
    __all__.extend(['geog', 'ahps'])

# Provide a function to check GDAL availability
def is_gdal_available():
    """Check if GDAL-dependent modules are available."""
    return _GDAL_AVAILABLE
