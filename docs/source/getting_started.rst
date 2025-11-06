Getting Started
===============

This guide will help you install and set up the ``supertropicalpy`` package.

Installation
------------

Online Installation (PyPI)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Install the latest stable version from PyPI using pip:

.. code-block:: bash

   pip install supertropicalpy

To install a specific version:

.. code-block:: bash

   pip install supertropicalpy==0.1.2

To upgrade to the latest version:

.. code-block:: bash

   pip install --upgrade supertropicalpy

Offline Installation
^^^^^^^^^^^^^^^^^^^^

If you need to install the package offline (without internet access), follow these steps:

**Step 1: Download the package** (on a machine with internet)

.. code-block:: bash

   # Download the wheel file
   pip download supertropicalpy -d ./packages

**Step 2: Transfer files**

Copy the ``packages`` directory to your offline machine.

**Step 3: Install offline**

.. code-block:: bash

   # Install from the downloaded wheel
   pip install --no-index --find-links=./packages supertropicalpy

Development Installation
^^^^^^^^^^^^^^^^^^^^^^^^

To install the package in development mode from source:

.. code-block:: bash

   # Clone the repository
   git clone https://github.com/TetewHeroez/supertropicalpy.git
   cd supertropicalpy

   # Install in editable mode
   pip install -e .

   # Or with development dependencies
   pip install -e ".[dev]"

Verify Installation
-------------------

After installation, verify that the package is working correctly:

.. code-block:: python

   import supertropical as suptrop

   # Create a simple element
   a = suptrop.Element(5)
   b = suptrop.Element(3)
   
   # Test addition
   result = a + b
   print(f"{a} ⊕ {b} = {result}")

If you see output like ``5.0 ⊕ 3.0 = 5.0``, the installation was successful!

Quick Start
-----------

Here's a minimal example to get you started:

.. code-block:: python

   import supertropical as suptrop

   # Create tangible and ghost elements
   tangible = suptrop.Element(5)
   ghost = suptrop.Element(5, is_ghost=True)
   
   print(f"Tangible: {tangible}")     # 5.0
   print(f"Ghost: {ghost}")            # 5.0ν

   # Supertropical operations
   sum_result = tangible + suptrop.Element(3)   # 5 ⊕ 3 = 5
   prod_result = tangible * suptrop.Element(2)  # 5 ⊗ 2 = 7
   
   print(f"Addition: {sum_result}")
   print(f"Multiplication: {prod_result}")

   # Matrix operations
   A = suptrop.Matrix([[2, 1], [1, 3]])
   b = suptrop.Matrix([[5], [4]])
   
   # Solve linear system A ⊗ x ⊨ b
   x = A.solve(b)
   print(f"Solution:\n{x}")

Import Styles
-------------

The package supports multiple import styles for flexibility:

**Recommended (NumPy-style)**:

.. code-block:: python

   import supertropical as suptrop
   
   element = suptrop.Element(5)
   matrix = suptrop.Matrix([[1, 2], [3, 4]])

**Direct imports**:

.. code-block:: python

   from supertropical import Element, Matrix
   
   element = Element(5)
   matrix = Matrix([[1, 2], [3, 4]])

**Full class names**:

.. code-block:: python

   from supertropical import SupertropicalElement, SupertropicalMatrix
   
   element = SupertropicalElement(5)
   matrix = SupertropicalMatrix([[1, 2], [3, 4]])

Requirements
------------

- Python ≥ 3.9
- NumPy ≥ 1.20.0

Optional dependencies for documentation:

- Sphinx
- nbsphinx
- sphinx-rtd-theme

Next Steps
----------

- :doc:`theory` - Learn the mathematical theory with complete examples
- :doc:`examples/01_supertropical_elements` - Interactive element operations
- :doc:`examples/03_matrices` - Interactive matrix examples
- :doc:`api/index` - Browse the complete API reference

Troubleshooting
---------------

**ImportError: No module named 'supertropical'**

Make sure the package is installed:

.. code-block:: bash

   pip list | grep supertropical

If not found, install it with ``pip install supertropicalpy``.

**NumPy version conflict**

If you encounter NumPy compatibility issues:

.. code-block:: bash

   pip install --upgrade numpy>=1.20.0

**Permission denied during installation**

Use the ``--user`` flag:

.. code-block:: bash

   pip install --user supertropicalpy

Support
-------

- **GitHub Issues**: https://github.com/TetewHeroez/supertropicalpy/issues
- **Documentation**: https://tetewheroez.github.io/supertropicalpy/
- **PyPI Package**: https://pypi.org/project/supertropicalpy/
