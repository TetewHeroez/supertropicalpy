What is Supertropical Algebra?
============================

Supertropical algebra is an algebraic structure that extends tropical algebra
by introducing **ghost elements**. It provides a framework for solving 
optimization problems and has applications in algebraic geometry, phylogenetics,
and computer science.
This page provides comprehensive mathematical background on supertropical algebra, based on the extended semiring tropical framework.

1. Supertropical Algebra
------------------------

1.1 Extended Semiring Tropical
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As discussed in max-plus algebra, the tropical algebra structure lacks an inverse element for the addition operation Γèò. This limitation is specifically addressed by introducing the **extended semiring tropical** structure, allowing us to solve systems of linear equations.

Definition 1.1 (Extended Semiring Tropical)
""""""""""""""""""""""""""""""""""""""""""""

An **extended semiring tropical** is defined as :math:`(T, \oplus, \otimes)` where :math:`T = \mathbb{R} \cup \{-\infty\} \cup \mathbb{R}^\nu`, where :math:`\mathbb{R}` is the set of all real numbers and :math:`\mathbb{R}^\nu = \{a^\nu \mid a \in \mathbb{R}\}`.

- The **neutral element** for :math:`T` is :math:`\varepsilon \stackrel{\text{def}}{=} -\infty`
- The **unit element** is :math:`e \stackrel{\text{def}}{=} 0`

The set :math:`\mathbb{R}_{-\infty} = \mathbb{R} \cup \{-\infty\}` represents the **ideal** of :math:`T`, called the **ideal ghost**. 

Meanwhile, a function :math:`v : T \to \mathbb{R}_{-\infty}` defined by :math:`v(x) \stackrel{\text{def}}{=} x, \forall x \in \mathbb{R}_{-\infty}` represents **tangible identity**, and :math:`v(a) = a^\nu, \forall a \in \mathbb{R}` where element :math:`a^\nu` is called the **element ghost** or **ghost** of :math:`a`. The function :math:`v` is called the **ghost mapping**.

Definition 1.2 (Extended Semiring Tropical Order)
""""""""""""""""""""""""""""""""""""""""""""""""""

Given an **extended semiring tropical** :math:`T`, a **partial order** relation :math:`\prec` is defined on :math:`T` as follows:

For any :math:`a, b \in \mathbb{R}`, :math:`a^\nu, b^\nu \in \mathbb{R}^\nu` and :math:`x \in T`:

1. :math:`-\infty \prec x, \forall x \in T \setminus \{-\infty\}`
2. For any real numbers :math:`a \prec b`, then :math:`a \prec a^\nu, a \prec b^\nu, a^\nu \prec b`, and :math:`a^\nu \prec b^\nu`
3. :math:`a \prec a^\nu` for any :math:`a \in \mathbb{R}`

Axiom 1.1 (Extended Semiring Tropical Operations)
""""""""""""""""""""""""""""""""""""""""""""""""""

Given an extended semiring tropical :math:`T`, the operations :math:`\oplus` (max) and :math:`\otimes` (addition) on :math:`T` satisfy the following axioms.

For any :math:`a, b \in \mathbb{R}`, :math:`a^\nu, b^\nu \in \mathbb{R}^\nu` and :math:`x, y \in T`:

1. :math:`-\infty \oplus x = x \oplus -\infty = x, \forall x \in T`
2. :math:`x \oplus y = \max_{\prec} \{x, y\}` provided :math:`x \neq y`
3. :math:`a \oplus a = a^\nu \oplus a^\nu = a \oplus a^\nu = a^\nu \oplus a = a^\nu`
4. :math:`-\infty \otimes x = x \otimes -\infty = -\infty`
5. :math:`a \otimes b = a + b` (classical addition)
6. :math:`a^\nu \otimes b = a \otimes b^\nu = a^\nu \otimes b^\nu = (a + b)^\nu`

**Example 1.1**: Operations in extended semiring tropical :math:`T`:

1. :math:`-\infty \oplus 4 = 4 \oplus -\infty = 4`
2. :math:`-2 \oplus 7 = \max_{\prec} \{-2, 7\} = 7`
3. :math:`8 \oplus 8 = 8^\nu \oplus 8^\nu = 8 \oplus 8^\nu = 8^\nu \oplus 8 = 8^\nu`
4. :math:`-\infty \otimes 3 = 3 \otimes -\infty = -\infty`
5. :math:`6 \otimes 9 = 6 + 9 = 15`
6. :math:`7^\nu \otimes 8 = 7 \otimes 8^\nu = 7^\nu \otimes 8^\nu = (7 + 8)^\nu = 15^\nu`

2. Ghost Surpasses Relation
----------------------------

2.1 Definition
^^^^^^^^^^^^^^

In supertropical semiring :math:`R`, for any :math:`a \in R`, then :math:`a \oplus a = -\infty` only holds when :math:`a = -\infty`. However, for any :math:`a \in T` then :math:`a \oplus a = a^\nu` and for any :math:`x \in G` then :math:`x \oplus x = x`. Therefore, a **ghost surpasses** relation in :math:`R` will be introduced as follows.

Definition 2.1 (Ghost Surpasses Relation)
""""""""""""""""""""""""""""""""""""""""""

Given a supertropical semiring :math:`R`, a relation :math:`\vDash` is called a **ghost surpasses** relation in :math:`R` defined as:

.. math::

   x \vDash y \quad \text{if} \quad x = y \oplus z \quad \text{for some} \quad z \in \mathcal{G}_0

where :math:`\mathcal{G}_0` is the set of ghost elements.

**Example 2.1**: Ghost surpasses relation in supertropical semiring :math:`R`:

1. For :math:`9, 10^\nu \in R`, we have :math:`10^\nu \vDash 9` because :math:`10^\nu = 9 \oplus 10^\nu`. Here, :math:`z = 10^\nu` is a value in :math:`\mathcal{G}_0` satisfying :math:`10^\nu = 9 \oplus 10^\nu`.

2. For :math:`-5 \in R`, we have :math:`-5 \vDash -5` because :math:`-5 = -5 \oplus \varepsilon`. Here, :math:`z = \varepsilon \in \mathcal{G}_0` with :math:`z \neq \varepsilon` satisfying :math:`-5 = -5 \oplus z` is :math:`z \prec -5`. For example, :math:`z = -6^\nu` and :math:`z = -7.5^\nu`. Notice that there are many values of :math:`z \in \mathcal{G}_0` satisfying :math:`-5 = -5 \oplus z` other than :math:`z \prec -5`.

3. Meanwhile, for :math:`7, 6 \in R`, we have :math:`7 \nvDash 6` because the value of :math:`z` satisfying :math:`7 = 6 \oplus z` is only :math:`z = 7 \notin \mathcal{G}_0`.

3. Supertropical Matrices
--------------------------

3.1 Matrix Operations
^^^^^^^^^^^^^^^^^^^^^

The set of all :math:`m \times n` matrices over supertropical semiring is denoted as :math:`M_{m \times n}(R)`, where matrix elements are members of :math:`R`. When the dimension of a matrix is square, denoted as :math:`M_n(R)`, the binary operations ⊕ and ⊗ in :math:`R` can be extended to matrix operations in :math:`M_n(R)`. Furthermore, the ghost surpasses relation in :math:`R` can also be extended to matrices in :math:`M_n(R)`.

If :math:`A \vDash B` then :math:`a_{i,j} \vDash b_{i,j}` for any :math:`i` and :math:`j` in :math:`\underline{n}`.

**Matrix Addition**

For matrices :math:`A, B \in M_{m \times n}(R)`, the addition :math:`A \oplus B` is defined as:

.. math::

   [A \oplus B]_{i,j} = a_{i,j} \oplus b_{i,j}

for :math:`i \in \underline{m}` and :math:`j \in \underline{n}`.

**Example 3.1**: Given matrices

.. math::

   A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}, \quad B = \begin{pmatrix} 5 & 4^\nu \\ 2 & 1 \end{pmatrix}

Then:

.. math::

   A \oplus B = \begin{pmatrix} 2 \oplus 5 & 1 \oplus 4^\nu \\ 1 \oplus 2 & 3 \oplus 1 \end{pmatrix} = \begin{pmatrix} 5 & 4^\nu \\ 2 & 3 \end{pmatrix}

**Matrix Multiplication**

For matrix :math:`A \in M_{m \times p}(R)` and :math:`B \in M_{p \times n}(R)`, the multiplication :math:`A \otimes B` is defined as:

.. math::

   [A \otimes B]_{i,j} = \bigoplus_{k=1}^{p} a_{i,k} \otimes b_{k,j}

for :math:`i \in \underline{m}` and :math:`j \in \underline{n}`.

**Example 3.2**: Using the same matrices :math:`A` and :math:`B` from Example 3.1:

.. math::

   A \otimes B = \begin{pmatrix} 
   (2 \otimes 5) \oplus (1 \otimes 2) & (2 \otimes 4^\nu) \oplus (1 \otimes 1) \\
   (1 \otimes 5) \oplus (3 \otimes 2) & (1 \otimes 4^\nu) \oplus (3 \otimes 1)
   \end{pmatrix}

.. math::

   = \begin{pmatrix} 
   7 \oplus 3 & 6^\nu \oplus 2 \\
   6 \oplus 5 & 5^\nu \oplus 4
   \end{pmatrix} = \begin{pmatrix} 
   7 & 6^\nu \\
   6 & 5^\nu
   \end{pmatrix}

3.2 Advanced Matrix Operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Matrix Transpose**

For any matrix :math:`A \in M_{m \times n}(R)`, its transpose :math:`A^T \in M_{n \times m}(R)` is defined by:

.. math::

   [A^T]_{i,j} = a_{j,i}

where :math:`i \in \underline{n}` and :math:`j \in \underline{m}`.

**Example 3.3**: For the matrix

.. math::

   A = \begin{pmatrix} 2 & 1 & 5^\nu \\ 3 & 4 & 1 \end{pmatrix}

The transpose is:

.. math::

   A^T = \begin{pmatrix} 2 & 3 \\ 1 & 4 \\ 5^\nu & 1 \end{pmatrix}

**Matrix Power**

For any square matrix :math:`A \in M_n(R)` and positive integer :math:`k`, the power :math:`A^k` is defined recursively:

.. math::

   A^1 = A, \quad A^k = A^{k-1} \otimes A

**Example 3.4**: For the matrix

.. math::

   A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}

We can compute:

.. math::

   A^2 = A \otimes A = \begin{pmatrix} 
   (1 \otimes 1) \oplus (2 \otimes 0) & (1 \otimes 2) \oplus (2 \otimes 1) \\
   (0 \otimes 1) \oplus (1 \otimes 0) & (0 \otimes 2) \oplus (1 \otimes 1)
   \end{pmatrix}

.. math::

   = \begin{pmatrix} 
   1 \oplus (-\infty) & 3 \oplus 3 \\
   (-\infty) \oplus (-\infty) & (-\infty) \oplus 1
   \end{pmatrix} = \begin{pmatrix} 
   1 & 3 \\
   -\infty & 1
   \end{pmatrix}

**Identity Matrix**

The identity matrix :math:`I_n \in M_n(R)` is defined as:

.. math::

   [I_n]_{i,j} = \begin{cases}
   0 & \text{if } i = j \\
   -\infty & \text{if } i \neq j
   \end{cases}

It satisfies :math:`A \otimes I_n = I_n \otimes A = A` for any :math:`A \in M_n(R)`.

3.3 Permanent (Supertropical Determinant)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **permanent** of a square matrix :math:`A \in M_n(R)` is defined as:

.. math::

   \text{per}(A) = \bigoplus_{\sigma \in S_n} \bigotimes_{i=1}^{n} a_{i,\sigma(i)}

where :math:`S_n` is the set of all permutations of :math:`\{1, 2, \ldots, n\}`.

**Example 3.5**: For a :math:`2 \times 2` matrix

.. math::

   A = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}

The permanent is:

.. math::

   \text{per}(A) = (3 \otimes 4) \oplus (1 \otimes 2) = 7 \oplus 3 = 7

For a :math:`3 \times 3` matrix

.. math::

   B = \begin{pmatrix} 1 & 2 & 0 \\ 2 & 1 & 3 \\ 1 & 0 & 2 \end{pmatrix}

We compute over all 6 permutations:

1. :math:`(1,2,3) \to 1 \otimes 1 \otimes 2 = 4`
2. :math:`(1,3,2) \to 1 \otimes 3 \otimes 0 = 4`
3. :math:`(2,1,3) \to 2 \otimes 2 \otimes 2 = 6`
4. :math:`(2,3,1) \to 2 \otimes 3 \otimes 1 = 6`
5. :math:`(3,1,2) \to 0 \otimes 2 \otimes 0 = 2`
6. :math:`(3,2,1) \to 0 \otimes 1 \otimes 1 = 2`

Therefore :math:`\text{per}(B) = 4 \oplus 4 \oplus 6 \oplus 6 \oplus 2 \oplus 2 = 6`.

3.4 Adjoint Matrix and Pseudo-Inverse
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The **adjoint matrix** :math:`\text{adj}(A)` of a matrix :math:`A \in M_n(R)` is defined by:

.. math::

   [\text{adj}(A)]_{i,j} = \text{per}(M_{j,i})

where :math:`M_{j,i}` is the :math:`(n-1) \times (n-1)` minor obtained by deleting row :math:`j` and column :math:`i` from :math:`A`.

The **pseudo-inverse** or **weak inverse** :math:`A^\nabla` is defined as:

.. math::

   A^\nabla = \text{adj}(A) \otimes (\text{per}(A))^{-1}

where :math:`(\text{per}(A))^{-1} = -\text{per}(A)` in supertropical algebra.

**Example 3.6**: For the matrix

.. math::

   A = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}

We have :math:`\text{per}(A) = 7` (from Example 3.5).

The minors are:

- :math:`M_{1,1} = (4)`, so :math:`\text{per}(M_{1,1}) = 4`
- :math:`M_{1,2} = (2)`, so :math:`\text{per}(M_{1,2}) = 2`
- :math:`M_{2,1} = (1)`, so :math:`\text{per}(M_{2,1}) = 1`
- :math:`M_{2,2} = (3)`, so :math:`\text{per}(M_{2,2}) = 3`

Therefore:

.. math::

   \text{adj}(A) = \begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix}

The pseudo-inverse is:

.. math::

   A^\nabla = \text{adj}(A) \otimes (-7) = \begin{pmatrix} 4 + (-7) & 2 + (-7) \\ 1 + (-7) & 3 + (-7) \end{pmatrix} = \begin{pmatrix} -3 & -5 \\ -6 & -4 \end{pmatrix}

4. Linear Systems over Supertropical Algebra
---------------------------------------------

4.1 Homogeneous and Non-Homogeneous Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As in ordinary linear algebra, linear systems over supertropical algebra can be classified into **homogeneous systems** and **non-homogeneous systems**. In supertropical algebra, the **ghost surpasses relation** will be used instead of the equality relation :math:`=`.

A homogeneous linear system over supertropical algebra is stated as :math:`A \otimes x \vDash b`. Meanwhile, if :math:`b = \mathcal{E}` where :math:`\mathcal{E}` is a vector whose elements are all :math:`\varepsilon`, then the system :math:`A \otimes x \vDash \mathcal{E}` is called a **homogeneous system** over supertropical algebra.

4.2 Solution Analysis
^^^^^^^^^^^^^^^^^^^^^

As has been explained in max-plus algebra theory, the max-plus algebra structure :math:`\mathbb{R}_{\max} = (\mathbb{R}_{\varepsilon}, \oplus, \otimes)` lacks inverse elements for the :math:`\oplus` operation. In other words, if :math:`a \in \mathbb{R}_{\varepsilon}`, there does not exist :math:`x \in \mathbb{R}_{\varepsilon}` satisfying :math:`a \oplus x = \varepsilon` if and only if :math:`a = \varepsilon`. This limitation makes it difficult to directly solve homogeneous linear systems :math:`A \otimes x = b` in :math:`\mathbb{R}_{\max}`.

As a motivation from the discussion of homogeneous systems in :math:`\mathbb{R}_{\max}`, the solution for non-homogeneous linear systems :math:`A \otimes x \vDash b` will be provided.

4.3 Cramer's Rule
^^^^^^^^^^^^^^^^^

The solution to the system :math:`A \otimes x \vDash b` can be found using **Cramer's rule** in supertropical algebra:

.. math::

   x = \text{adj}(A) \otimes b \otimes (\text{per}(A))^{-1}

where:

- :math:`\text{per}(A)` is the **permanent** (supertropical determinant)
- :math:`\text{adj}(A)` is the **adjoint matrix**
- :math:`(\text{per}(A))^{-1} = -\text{per}(A)` in supertropical algebra

The matrix is **nonsingular** (has unique solution) if :math:`\text{per}(A)` is **tangible** (not ghost).

**Example 4.1**: Solve the system :math:`A \otimes x \vDash b` where

.. math::

   A = \begin{pmatrix} 2 & 3 \\ 1 & 4 \end{pmatrix}, \quad b = \begin{pmatrix} 8 \\ 7 \end{pmatrix}

**Step 1**: Compute the permanent

.. math::

   \text{per}(A) = (2 \otimes 4) \oplus (3 \otimes 1) = 6 \oplus 4 = 6

Since :math:`\text{per}(A) = 6` is tangible, the system has a unique solution.

**Step 2**: Compute the adjoint matrix

The minors are:

- :math:`M_{1,1} = (4)`, so :math:`\text{per}(M_{1,1}) = 4`
- :math:`M_{1,2} = (1)`, so :math:`\text{per}(M_{1,2}) = 1`
- :math:`M_{2,1} = (3)`, so :math:`\text{per}(M_{2,1}) = 3`
- :math:`M_{2,2} = (2)`, so :math:`\text{per}(M_{2,2}) = 2`

Therefore:

.. math::

   \text{adj}(A) = \begin{pmatrix} 4 & 1 \\ 3 & 2 \end{pmatrix}

**Step 3**: Apply Cramer's rule

.. math::

   x = \text{adj}(A) \otimes b \otimes (-\text{per}(A)) = \begin{pmatrix} 4 & 1 \\ 3 & 2 \end{pmatrix} \otimes \begin{pmatrix} 8 \\ 7 \end{pmatrix} \otimes (-6)

First compute :math:`\text{adj}(A) \otimes b`:

.. math::

   \text{adj}(A) \otimes b = \begin{pmatrix} (4 \otimes 8) \oplus (1 \otimes 7) \\ (3 \otimes 8) \oplus (2 \otimes 7) \end{pmatrix} = \begin{pmatrix} 12 \oplus 8 \\ 11 \oplus 9 \end{pmatrix} = \begin{pmatrix} 12 \\ 11 \end{pmatrix}

Then multiply by :math:`-6`:

.. math::

   x = \begin{pmatrix} 12 + (-6) \\ 11 + (-6) \end{pmatrix} = \begin{pmatrix} 6 \\ 5 \end{pmatrix}

**Step 4**: Verify the solution

.. math::

   A \otimes x = \begin{pmatrix} 2 & 3 \\ 1 & 4 \end{pmatrix} \otimes \begin{pmatrix} 6 \\ 5 \end{pmatrix} = \begin{pmatrix} (2 \otimes 6) \oplus (3 \otimes 5) \\ (1 \otimes 6) \oplus (4 \otimes 5) \end{pmatrix}

.. math::

   = \begin{pmatrix} 8 \oplus 8 \\ 7 \oplus 9 \end{pmatrix} = \begin{pmatrix} 8^\nu \\ 9 \end{pmatrix}

We check: :math:`8^\nu \vDash 8` ✓ and :math:`9 \vDash 7` ✓ (since :math:`9 > 7`).

Therefore :math:`x = \begin{pmatrix} 6 \\ 5 \end{pmatrix}` is indeed a solution.

References
----------

- Izhakian, Z., & Rowen, L. (2010). *Supertropical algebra*. Advances in Mathematics.
- Subiono (2022). *Aljabar Min-Max Plus dan Terapannya*. Departemen Matematika ITS, Surabaya, 22 February 2022.

Implementation Notes
--------------------

This package implements the supertropical semiring with:

- **Tangible elements**: Standard numerical values
- **Ghost elements**: Values marked with the ``is_ghost`` flag, displayed with ╬╜
- **Zero element**: Represented as ``-math.inf``
- **Efficient operations**: Using NumPy arrays for matrix computations