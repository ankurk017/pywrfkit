from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements from a requirements.txt file if it exists
def read_requirements():
    requirements = []
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    return requirements

setup(
    name="pywrfkit",
    version="0.1.5",
    author="Ankur Kumar",
    author_email="ankurk017@gmail.com",
    description="A comprehensive Python toolkit for Weather Research and Forecasting (WRF) model data processing, analysis, and visualization",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ankurk017/pywrfkit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
    install_requires=[
        "xarray>=2023.1.0",
        "numpy>=1.21.0",
        "matplotlib>=3.5.0",
        "scipy>=1.9.0",
        "pandas>=1.5.0",
        "pyproj>=3.4.0",
    ],
    extras_require={
        "cartopy": ["cartopy>=0.21.0"],
        "docs": [
            "sphinx>=7.0.0",
            "sphinx-rtd-theme>=3.0.0",
            "sphinx-autodoc-typehints>=2.0.0",
        ],
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "twine>=4.0.0",
            "build>=0.10.0",
            "cartopy>=0.21.0",
            "sphinx>=7.0.0",
            "sphinx-rtd-theme>=3.0.0",
            "sphinx-autodoc-typehints>=2.0.0",
        ],
    },
    keywords="wrf, weather, forecasting, meteorology, climate, atmospheric science",
    project_urls={
        "Homepage": "https://github.com/ankurk017/pywrfkit",
        "Documentation": "https://github.com/ankurk017/pywrfkit#readme",
        "Repository": "https://github.com/ankurk017/pywrfkit",
        "Bug Tracker": "https://github.com/ankurk017/pywrfkit/issues",
    },
) 