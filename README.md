# Supertropical Algebra# Supertropical Algebra# Supertropical Algebra=======================

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)Supertropical Algebra

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/TetewHeroez/supertropical-algebra/main?filepath=docs/source/examples/tutorial.ipynb)[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A comprehensive Python package for **supertropical algebra**, featuring tangible and ghost elements, matrix operations, and linear system solving using Cramer's rule.[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/YOUR_USERNAME/supertropical-algebra/main?filepath=docs/source/examples/tutorial.ipynb)[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)=======================

> **🚀 Try it now!** Click the Binder badge above to run the interactive tutorial in your browser without installing anything.A comprehensive Python package for **supertropical algebra**, featuring tangible and ghost elements, matrix operations, and linear system solving using Cramer's rule.[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## ✨ Features> **🚀 Try it now!** Click the Binder badge above to run the interactive tutorial in your browser without installing anything... image:: https://img.shields.io/badge/python-3.8+-blue.svg

- **🎯 Tangible & Ghost Elements**: Full support for both element types with automatic conversion## ✨ FeaturesA comprehensive Python package for **supertropical algebra**, featuring tangible and ghost elements, matrix operations, and linear system solving using Cramer's rule. :target: https://www.python.org/downloads/

- **🧮 Supertropical Operations**: Addition (⊕ as max) and multiplication (⊙ as classical +)

- **📐 Matrix Operations**: Matrix multiplication, permanent (supertropical determinant), adjoint- **🎯 Tangible & Ghost Elements**: Full support for both element types with automatic conversion :alt: Python Version

- **🔧 Linear System Solver**: Cramer's rule implementation for solving Ax = b

- **🚀 NumPy Integration**: Efficient computations using NumPy arrays- **🧮 Supertropical Operations**: Addition (⊕ as max) and multiplication (⊙ as classical +)

- **📚 Comprehensive Documentation**: Full API reference, theory guide, and interactive tutorials

- **✅ Type Safety**: Automatic type coercion and validation- **📐 Matrix Operations**: Matrix multiplication, permanent (supertropical determinant), adjoint## ✨ Features

## 📦 Installation- **🔧 Linear System Solver**: Cramer's rule implementation for solving Ax = b

`````bash- **🚀 NumPy Integration**: Efficient computations using NumPy arrays.. image:: https://img.shields.io/badge/license-MIT-green.svg

pip install supertropical-algebra

```- **📚 Comprehensive Documentation**: Full API reference, theory guide, and interactive tutorials



Or install from source:- **✅ Type Safety**: Automatic type coercion and validation- **🎯 Tangible & Ghost Elements**: Full support for both element types with automatic conversion :target: LICENSE



```bash## 📦 Installation- **🧮 Supertropical Operations**: Addition (⊕ as max) and multiplication (⊙ as classical +) :alt: License

git clone https://github.com/TetewHeroez/supertropical-algebra.git

cd supertropical-algebra````bash- **📐 Matrix Operations**: Matrix multiplication, permanent (supertropical determinant), adjoint

pip install -e .

```pip install supertropical-algebra



## 🚀 Quick Start```- **🔧 Linear System Solver**: Cramer's rule implementation for solving Ax = bA comprehensive Python package for **supertropical algebra**, featuring tangible and ghost elements,



**Recommended: Use short alias (like numpy as `np` or tensorflow as `tf`)**



### Creating ElementsOr install from source:- **🚀 NumPy Integration**: Efficient computations using NumPy arraysmatrix operations, and linear system solving using Cramer's rule.



```python

import supertropical as suptrop

```bash- **📚 Comprehensive Documentation**: Full API reference, theory guide, and interactive tutorials

# Tangible elements (regular)

a = suptrop.Element(5)git clone https://github.com/YOUR_USERNAME/supertropical-algebra.git

b = suptrop.Element(3)

cd supertropical-algebra- **✅ Type Safety**: Automatic type coercion and validation✨ Features

# Ghost elements (marked with ν)

c = suptrop.Element(5, is_ghost=True)pip install -e .



print(a)  # Output: 5.0```===========

print(c)  # Output: 5.0ν

`````

**Alternative:** You can also import directly:## 🚀 Quick Start## 📦 Installation

```python

from supertropical import Element, Matrix

# Even shorter!**Recommended: Use short alias (like numpy as `np` or tensorflow as `tf`)**- **🎯 Tangible & Ghost Elements**: Full support for both element types with automatic conversion

a = Element(5)

```

### Supertropical Arithmetic### Creating Elements```bash- **🧮 Supertropical Operations**: Addition (⊕ as max) and multiplication (⊙ as classical +)

````python

import supertropical as suptrop

```pythonpip install supertropical-algebra- **📐 Matrix Operations**: Matrix multiplication, permanent (supertropical determinant), adjoint

a = suptrop.Element(5)

b = suptrop.Element(3)import supertropical as suptrop

c = suptrop.Element(5, is_ghost=True)

```- **🔧 Linear System Solver**: Cramer's rule implementation for solving Ax = b

# Addition (⊕): max operation with ghost rules

result1 = a + b  # 5 ⊕ 3 = 5 (max)# Tangible elements (regular)

result2 = a + a  # 5 ⊕ 5 = 5ν (becomes ghost)

a = suptrop.Element(5)- **🚀 NumPy Integration**: Efficient computations using NumPy arrays

# Multiplication (⊙): classical addition

result3 = a * b  # 5 ⊙ 3 = 8 (5 + 3)b = suptrop.Element(3)

result4 = a * c  # 5 ⊙ 5ν = 10ν (result is ghost)

Or install from source:- **📚 Comprehensive Documentation**: Full API reference, theory guide, and interactive tutorials

# Works with Python numbers

result5 = a + 7  # Automatic conversion# Ghost elements (marked with ν)

result6 = 2 * a  # 2 ⊙ 5 = 7

```c = suptrop.Element(5, is_ghost=True)- **✅ Type Safety**: Automatic type coercion and validation



### Matrix Operations



```pythonprint(a)  # Output: 5.0```bash

import supertropical as suptrop

print(c)  # Output: 5.0ν

# Create matrices

A = suptrop.Matrix([[2, 1], ```git clone https://github.com/YOUR_USERNAME/supertropical-algebra.git📦 Installation

                    [1, 3]])



B = suptrop.Matrix([[5, 4],

                    [2, 1]])**Alternative:** You can also import directly:cd supertropical-algebra===============



# Matrix multiplication (supertropical)

C = A @ B

```pythonpip install -e .

# Permanent (supertropical determinant)

perm = A.permanent()from supertropical import Element, Matrix

print(f"Permanent: {perm}")

# Even shorter!```.. code-block:: bash

# Adjoint matrix

adj = A.adjoint()a = Element(5)

````

`````

### Solving Linear Systems

### Supertropical Arithmetic## 🚀 Quick Start pip install supertropical-algebra

```python

import supertropical as suptrop````python



# Define system: Ax = bimport supertropical as suptrop

A = suptrop.Matrix([[2, 1],

                    [1, 3]])**Recommended: Use short alias (like numpy as np or tensorflow as tf)**Or install from source:



b = suptrop.Matrix([[5], a = suptrop.Element(5)

                    [4]])

b = suptrop.Element(3)

# Solve using Cramer's rule

x = A.solve(b)c = suptrop.Element(5, is_ghost=True)



print(f"Solution:\n{x}")### Creating Elements.. code-block:: bash

```

# Addition (⊕): max operation with ghost rules

## 📖 Documentation

result1 = a + b  # 5 ⊕ 3 = 5 (max)

Full documentation is available at: **[GitHub Pages](https://tetewhereoez.github.io/supertropical-algebra)**

result2 = a + a  # 5 ⊕ 5 = 5ν (becomes ghost)

- **[Theory Guide](https://tetewhereoez.github.io/supertropical-algebra/theory.html)**: Mathematical background on supertropical algebra

- **[Interactive Tutorial](https://tetewhereoez.github.io/supertropical-algebra/examples/tutorial.html)**: Jupyter notebook with executable examples```python   git clone https://github.com/YOUR_USERNAME/supertropical-algebra.git

- **[API Reference](https://tetewhereoez.github.io/supertropical-algebra/api/index.html)**: Complete API documentation

# Multiplication (⊙): classical addition

## 🧪 Running Tests

result3 = a * b  # 5 ⊙ 3 = 8 (5 + 3)import supertropical as suptrop   cd supertropical-algebra

```bash

# Install dev dependenciesresult4 = a * c  # 5 ⊙ 5ν = 10ν (result is ghost)

pip install -e ".[dev]"

   pip install -e .

# Run tests

pytest# Works with Python numbers



# Run with coverageresult5 = a + 7  # Automatic conversion# Tangible elements (regular)

pytest --cov=supertropical

```result6 = 2 * a  # 2 ⊙ 5 = 7



## 📚 Building Documentation Locally```a = suptrop.Element(5)🚀 Quick Start



```bash

# Install docs dependencies

pip install -e ".[docs]"### Matrix Operationsb = suptrop.Element(3)==============



# Build HTML docs

cd docs

sphinx-build -b html source build```python



# Or use make (on Unix/Mac/Windows with make installed)import supertropical as suptrop

cd docs

make html# Ghost elements (marked with ν)**Recommended: Use short alias like numpy (np) or tensorflow (tf)**

```

# Create matrices

The documentation will be in `docs/build/html/index.html`.

A = suptrop.Matrix([[2, 1], c = suptrop.Element(5, is_ghost=True)

## 🎓 Mathematical Background

                    [1, 3]])

Supertropical algebra extends tropical algebra with ghost elements:

Creating Elements

**Operations**:

- **Addition** (⊕): `a ⊕ b = max(a, b)` with special ghost rulesB = suptrop.Matrix([[5, 4],

- **Multiplication** (⊙): `a ⊙ b = a + b` (classical addition)

                    [2, 1]])print(a)  # Output: 5.0-----------------

**Elements**:

- **Tangible**: Regular elements (e.g., `5.0`)

- **Ghost**: Elements marked with ν (e.g., `5.0ν`)

- **Zero**: `-∞` (additive identity)# Matrix multiplication (supertropical)print(c)  # Output: 5.0ν

- **One**: `0` (multiplicative identity)

C = A @ B

**Key Properties**:

- Matrix permanent replaces determinant```.. code-block:: python

- Cramer's rule works for nonsingular matrices (permanent is tangible)

- Applications in optimization, algebraic geometry, and phylogenetics# Permanent (supertropical determinant)



## 🤝 Contributingperm = A.permanent()



Contributions are welcome! Please feel free to submit a Pull Request.print(f"Permanent: {perm}")



1. Fork the repository**Alternative:** You can also import directly:   import supertropical as suptrop

2. Create your feature branch (`git checkout -b feature/amazing-feature`)

3. Commit your changes (`git commit -m 'Add amazing feature'`)# Adjoint matrix

4. Push to the branch (`git push origin feature/amazing-feature`)

5. Open a Pull Requestadj = A.adjoint()



## 📄 License````



This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.````python # Tangible elements (regular)



## 👥 Authors### Solving Linear Systems



- **Supertropical Team**from supertropical import Element, Matrix   a = suptrop.Element(5)



## 🙏 Acknowledgments```python



- Based on research by Izhakian, Z., & Rowen, L. on supertropical algebraimport supertropical as suptrop# Even shorter!   b = suptrop.Element(3)

- Inspired by tropical algebra and max-plus algebra implementations



## 📞 Contact

# Define system: Ax = ba = Element(5)

- **GitHub**: [https://github.com/TetewHeroez/supertropical-algebra](https://github.com/TetewHeroez/supertropical-algebra)

- **Issues**: [https://github.com/TetewHeroez/supertropical-algebra/issues](https://github.com/TetewHeroez/supertropical-algebra/issues)A = suptrop.Matrix([[2, 1],

- **Documentation**: [https://tetewhereoez.github.io/supertropical-algebra](https://tetewhereoez.github.io/supertropical-algebra)

                    [1, 3]])```   # Ghost elements (marked with ν)

---



**Made with ❤️ for mathematical computing**

b = suptrop.Matrix([[5],    c = suptrop.Element(5, is_ghost=True)

                    [4]])

### Supertropical Arithmetic

# Solve using Cramer's rule

x = A.solve(b)   print(a)  # Output: 5.0



print(f"Solution:\n{x}")```python   print(c)  # Output: 5.0ν

`````

import supertropical as suptrop

## 📖 Documentation

**Alternative:** You can also import directly:

Full documentation is available at: **[GitHub Pages](https://YOUR_USERNAME.github.io/supertropical-algebra)**

a = suptrop.Element(5)

- **[Theory Guide](https://YOUR_USERNAME.github.io/supertropical-algebra/theory.html)**: Mathematical background on supertropical algebra

- **[Interactive Tutorial](https://YOUR_USERNAME.github.io/supertropical-algebra/examples/tutorial.html)**: Jupyter notebook with executable examplesb = suptrop.Element(3).. code-block:: python

- **[API Reference](https://YOUR_USERNAME.github.io/supertropical-algebra/api/index.html)**: Complete API documentation

c = suptrop.Element(5, is_ghost=True)

## 🧪 Running Tests

from supertropical import Element, Matrix

````bash

# Install dev dependencies# Addition (⊕): max operation with ghost rules   # Even shorter!

pip install -e ".[dev]"

result1 = a + b  # 5 ⊕ 3 = 5 (max)   a = Element(5)

# Run tests

pytestresult2 = a + a  # 5 ⊕ 5 = 5ν (becomes ghost)



# Run with coverageSupertropical Arithmetic

pytest --cov=supertropical

```# Multiplication (⊙): classical addition-------------------------



## 📚 Building Documentation Locallyresult3 = a * b  # 5 ⊙ 3 = 8 (5 + 3)



```bashresult4 = a * c  # 5 ⊙ 5ν = 10ν (result is ghost).. code-block:: python

# Install docs dependencies

pip install -e ".[docs]"



# Build HTML docs# Works with Python numbers   import supertropical as suptrop

cd docs

sphinx-build -b html source buildresult5 = a + 7  # Automatic conversion



# Or use make (on Unix/Mac/Windows with make installed)result6 = 2 * a  # 2 ⊙ 5 = 7   a = suptrop.Element(5)

cd docs

make html```   b = suptrop.Element(3)

````

c = suptrop.Element(5, is_ghost=True)

The documentation will be in `docs/build/html/index.html`.

### Matrix Operations

## 🎓 Mathematical Background

# Addition (⊕): max operation with ghost rules

Supertropical algebra extends tropical algebra with ghost elements:

````python result1 = a + b  # 5 ⊕ 3 = 5 (max)

**Operations**:

- **Addition** (⊕): `a ⊕ b = max(a, b)` with special ghost rulesimport supertropical as suptrop   result2 = a + a  # 5 ⊕ 5 = 5ν (becomes ghost)

- **Multiplication** (⊙): `a ⊙ b = a + b` (classical addition)



**Elements**:

- **Tangible**: Regular elements (e.g., `5.0`)# Create matrices   # Multiplication (⊙): classical addition

- **Ghost**: Elements marked with ν (e.g., `5.0ν`)

- **Zero**: `-∞` (additive identity)A = suptrop.Matrix([[2, 1],    result3 = a * b  # 5 ⊙ 3 = 8 (5 + 3)

- **One**: `0` (multiplicative identity)

                    [1, 3]])   result4 = a * c  # 5 ⊙ 5ν = 10ν (result is ghost)

**Key Properties**:

- Matrix permanent replaces determinant

- Cramer's rule works for nonsingular matrices (permanent is tangible)

- Applications in optimization, algebraic geometry, and phylogeneticsB = suptrop.Matrix([[5, 4],    # Works with Python numbers



## 🤝 Contributing                    [2, 1]])   result5 = a + 7  # Automatic conversion



Contributions are welcome! Please feel free to submit a Pull Request.   result6 = 2 * a  # 2 ⊙ 5 = 7



1. Fork the repository# Matrix multiplication (supertropical)

2. Create your feature branch (`git checkout -b feature/amazing-feature`)

3. Commit your changes (`git commit -m 'Add amazing feature'`)C = A @ BMatrix Operations

4. Push to the branch (`git push origin feature/amazing-feature`)

5. Open a Pull Request-----------------



## 📄 License# Permanent (supertropical determinant)



This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.perm = A.permanent().. code-block:: python



## 👥 Authorsprint(f"Permanent: {perm}")



- **Supertropical Team**   import supertropical as suptrop



## 🙏 Acknowledgments# Adjoint matrix



- Based on research by Izhakian, Z., & Rowen, L. on supertropical algebraadj = A.adjoint()   # Create matrices

- Inspired by tropical algebra and max-plus algebra implementations

```   A = suptrop.Matrix([[2, 1],

## 📞 Contact

                  [1, 3]])

- **GitHub**: [https://github.com/YOUR_USERNAME/supertropical-algebra](https://github.com/YOUR_USERNAME/supertropical-algebra)

- **Issues**: [https://github.com/YOUR_USERNAME/supertropical-algebra/issues](https://github.com/YOUR_USERNAME/supertropical-algebra/issues)### Solving Linear Systems

- **Documentation**: [https://YOUR_USERNAME.github.io/supertropical-algebra](https://YOUR_USERNAME.github.io/supertropical-algebra)

   B = suptrop.Matrix([[5, 4],

---

```python                  [2, 1]])

**Made with ❤️ for mathematical computing**

import supertropical as suptrop

   # Matrix multiplication (supertropical)

# Define system: Ax = b   C = A @ B

A = suptrop.Matrix([[2, 1],

                    [1, 3]])   # Permanent (supertropical determinant)

   perm = A.permanent()

b = suptrop.Matrix([[5],    print(f"Permanent: {perm}")

                    [4]])

   # Adjoint matrix

# Solve using Cramer's rule   adj = A.adjoint()

x = A.solve(b)

Solving Linear Systems

print(f"Solution:\n{x}")----------------------

````

.. code-block:: python

## 📖 Documentation

import supertropical as suptrop

Full documentation is available at: [GitHub Pages](https://github.com/YOUR_USERNAME/supertropical-algebra)

# Define system: Ax = b

- **Theory Guide**: Mathematical background on supertropical algebra A = suptrop.Matrix([[2, 1],

- **Tutorial**: Interactive Jupyter notebook with executable examples [1, 3]])

- **API Reference**: Complete API documentation with examples

  b = suptrop.Matrix([[5],

## 🧪 Running Tests [4]])

````bash # Solve using Cramer's rule

# Install dev dependencies   x = A.solve(b)

pip install -e ".[dev]"

   print(f"Solution:\n{x}")   # Solve using Cramer's rule

# Run tests   x = A.solve(b)

pytest

   print(f"Solution:\\n{x}")

# Run with coverage

pytest --cov=supertropical📖 Documentation

```================



## 📚 Building DocumentationFull documentation is available at: `GitHub Pages <https://github.com/YOUR_USERNAME/supertropical-algebra>`_



```bash- **Theory Guide**: Mathematical background on supertropical algebra

# Install docs dependencies- **Tutorial**: Interactive Jupyter notebook with executable examples

pip install -e ".[docs]"- **API Reference**: Complete API documentation with examples



# Build HTML docs🧪 Running Tests

cd docs================

sphinx-build -b html source build

.. code-block:: bash

# Or use make (on Unix/Mac/Windows with make installed)

cd docs   # Install dev dependencies

make html   pip install -e ".[dev]"

````

# Run tests

The documentation will be in `docs/build/index.html`. pytest

## 🎓 Mathematical Background # Run with coverage

pytest --cov=supertropical

Supertropical algebra extends tropical algebra with ghost elements:

📚 Building Documentation

**Operations**:=========================

- **Addition** (⊕): `a ⊕ b = max(a, b)` with special ghost rules

- **Multiplication** (⊙): `a ⊙ b = a + b` (classical addition).. code-block:: bash

**Elements**: # Install docs dependencies

- **Tangible**: Regular elements (e.g., `5.0`) pip install -e ".[docs]"

- **Ghost**: Elements marked with ν (e.g., `5.0ν`)

- **Zero**: `-∞` (additive identity) # Build HTML docs

- **One**: `0` (multiplicative identity) cd docs

  sphinx-build -b html source build

**Key Properties**:

- Matrix permanent replaces determinant # Or use make (on Unix/Mac/Windows with make installed)

- Cramer's rule works for nonsingular matrices (permanent is tangible) cd docs

- Applications in optimization, algebraic geometry, and phylogenetics make html

## 🤝 ContributingThe documentation will be in `docs/build/index.html`.

Contributions are welcome! Please feel free to submit a Pull Request.🎓 Mathematical Background

===========================

1. Fork the repository

2. Create your feature branch (`git checkout -b feature/amazing-feature`)Supertropical algebra extends tropical algebra with ghost elements:

3. Commit your changes (`git commit -m 'Add amazing feature'`)

4. Push to the branch (`git push origin feature/amazing-feature`)**Operations**:

5. Open a Pull Request

- **Addition** (⊕): `a ⊕ b = max(a, b)` with special ghost rules

## 📄 License- **Multiplication** (⊙): `a ⊙ b = a + b` (classical addition)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.**Elements**:

## 👥 Authors- **Tangible**: Regular elements (e.g., `5.0`)

- **Ghost**: Elements marked with ν (e.g., `5.0ν`)

- **Supertropical Team**- **Zero**: `-∞` (additive identity)

- **One**: `0` (multiplicative identity)

## 🙏 Acknowledgments

**Key Properties**:

- Based on research by Izhakian, Z., & Rowen, L. on supertropical algebra

- Inspired by tropical algebra and max-plus algebra implementations- Matrix permanent replaces determinant

- Cramer's rule works for nonsingular matrices (permanent is tangible)

## 📞 Contact- Applications in optimization, algebraic geometry, and phylogenetics

- GitHub: https://github.com/YOUR_USERNAME/supertropical-algebra🤝 Contributing

- Issues: https://github.com/YOUR_USERNAME/supertropical-algebra/issues===============

---Contributions are welcome! Please feel free to submit a Pull Request.

Made with ❤️ for mathematical computing1. Fork the repository

2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

# 📄 License

This project is licensed under the MIT License - see the `LICENSE <LICENSE>`\_ file for details.

# 👥 Authors

- **Supertropical Team**

# 🙏 Acknowledgments

- Based on research by Izhakian, Z., & Rowen, L. on supertropical algebra
- Inspired by tropical algebra and max-plus algebra implementations

# 📞 Contact

- GitHub: `https://github.com/YOUR_USERNAME/supertropical-algebra <https://github.com/YOUR_USERNAME/supertropical-algebra>`\_
- Issues: `https://github.com/YOUR_USERNAME/supertropical-algebra/issues <https://github.com/YOUR_USERNAME/supertropical-algebra/issues>`\_

---

Made with ❤️ for mathematical computing
