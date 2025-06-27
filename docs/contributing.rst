Contributing
===========

Thank you for your interest in contributing to PyWRFKit! This document provides guidelines for contributing to the project.

Getting Started
--------------

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Create a feature branch** for your changes
4. **Make your changes** and commit them
5. **Push to your fork** and submit a pull request

Development Setup
----------------

.. code-block:: bash

   # Clone your fork
   git clone https://github.com/YOUR_USERNAME/pywrfkit.git
   cd pywrfkit

   # Install in development mode
   pip install -e .[dev]

   # Install documentation dependencies
   pip install sphinx sphinx-rtd-theme sphinx-autodoc-typehints

Code Style
----------

PyWRFKit follows PEP 8 style guidelines and uses Black for code formatting:

.. code-block:: bash

   # Format code with Black
   black pywrfkit/ tests/

   # Check code style with flake8
   flake8 pywrfkit/ tests/

Testing
-------

Run the test suite to ensure your changes don't break existing functionality:

.. code-block:: bash

   # Run all tests
   pytest tests/ -v

   # Run with coverage
   pytest tests/ --cov=pywrfkit --cov-report=html

Documentation
-------------

Build the documentation locally to check for any issues:

.. code-block:: bash

   cd docs
   make html
   # Open _build/html/index.html in your browser

Guidelines
----------

- **Code**: Follow PEP 8 and use Black for formatting
- **Tests**: Add tests for new functionality
- **Documentation**: Update docstrings and documentation
- **Commits**: Use clear, descriptive commit messages
- **Pull Requests**: Provide a clear description of changes

Issue Reporting
--------------

When reporting issues, please include:

- Python version
- Operating system
- PyWRFKit version
- Error messages and tracebacks
- Steps to reproduce the issue

Contact
-------

- **GitHub Issues**: https://github.com/ankurk017/pywrfkit/issues
- **Email**: ankurk017@gmail.com

Thank you for contributing to PyWRFKit! 