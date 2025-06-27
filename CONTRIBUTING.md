# Contributing to PyWRFKit

Thank you for your interest in contributing to PyWRFKit! This document provides guidelines for contributing to the project.

## Development Workflow

### Branch Structure

- **`dev`** - Development branch (default branch for new features)
- **`main`** - Production branch (stable releases)

### Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/pywrfkit.git
   cd pywrfkit
   ```

3. **Set up the development environment**:
   ```bash
   pip install -e .
   pip install -e .[dev]  # Install development dependencies
   ```

4. **Create a feature branch** from `dev`:
   ```bash
   git checkout dev
   git pull origin dev
   git checkout -b feature/your-feature-name
   ```

### Development Process

1. **Make your changes** and add tests
2. **Run tests** locally:
   ```bash
   pytest tests/ -v
   ```

3. **Commit your changes** with descriptive messages:
   ```bash
   git add .
   git commit -m "Add feature: brief description"
   ```

4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request** from your feature branch to the `dev` branch

### Release Process

When ready for a release:

1. **Merge to main** from `dev`:
   ```bash
   git checkout main
   git merge dev
   ```

2. **Update version** in:
   - `pyproject.toml`
   - `setup.py`
   - `pywrfkit/__init__.py`

3. **Create and push a version tag**:
   ```bash
   git tag -a v0.1.2 -m "Release v0.1.2: description"
   git push origin v0.1.2
   ```

4. **GitHub Actions will automatically**:
   - Build the package
   - Run tests
   - Publish to PyPI
   - Create a GitHub release

### Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to all public functions
- Include type hints where appropriate

### Testing

- Write tests for new functionality
- Ensure all tests pass before submitting PR
- Tests should be in the `tests/` directory

### Documentation

- Update README.md if adding new features
- Add docstrings to new functions
- Update examples if API changes

## Questions?

If you have questions about contributing, please:
- Open an issue on GitHub
- Contact the maintainer at ankurk017@gmail.com

Thank you for contributing to PyWRFKit! 🚀 