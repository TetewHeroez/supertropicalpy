Supertropical Algebra Theory
============================

This page provides mathematical background on supertropical algebra.

What is Supertropical Algebra?
-------------------------------

Supertropical algebra is an algebraic structure that extends tropical algebra
by introducing **ghost elements**. It provides a framework for solving 
optimization problems and has applications in algebraic geometry, phylogenetics,
and computer science.

Basic Definitions
-----------------

Elements
^^^^^^^^

A supertropical semiring contains two types of elements:

- **Tangible elements**: Regular elements, denoted as :math:`a`
- **Ghost elements**: Special elements marked with ν, denoted as :math:`a^\nu`

The **zero element** is :math:`-\infty` (additive identity).

The **one element** is :math:`0` (multiplicative identity).

Operations
^^^^^^^^^^

**Supertropical Addition** (:math:`\oplus`):

.. math::

   a \oplus b = \begin{cases}
   \max(a, b) & \text{if } a \neq b \\
   a^\nu & \text{if } a = b
   \end{cases}

Rules:

1. :math:`a \oplus b = \max(a, b)` when :math:`a \neq b` (tangible result)
2. :math:`a \oplus a = a^\nu` (becomes ghost)
3. :math:`a \oplus a^\nu = a^\nu` (ghost absorbs tangible of same value)
4. :math:`a^\nu \oplus b^\nu = \max(a, b)^\nu` (ghost addition)

**Supertropical Multiplication** (:math:`\odot`):

.. math::

   a \odot b = a + b

Rules:

1. :math:`a \odot b = a + b` (classical addition)
2. :math:`a \odot b^\nu = (a + b)^\nu` (result is ghost if any operand is ghost)
3. :math:`a^\nu \odot b^\nu = (a + b)^\nu`

Properties
^^^^^^^^^^

- **Associativity**: Both :math:`\oplus` and :math:`\odot` are associative
- **Commutativity**: Both operations are commutative
- **Distributivity**: :math:`a \odot (b \oplus c) = (a \odot b) \oplus (a \odot c)`
- **Idempotency**: :math:`a \oplus a = a^\nu` (not strictly idempotent due to ghost)

Matrix Operations
-----------------

Supertropical Matrix Multiplication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Given matrices :math:`A` (size :math:`m \times n`) and :math:`B` (size :math:`n \times p`),
the product :math:`C = A \odot B` is:

.. math::

   C_{ij} = \bigoplus_{k=1}^{n} (A_{ik} \odot B_{kj})

This means:

- For each entry: sum over products (using supertropical operations)
- Products use :math:`\odot` (classical addition)
- Sums use :math:`\oplus` (max operation with ghost rules)

Permanent (Supertropical Determinant)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **permanent** of a square matrix :math:`A` is the supertropical analogue
of the determinant:

.. math::

   \text{per}(A) = \bigoplus_{\pi \in S_n} \bigodot_{i=1}^{n} a_{i,\pi(i)}

where :math:`S_n` is the set of all permutations of :math:`\{1, 2, \ldots, n\}`.

A matrix is **nonsingular** if its permanent is tangible (not ghost).

Linear Systems
--------------

Solving :math:`Ax = b` using Cramer's Rule
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a nonsingular matrix :math:`A` (permanent is tangible), the solution to
:math:`Ax = b` can be found using:

.. math::

   x = \text{adj}(A) \odot b \odot (\text{per}(A))^{-1}

where:

- :math:`\text{adj}(A)` is the adjoint matrix
- :math:`\text{per}(A)` is the permanent
- :math:`(\text{per}(A))^{-1} = -\text{per}(A)` in supertropical algebra

The adjoint matrix :math:`\text{adj}(A)` has entries:

.. math::

   \text{adj}(A)_{ij} = \text{per}(M_{ji})

where :math:`M_{ji}` is the minor obtained by removing row :math:`j` and column :math:`i`.

Example
^^^^^^^

Consider the system:

.. math::

   \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} x = \begin{pmatrix} 5 \\ 4 \end{pmatrix}

1. Calculate permanent: :math:`\text{per}(A) = (2 + 3) \oplus (1 + 1) = 5 \oplus 2 = 5`
2. Calculate adjoint matrix entries using minors
3. Apply Cramer's formula to find :math:`x`

References
----------

- Izhakian, Z., & Rowen, L. (2010). *Supertropical algebra*. Advances in Mathematics.
- Subiono (2022). *Aljabar Min-Max Plus dan Terapannya*. Departemen Matematika ITS, Surabaya, 22 February 2022.

Implementation Notes
--------------------

This package implements the supertropical semiring with:

- **Tangible elements**: Standard numerical values
- **Ghost elements**: Values marked with the ``is_ghost`` flag, displayed with ν
- **Zero element**: Represented as ``-math.inf``
- **Efficient operations**: Using NumPy arrays for matrix computations
