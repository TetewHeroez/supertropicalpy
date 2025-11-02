# Supertropical Algebra

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/TetewHeroez/supertropical-algebra/main?filepath=docs/source/examples/tutorial.ipynb)

A comprehensive Python package for **supertropical algebra**, featuring tangible and ghost elements, matrix operations, and linear system solving using Cramer's rule.

> **🚀 Try it now!** Click the Binder badge above to run the interactive tutorial in your browser without installing anything. A comprehensive Python package for **supertropical algebra**, featuring tangible and ghost elements, matrix operations, and linear system solving using Cramer's rule.

## ✨ Features

- **🎯 Tangible & Ghost Elements**: Full support for both element types with automatic conversion

- **🧮 Supertropical Operations**: Addition $\oplus$ defined by $a\oplus b=\max\{a,b\}$ (with ghost rules), and multiplication $\odot$ defined by $a\odot b=a+b$.

- **📐 Matrix Operations**: Matrix multiplication, permanent (supertropical determinant), adjoint.

- **🔧 Linear System Solver**: Cramer's rule implementation for solving $Ax = b$

- **🚀 NumPy Integration**: Efficient computations using NumPy arrays

- **📚 Comprehensive Documentation**: Full API reference, theory guide, and interactive tutorials

- **✅ Type Safety**: Automatic type coercion and validation

## 📦 Installation

```bash
pip install supertropical-algebra
```

Or install from source:

```bash

git clone https://github.com/TetewHeroez/supertropical-algebra.git

cd supertropical-algebra

pip install -e .

```

## 🚀 Quick Start

### Creating Elements

```python
import supertropical as suptrop

# Tangible elements (regular)

a = suptrop.Element(5)

b = suptrop.Element(3)

# Ghost elements (marked with ν)

c = suptrop.Element(5, is_ghost=True)

print(a)  # Output: 5.0

print(c)  # Output: 5.0ν
```

**Alternative:** You can also import directly:

```python
from supertropical import Element, Matrix

a = Element(5)
```

### Supertropical Arithmetic

```python
import supertropical as suptrop

a = suptrop.Element(5)  # Tangible elements (regular)

b = suptrop.Element(3)

c = suptrop.Element(5, is_ghost=True) # Ghost elements (marked with ν)

# Addition (⊕): max operation with ghost rules

result1 = a + b  # 5 ⊕ 3 = 5 (max)

result2 = a + a  # 5 ⊕ 5 = 5ν (becomes ghost)

a = suptrop.Element(5)

# Multiplication (⊙): classical addition

result3 = a * b  # 5 ⊙ 3 = 8 (5 + 3)b = suptrop.Element(3)

result4 = a * c  # 5 ⊙ 5ν = 10ν (result is ghost)

# Works with Python numbers

result5 = a + 7  # Automatic conversion

result6 = 2 * a  # 2 ⊙ 5 = 7

```

### Create matrices

```python
A = suptrop.Matrix([[2, 1],
                    [1, 3]])

B = suptrop.Matrix([[5, 4],
                    [2, 1]])
```

### Matrix Operations

```python
scalar = suptrop.Element(5)

C = A * B              # Matrix multiplication
D = scalar * A         # Scalar multiplication (same operator!)
```

### Permanent (supertropical determinant)

```python
perm = A.permanent()

print(f"Permanent: {perm}")
```

### Adjoint matrix

```python
adj = A.adjoint()

print(f"Adjoint:\n{adj}")

```

## Solving Linear Systems

```python
# Define system: Ax = b

A = suptrop.Matrix([[2, 1],
                    [1, 3]])
b = suptrop.Matrix([[5],
                    [4]])
x = A.solve(b)

print(f"Solution:\n{x}"
```

## Solve using Cramer's rule

## 📖 Documentation

- Full documentation is available at: **[GitHub Pages](https://tetewhereoez.github.io/supertropical-algebra)**

- **[Theory Guide](https://tetewhereoez.github.io/supertropical-algebra/theory.html)**: Mathematical background on supertropical algebra

- **[Interactive Tutorial](https://tetewhereoez.github.io/supertropical-algebra/examples/tutorial.html)**: Jupyter notebook with executable examples

- **[API Reference](https://tetewhereoez.github.io/supertropical-algebra/api/index.html)**: Complete API documentation

## 🧪 Running Tests

```bash

# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

```

## Run with coverage

```bash
pytest --cov=supertropical

```

## 📚 Building Documentation Locally

```bash
# Install docs dependencies
pip install -e ".[docs]"

# Build HTML docs
cd docs
sphinx-build -b html source build
pytest --cov=supertropical

```

## 📚 Building Documentation Locally

```bash
# Install docs dependencies

pip install -e ".[docs]"

# Build HTML docs

cd docs

sphinx-build -b html source build
```

```python
# Or use make (on Unix/Mac/Windows with make installed)
cd docs

make html
```

## 🎓 Mathematical Background

Supertropical algebra extends tropical algebra with ghost elements:

**Operations**:

- **Addition**: $a \oplus b = \max(a, b)$ with special ghost rules

- **Multiplication**: $a \odot b = a + b$ (classical addition)

**Elements**:

- **Tangible**: Regular elements (e.g., $5.0$)

- **Ghost**: Elements marked with $\nu$ (e.g., $5.0\nu$)

- **Zero**: $-\infty$ (additive identity)

- **One**: $0$ (multiplicative identity)

**Key Properties**:

- Matrix permanent replaces determinant

- Cramer's rule works for nonsingular matrices (permanent is tangible)

- Applications in optimization, algebraic geometry, and phylogenetics

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.```

## 👥 Authors

- **Supertropical Team**

## 🙏 Acknowledgments

- Based on research by Izhakian, Z., & Rowen, L. on supertropical algebra

## 📞 Contact

- **GitHub**: [https://github.com/TetewHeroez/supertropical-algebra](https://github.com/TetewHeroez/supertropical-algebra)

- **Issues**: [https://github.com/TetewHeroez/supertropical-algebra/issues](https://github.com/TetewHeroez/supertropical-algebra/issues)

- **Documentation**: [https://tetewhereoez.github.io/supertropical-algebra](https://tetewhereoez.github.io/supertropical-algebra)
