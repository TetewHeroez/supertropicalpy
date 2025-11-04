# Advanced Features

This guide covers advanced features of the supertropical-algebra package.

## Element Power Operations

### Basic Power
```python
import supertropical as suptrop

# Positive exponent
a = suptrop.Element(5)
print(a ** 2)   # Output: 10.0 (5 * 2)
print(a ** 3)   # Output: 15.0 (5 * 3)

# Zero exponent
print(a ** 0)   # Output: 0.0 (multiplicative identity)

# Negative exponent (max-plus subtraction)
print(a ** -2)  # Output: -10.0 (5 * -2)
```

### Ghost Element Power
```python
# Ghost element power
c = suptrop.Element(5, is_ghost=True)
print(c ** 2)   # Output: 10.0ν (ghost preserved)
print(c ** -1)  # Output: -5.0ν (ghost preserved)
```

## Ghost Surpasses Relation

The ghost surpasses relation (⊨) is defined as: x ⊨ y if x = y ⊕ z for some z ∈ G₀.

```python
# Create elements
x = suptrop.Element(5, is_ghost=True)  # 5ν
y = suptrop.Element(5)                 # 5

# Check ghost surpasses
print(x.ghost_surpasses(y))  # True: 5ν ⊨ 5

# Tangible does not surpass tangible
a = suptrop.Element(5)
b = suptrop.Element(5)
print(a.ghost_surpasses(b))  # False

# Different values
x = suptrop.Element(7, is_ghost=True)
y = suptrop.Element(5)
print(x.ghost_surpasses(y))  # False (different values)
```

## Matrix Transpose

Get the transpose of a matrix A^T where [A^T]ᵢⱼ = Aⱼᵢ.

```python
# Create matrix
A = suptrop.Matrix([[2, 1, 3],
                    [4, 5, 6]])

# Get transpose
A_T = A.transpose()
print("Original A:")
print(A)
print("\nTranspose A^T:")
print(A_T)

# Output:
# Original A:
# [
#   [2.0  1.0  3.0]
#   [4.0  5.0  6.0]
# ]
#
# Transpose A^T:
# [
#   [2.0  4.0]
#   [1.0  5.0]
#   [3.0  6.0]
# ]
```

## Matrix Power

Compute matrix powers A^k = A * A * ... * A (k times).

```python
# Create square matrix
A = suptrop.Matrix([[2, 1],
                    [1, 3]])

# Matrix squared
A_2 = A ** 2
print("A^2:")
print(A_2)

# Matrix cubed
A_3 = A ** 3
print("\nA^3:")
print(A_3)

# Identity (A^0)
A_0 = A ** 0
print("\nA^0 (Identity):")
print(A_0)
```

## Identity Matrix

Create an n×n identity matrix I where:
- [I]ᵢⱼ = 0 if i = j (multiplicative identity)
- [I]ᵢⱼ = ε = -∞ν (ghost) if i ≠ j

```python
# Create 3×3 identity matrix
I = suptrop.Matrix.identity(3)
print("Identity matrix I:")
print(I)

# Output:
# [
#   [0.0      -infv    -infv  ]
#   [-infv    0.0      -infv  ]
#   [-infv    -infv    0.0    ]
# ]

# Verify: A * I = A
A = suptrop.Matrix([[2, 1],
                    [3, 4]])
I = suptrop.Matrix.identity(2)
result = A * I
print("\nA * I = A:")
print(result)
```

## Pseudo-Zero Matrix

Create an n×n pseudo-zero matrix Z_G where all entries are ε = -∞ν (ghost).

```python
# Create 3×3 pseudo-zero matrix
Z_G = suptrop.Matrix.pseudo_zero(3)
print("Pseudo-zero matrix Z_G:")
print(Z_G)

# Output:
# [
#   [-infv  -infv  -infv]
#   [-infv  -infv  -infv]
#   [-infv  -infv  -infv]
# ]
```

## Pseudo-Inverse

Calculate the pseudo-inverse A^♯ of a matrix.

For a square matrix A:
- If |A| ∈ T (tangible): A^♯ = (1/|A|) ⊗ adj(A)
- If |A| ∈ G₀ (ghost, |A| ≠ ε): A^♯ = (1/|A|)^ν ⊗ adj(A)

where |A| is the permanent and 1/a = -a in supertropical algebra.

```python
# Create matrix
A = suptrop.Matrix([[2, 1],
                    [1, 3]])

# Calculate pseudo-inverse
A_sharp = A.pseudo_inverse()
print("A^♯:")
print(A_sharp)

# Calculate permanent to verify
perm = A.permanent()
print(f"\nPermanent |A|: {perm}")

# Verify property (for tangible permanent)
# A * A^♯ should relate to identity-like behavior
result = A * A_sharp
print("\nA * A^♯:")
print(result)
```

## Complete Example

```python
import supertropical as suptrop

# 1. Element operations
print("=== Element Operations ===")
a = suptrop.Element(5)
print(f"a = {a}")
print(f"a^2 = {a**2}")
print(f"a^-1 = {a**-1}")

# 2. Ghost surpasses
print("\n=== Ghost Surpasses ===")
x = suptrop.Element(5, is_ghost=True)
y = suptrop.Element(5)
print(f"x = {x}, y = {y}")
print(f"x ⊨ y: {x.ghost_surpasses(y)}")

# 3. Matrix operations
print("\n=== Matrix Operations ===")
A = suptrop.Matrix([[2, 1],
                    [1, 3]])
print(f"A:\n{A}")
print(f"\nA^T:\n{A.transpose()}")
print(f"\nA^2:\n{A ** 2}")

# 4. Special matrices
print("\n=== Special Matrices ===")
I = suptrop.Matrix.identity(2)
print(f"Identity I:\n{I}")

Z_G = suptrop.Matrix.pseudo_zero(2)
print(f"\nPseudo-zero Z_G:\n{Z_G}")

# 5. Pseudo-inverse
print("\n=== Pseudo-Inverse ===")
A_sharp = A.pseudo_inverse()
print(f"A^♯:\n{A_sharp}")
```

## Mathematical Properties

### Element Power Properties
- **Positive exponent**: a^k = k ⊙ a (k times multiplication)
- **Zero exponent**: a^0 = 0 (multiplicative identity)
- **Negative exponent**: a^(-k) = (-k) ⊙ a (subtraction in max-plus)
- **Ghost preservation**: If a is ghost, a^k is also ghost

### Matrix Power Properties
- **A^0 = I** (identity matrix)
- **A^(k+m) = A^k * A^m**
- **Ghost elements preserved** through matrix operations

### Pseudo-Inverse Properties
- Defined only for square matrices
- Requires |A| ≠ ε (permanent not epsilon)
- Generalizes matrix inversion in supertropical algebra
- A * A^♯ relates to pseudo-identity behavior

## References

For theoretical background, see:
- Izhakian, Z., & Rowen, L. (2010). *Supertropical algebra*. Advances in Mathematics.
- Subiono (2022). *Aljabar Min-Max Plus dan Terapannya*. Departemen Matematika ITS, Surabaya.
