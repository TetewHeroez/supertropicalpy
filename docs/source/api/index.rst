API Reference
=============

This section contains the complete API documentation for the SupertropicalPy package.

Core Classes
------------

SupertropicalElement
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: supertropical.SupertropicalElement
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__, __add__, __mul__, __str__, __repr__, __eq__, __lt__

SupertropicalMatrix
^^^^^^^^^^^^^^^^^^^

.. autoclass:: supertropical.SupertropicalMatrix
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__, __matmul__, __mul__, __getitem__, __repr__

Quick Reference
---------------

Element Operations
^^^^^^^^^^^^^^^^^^

Creating Elements:

.. code-block:: python

   from supertropical import SupertropicalElement
   
   a = SupertropicalElement(5)           # Tangible: 5.0
   b = SupertropicalElement(3, True)     # Ghost: 3.0ν
   zero = SupertropicalElement(float('-inf'))  # Zero element

Arithmetic:

.. code-block:: python

   c = a + b   # Supertropical addition (⊕)
   d = a * b   # Supertropical multiplication (⊙)
   
   # Also works with Python numbers
   e = a + 7   # Automatically converts 7 to SupertropicalElement
   f = 2 * a   # Right multiplication

Comparison:

.. code-block:: python

   a == b      # Equality check
   a < b       # Less than (by value, then tangible < ghost)
   a.is_tangible()  # Check if tangible
   a.is_ghost  # Check if ghost (attribute)

Matrix Operations
^^^^^^^^^^^^^^^^^

Creating Matrices:

.. code-block:: python

   from supertropical import SupertropicalMatrix
   
   # From list of lists
   A = SupertropicalMatrix([[1, 2], [3, 4]])
   
   # From SupertropicalElement objects
   e1 = SupertropicalElement(5)
   e2 = SupertropicalElement(3, True)
   B = SupertropicalMatrix([[e1, e2], [e2, e1]])

Matrix Arithmetic:

.. code-block:: python

   C = A * B              # Matrix multiplication
   D = A * scalar         # Scalar multiplication (same operator!)
   
   perm = A.permanent()   # Permanent (supertropical determinant)
   adj = A.adjoint()      # Adjoint matrix

Solving Linear Systems:

.. code-block:: python

   # Solve Ax = b
   A = SupertropicalMatrix([[2, 1], [1, 3]])
   b = SupertropicalMatrix([[5], [4]])
   x = A.solve(b)
   
   print(f"Solution: {x}")

Advanced Operations:

.. code-block:: python

   # Get matrix minor (remove row i, column j)
   minor = A.get_minor(0, 1)
   
   # Access elements
   element = A[0, 1]  # Get element at row 0, col 1
   
   # Matrix properties
   shape = A.shape    # Get dimensions (rows, cols)
