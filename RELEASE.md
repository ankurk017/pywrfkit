# Release Guide

This document explains the automated release process for PyWRFKit.

## Automated Release Process

PyWRFKit uses GitHub Actions to automatically publish releases to PyPI and GitHub when you push a version tag.

### Prerequisites

1. **PyPI API Token**: You need a PyPI API token for automated publishing
   - Go to https://pypi.org/manage/account/token/
   - Create a new token with "Entire project" scope
   - Add it to your GitHub repository secrets as `PYPI_API_TOKEN`

### Release Steps

1. **Ensure you're on the main branch**:
   ```bash
   git checkout main
   git pull origin main
   ```

2. **Update version numbers** in these files:
   - `pyproject.toml` - Update `version = "0.1.2"`
   - `setup.py` - Update `version="0.1.2"`
   - `pywrfkit/__init__.py` - Update `__version__ = "0.1.2"`

3. **Commit version changes**:
   ```bash
   git add .
   git commit -m "Bump version to 0.1.2"
   git push origin main
   ```

4. **Create and push a version tag**:
   ```bash
   git tag -a v0.1.2 -m "Release v0.1.2: description of changes"
   git push origin v0.1.2
   ```

5. **GitHub Actions will automatically**:
   - ✅ Build the package
   - ✅ Run tests across Python versions
   - ✅ Publish to PyPI
   - ✅ Create a GitHub release with release notes
   - ✅ Upload distribution files to the release

### What Happens Automatically

When you push a version tag (e.g., `v0.1.2`):

1. **Build Process**:
   - Creates source distribution (`.tar.gz`)
   - Creates wheel distribution (`.whl`)
   - Validates package structure

2. **Testing**:
   - Runs tests on Python 3.8, 3.9, 3.10, 3.11
   - Ensures package can be imported
   - Validates all dependencies

3. **Publishing**:
   - Uploads to PyPI (https://pypi.org/project/pywrfkit/)
   - Creates GitHub release with auto-generated notes
   - Attaches distribution files to release

4. **Notification**:
   - You'll receive email notifications
   - Release will be visible on GitHub releases page

### Version Numbering

Follow [Semantic Versioning](https://semver.org/):
- **MAJOR.MINOR.PATCH** (e.g., 1.0.0, 1.1.0, 1.1.1)
- **MAJOR**: Breaking changes
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes, backward compatible

### Example Release

```bash
# Update version to 0.1.2
git checkout main
git pull origin main

# Edit version files (pyproject.toml, setup.py, __init__.py)
# ... edit files ...

# Commit and push
git add .
git commit -m "Bump version to 0.1.2"
git push origin main

# Create and push tag
git tag -a v0.1.2 -m "Release v0.1.2: Add new coordinate transformation features"
git push origin v0.1.2

# 🎉 GitHub Actions will handle the rest!
```

### Troubleshooting

If the automated release fails:

1. **Check GitHub Actions logs** for error details
2. **Verify PyPI token** is correctly set in repository secrets
3. **Ensure version consistency** across all files
4. **Check for test failures** that might prevent release

### Manual Release (Fallback)

If automated release fails, you can manually release:

```bash
# Build locally
python -m build

# Upload to PyPI
twine upload dist/*

# Create GitHub release manually
```

For questions about releases, contact ankurk017@gmail.com 