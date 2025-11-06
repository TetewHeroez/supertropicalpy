# Publishing to PyPI - Setup Guide

This guide explains how to publish `SupertropicalPy` to PyPI (Python Package Index).

## Prerequisites

1. **PyPI Account**: Create account at https://pypi.org/account/register/
2. **GitHub Repository**: Already done ✅

## Setup Steps

### 1. Configure PyPI Trusted Publishing

This is the **modern, secure way** - no API tokens needed!

1. Go to https://pypi.org/ and login
2. Go to your account settings → "Publishing" section
3. Click "Add a new pending publisher"
4. Fill in:

   - **PyPI Project Name**: `SupertropicalPy`
   - **Owner**: `TetewHeroez`
   - **Repository name**: `SupertropicalPy`
   - **Workflow name**: `publish-to-pypi.yml`
   - **Environment name**: `pypi`

5. Click "Add"

### 2. Create GitHub Environment

1. Go to your GitHub repo: https://github.com/TetewHeroez/SupertropicalPy
2. Settings → Environments → "New environment"
3. Name: `pypi`
4. (Optional) Add protection rules:

   - ✅ Required reviewers (add yourself)
   - ✅ Wait timer: 0 minutes

5. Save

### 3. Create a Release (First Publish)

#### Option A: Via GitHub UI (Recommended)

1. Go to https://github.com/TetewHeroez/SupertropicalPy/releases
2. Click "Create a new release"
3. Click "Choose a tag" → Type `v0.1.0` → "Create new tag"
4. Release title: `v0.1.0 - Initial Release`
5. Description:

   ```
   ## 🎉 First Release!

   Initial release of SupertropicalPy package.

   ### Features
   - ✅ Supertropical elements (tangible and ghost)
   - ✅ Addition (⊕) and multiplication (⊙) operations
   - ✅ Matrix operations with permanent calculation
   - ✅ Linear system solver using Cramer's rule
   - ✅ Comprehensive documentation
   ```

6. Click "Publish release"

#### Option B: Via Git Command Line

```bash
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0
```

Then create release on GitHub from the tag.

### 4. Verify Publication

After creating the release:

1. GitHub Actions will automatically run
2. Check https://github.com/TetewHeroez/SupertropicalPy/actions
3. Wait for "Publish to PyPI" workflow to complete (green ✓)
4. Your package will be available at: https://pypi.org/project/SupertropicalPy/

### 5. Install Your Package

After successful publish:

```bash
pip install SupertropicalPy
```

## Future Updates

To publish new versions:

1. Update version in `pyproject.toml`:

   ```toml
   version = "0.1.1"  # or 0.2.0, 1.0.0, etc.
   ```

2. Commit and push:

   ```bash
   git add pyproject.toml
   git commit -m "Bump version to 0.1.2"
   git push
   ```

3. Create new release:

   ```bash
   git tag -a v0.1.1 -m "Release version 0.1.2"
   git push origin v0.1.1
   ```

   Then create GitHub release from the tag.

4. GitHub Actions will automatically publish to PyPI!

## Manual Publishing (Alternative)

If you prefer manual publishing:

1. Install build tools:

   ```bash
   pip install build twine
   ```

2. Build package:

   ```bash
   python -m build
   ```

3. Upload to PyPI:
   ```bash
   twine upload dist/*
   ```

## Troubleshooting

### "Project name already exists"

- Choose a different name in `pyproject.toml`
- Try: `supertropical-algebra-math`, `supertropical-lib`, etc.

### "Invalid or non-existent authentication"

- Make sure you configured Trusted Publishing on PyPI
- Check environment name matches (`pypi`)
- Verify workflow name is correct (`publish-to-pypi.yml`)

### "Permission denied"

- Add `id-token: write` permission in workflow (already done ✅)
- Check GitHub environment protection rules

## Files Created

- ✅ `.github/workflows/publish-to-pypi.yml` - Publishing workflow
- ✅ `MANIFEST.in` - Specifies which files to include in distribution
- ✅ Updated `pyproject.toml` with correct author info

## Next Steps

1. **Register on PyPI** if you haven't
2. **Setup Trusted Publishing** (steps above)
3. **Create first release** (v0.1.0)
4. **Celebrate!** 🎉

Your package will be installable worldwide via:

```bash
pip install SupertropicalPy
```
