# Supertropical Algebra

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/TetewHeroez/supertropical-algebra/main?filepath=docs/source/examples/tutorial.ipynb)

A comprehensive Python package for **supertropical algebra**, featuring tangible and ghost elements, matrix operations, and linear system solving using Cramer's rule.

> **?? Try it now!** Click the Binder badge above to run the interactive tutorial in your browser without installing anything. A comprehensive Python package for **supertropical algebra**, featuring tangible and ghost elements, matrix operations, and linear system solving using Cramer's rule.

## ? Features

- **?? Tangible & Ghost Elements**: Full support for both element types with automatic conversion

- **?? Supertropical Operations**: Addition $\oplus$ defined by $a\oplus b=\max\{a,b\}$ (with ghost rules), and multiplication $\odot$ defined by $a\odot b=a+b$.

- **?? Matrix Operations**: Matrix multiplication, permanent (supertropical determinant), adjoint.

- **?? Linear System Solver**: Cramer's rule implementation for solving $Ax = b$

- **?? NumPy Integration**: Efficient computations using NumPy arrays

- **?? Comprehensive Documentation**: Full API reference, theory guide, and interactive tutorials

- **? Type Safety**: Automatic type coercion and validation

## ?? Installation 

```bash
pip install supertropical-algebra
```
Or install from source:

```bash

git clone https://github.com/TetewHeroez/supertropical-algebra.git

cd supertropical-algebra

pip install -e .

```



## ?? Quick Start



**Recommended: Use short alias (like numpy as `np` or tensorflow as `tf`)**



### Creating Elements 

```python
import supertropical as suptrop

# Tangible elements (regular)

a = suptrop.Element(5)

b = suptrop.Element(3)

# Ghost elements (marked with ?)

c = suptrop.Element(5, is_ghost=True)

print(a)  # Output: 5.0

print(c)  # Output: 5.0?
```

**Alternative:** You can also import directly:

```python
from supertropical import Element, Matrix

# Supertropical Algebra

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/TetewHeroez/supertropical-algebra/main?filepath=docs/source/examples/tutorial.ipynb)

A compact, well-tested Python package for working with supertropical algebra. It provides:

- Tangible and ghost elements (ghosts are displayed with the ? symbol)
- Supertropical arithmetic (addition = max with ghost rules, multiplication = classical addition)
- Matrix operations (matrix product, permanent, adjoint)
- A simple linear system solver using Cramer's rule (for nonsingular matrices)

Quick links

- Documentation (HTML): https://tetewhereoez.github.io/supertropical-algebra
- Interactive tutorial (Binder): click the badge above
- Source code: https://github.com/TetewHeroez/supertropical-algebra

## Installation

Install from PyPI:

```bash
pip install supertropical-algebra
```

Or install from source (editable):

```bash
git clone https://github.com/TetewHeroez/supertropical-algebra.git
cd supertropical-algebra
pip install -e .
```

## Quick Start

Recommended short import (like numpy as np):

```python
import supertropical as suptrop

# Elements
a = suptrop.Element(5)           # tangible
b = suptrop.Element(3, is_ghost=True)  # ghost (3?)

print(a)  # -> 5.0
print(b)  # -> 3.0?

# Arithmetic
print(a + b)  # supertropical addition
print(a * b)  # supertropical multiplication
```

Matrix example and solving:

```python
from supertropical import Matrix

A = Matrix([[2, 1], [1, 3]])
b = Matrix([[5], [4]])

print("permanent:", A.permanent())
print("solution:", A.solve(b))
```

## Documentation

Full documentation (theory, API, examples) is built with Sphinx and available at the GitHub Pages site above after deployment.

To build docs locally:

```bash
pip install -e .
pip install -r docs/requirements.txt
cd docs
sphinx-build -b html source build/html
```

## Tests

Run the test suite with pytest (recommended to install dev extras):

```bash
pip install -e ".[dev]"
pytest
```

## Contributing

Contributions welcome — open an issue or submit a pull request. Follow standard GitHub workflow:

1. Fork and branch
2. Add tests
3. Open PR

## License

MIT — see `LICENSE`

---

Made with ?? for mathematical computing
# Permanent (supertropical determinant)

perm = A.permanent()from supertropical import Element, Matrix

print(f"Permanent: {perm}")

# Even shorter!```.. code-block:: bash

# Adjoint matrix

adj = A.adjoint()a = Element(5)

````

`````

### Solving Linear Systems

### Supertropical Arithmetic## ?? Quick Start pip install supertropical-algebra

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

# Addition (?): max operation with ghost rules

## ?? Documentation

result1 = a + b  # 5 ? 3 = 5 (max)

Full documentation is available at: **[GitHub Pages](https://tetewhereoez.github.io/supertropical-algebra)**

result2 = a + a  # 5 ? 5 = 5? (becomes ghost)

- **[Theory Guide](https://tetewhereoez.github.io/supertropical-algebra/theory.html)**: Mathematical background on supertropical algebra

- **[Interactive Tutorial](https://tetewhereoez.github.io/supertropical-algebra/examples/tutorial.html)**: Jupyter notebook with executable examples```python   git clone https://github.com/YOUR_USERNAME/supertropical-algebra.git

- **[API Reference](https://tetewhereoez.github.io/supertropical-algebra/api/index.html)**: Complete API documentation

# Multiplication (?): classical addition

## ?? Running Tests

result3 = a * b  # 5 ? 3 = 8 (5 + 3)import supertropical as suptrop   cd supertropical-algebra

```bash

# Install dev dependenciesresult4 = a * c  # 5 ? 5? = 10? (result is ghost)

pip install -e ".[dev]"

   pip install -e .

# Run tests

pytest# Works with Python numbers



# Run with coverageresult5 = a + 7  # Automatic conversion# Tangible elements (regular)

pytest --cov=supertropical

```result6 = 2 * a  # 2 ? 5 = 7



## ?? Building Documentation Locally```a = suptrop.Element(5)?? Quick Start



```bash

# Install docs dependencies

pip install -e ".[docs]"### Matrix Operationsb = suptrop.Element(3)==============



# Build HTML docs

cd docs

sphinx-build -b html source build```python



# Or use make (on Unix/Mac/Windows with make installed)import supertropical as suptrop

cd docs

make html# Ghost elements (marked with ?)**Recommended: Use short alias like numpy (np) or tensorflow (tf)**

```

# Create matrices

The documentation will be in `docs/build/html/index.html`.

A = suptrop.Matrix([[2, 1], c = suptrop.Element(5, is_ghost=True)

## ?? Mathematical Background

                    [1, 3]])

Supertropical algebra extends tropical algebra with ghost elements:

Creating Elements

**Operations**:

- **Addition** (?): `a ? b = max(a, b)` with special ghost rulesB = suptrop.Matrix([[5, 4],

- **Multiplication** (?): `a ? b = a + b` (classical addition)

                    [2, 1]])print(a)  # Output: 5.0-----------------

**Elements**:

- **Tangible**: Regular elements (e.g., `5.0`)

- **Ghost**: Elements marked with ? (e.g., `5.0?`)

- **Zero**: `-8` (additive identity)# Matrix multiplication (supertropical)print(c)  # Output: 5.0?

- **One**: `0` (multiplicative identity)

C = A * B

**Key Properties**:

- Matrix permanent replaces determinant```.. code-block:: python

- Cramer's rule works for nonsingular matrices (permanent is tangible)

- Applications in optimization, algebraic geometry, and phylogenetics# Permanent (supertropical determinant)



## ?? Contributingperm = A.permanent()



Contributions are welcome! Please feel free to submit a Pull Request.print(f"Permanent: {perm}")



1. Fork the repository**Alternative:** You can also import directly:   import supertropical as suptrop

2. Create your feature branch (`git checkout -b feature/amazing-feature`)

3. Commit your changes (`git commit -m 'Add amazing feature'`)# Adjoint matrix

4. Push to the branch (`git push origin feature/amazing-feature`)

5. Open a Pull Requestadj = A.adjoint()



## ?? License````



This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.````python # Tangible elements (regular)



## ?? Authors### Solving Linear Systems



- **Supertropical Team**from supertropical import Element, Matrix   a = suptrop.Element(5)



## ?? Acknowledgments```python



- Based on research by Izhakian, Z., & Rowen, L. on supertropical algebraimport supertropical as suptrop# Even shorter!   b = suptrop.Element(3)

- Inspired by tropical algebra and max-plus algebra implementations



## ?? Contact

# Define system: Ax = ba = Element(5)

- **GitHub**: [https://github.com/TetewHeroez/supertropical-algebra](https://github.com/TetewHeroez/supertropical-algebra)

- **Issues**: [https://github.com/TetewHeroez/supertropical-algebra/issues](https://github.com/TetewHeroez/supertropical-algebra/issues)A = suptrop.Matrix([[2, 1],

- **Documentation**: [https://tetewhereoez.github.io/supertropical-algebra](https://tetewhereoez.github.io/supertropical-algebra)

                    [1, 3]])```   # Ghost elements (marked with ?)

---



**Made with ?? for mathematical computing**

b = suptrop.Matrix([[5],    c = suptrop.Element(5, is_ghost=True)

                    [4]])

### Supertropical Arithmetic

# Solve using Cramer's rule

x = A.solve(b)   print(a)  # Output: 5.0



print(f"Solution:\n{x}")```python   print(c)  # Output: 5.0?

`````

import supertropical as suptrop

## ?? Documentation

**Alternative:** You can also import directly:

Full documentation is available at: **[GitHub Pages](https://YOUR_USERNAME.github.io/supertropical-algebra)**

a = suptrop.Element(5)

- **[Theory Guide](https://YOUR_USERNAME.github.io/supertropical-algebra/theory.html)**: Mathematical background on supertropical algebra

- **[Interactive Tutorial](https://YOUR_USERNAME.github.io/supertropical-algebra/examples/tutorial.html)**: Jupyter notebook with executable examplesb = suptrop.Element(3).. code-block:: python

- **[API Reference](https://YOUR_USERNAME.github.io/supertropical-algebra/api/index.html)**: Complete API documentation

c = suptrop.Element(5, is_ghost=True)

## ?? Running Tests

from supertropical import Element, Matrix

````bash

# Install dev dependencies# Addition (?): max operation with ghost rules   # Even shorter!

pip install -e ".[dev]"

result1 = a + b  # 5 ? 3 = 5 (max)   a = Element(5)

# Run tests

pytestresult2 = a + a  # 5 ? 5 = 5? (becomes ghost)



# Run with coverageSupertropical Arithmetic

pytest --cov=supertropical

```# Multiplication (?): classical addition-------------------------



## ?? Building Documentation Locallyresult3 = a * b  # 5 ? 3 = 8 (5 + 3)



```bashresult4 = a * c  # 5 ? 5? = 10? (result is ghost).. code-block:: python

# Install docs dependencies

pip install -e ".[docs]"



# Build HTML docs# Works with Python numbers   import supertropical as suptrop

cd docs

sphinx-build -b html source buildresult5 = a + 7  # Automatic conversion



# Or use make (on Unix/Mac/Windows with make installed)result6 = 2 * a  # 2 ? 5 = 7   a = suptrop.Element(5)

cd docs

make html```   b = suptrop.Element(3)

````

c = suptrop.Element(5, is_ghost=True)

The documentation will be in `docs/build/html/index.html`.

### Matrix Operations

## ?? Mathematical Background

# Addition (?): max operation with ghost rules

Supertropical algebra extends tropical algebra with ghost elements:

````python result1 = a + b  # 5 ? 3 = 5 (max)

**Operations**:

- **Addition** (?): `a ? b = max(a, b)` with special ghost rulesimport supertropical as suptrop   result2 = a + a  # 5 ? 5 = 5? (becomes ghost)

- **Multiplication** (?): `a ? b = a + b` (classical addition)



**Elements**:

- **Tangible**: Regular elements (e.g., `5.0`)# Create matrices   # Multiplication (?): classical addition

- **Ghost**: Elements marked with ? (e.g., `5.0?`)

- **Zero**: `-8` (additive identity)A = suptrop.Matrix([[2, 1],    result3 = a * b  # 5 ? 3 = 8 (5 + 3)

- **One**: `0` (multiplicative identity)

                    [1, 3]])   result4 = a * c  # 5 ? 5? = 10? (result is ghost)

**Key Properties**:

- Matrix permanent replaces determinant

- Cramer's rule works for nonsingular matrices (permanent is tangible)

- Applications in optimization, algebraic geometry, and phylogeneticsB = suptrop.Matrix([[5, 4],    # Works with Python numbers



## ?? Contributing                    [2, 1]])   result5 = a + 7  # Automatic conversion



Contributions are welcome! Please feel free to submit a Pull Request.   result6 = 2 * a  # 2 ? 5 = 7



1. Fork the repository# Matrix multiplication (supertropical)

2. Create your feature branch (`git checkout -b feature/amazing-feature`)

3. Commit your changes (`git commit -m 'Add amazing feature'`)C = A * BMatrix Operations

4. Push to the branch (`git push origin feature/amazing-feature`)

5. Open a Pull Request-----------------



## ?? License# Permanent (supertropical determinant)



This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.perm = A.permanent().. code-block:: python



## ?? Authorsprint(f"Permanent: {perm}")



- **Supertropical Team**   import supertropical as suptrop



## ?? Acknowledgments# Adjoint matrix



- Based on research by Izhakian, Z., & Rowen, L. on supertropical algebraadj = A.adjoint()   # Create matrices

- Inspired by tropical algebra and max-plus algebra implementations

```   A = suptrop.Matrix([[2, 1],

## ?? Contact

                  [1, 3]])

- **GitHub**: [https://github.com/YOUR_USERNAME/supertropical-algebra](https://github.com/YOUR_USERNAME/supertropical-algebra)

- **Issues**: [https://github.com/YOUR_USERNAME/supertropical-algebra/issues](https://github.com/YOUR_USERNAME/supertropical-algebra/issues)### Solving Linear Systems

- **Documentation**: [https://YOUR_USERNAME.github.io/supertropical-algebra](https://YOUR_USERNAME.github.io/supertropical-algebra)

   B = suptrop.Matrix([[5, 4],

---

```python                  [2, 1]])

**Made with ?? for mathematical computing**

import supertropical as suptrop

   # Matrix multiplication (supertropical)

# Define system: Ax = b   C = A * B

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

## ?? Documentation

import supertropical as suptrop

Full documentation is available at: [GitHub Pages](https://github.com/YOUR_USERNAME/supertropical-algebra)

# Define system: Ax = b

- **Theory Guide**: Mathematical background on supertropical algebra A = suptrop.Matrix([[2, 1],

- **Tutorial**: Interactive Jupyter notebook with executable examples [1, 3]])

- **API Reference**: Complete API documentation with examples

  b = suptrop.Matrix([[5],

## ?? Running Tests [4]])

````bash # Solve using Cramer's rule

# Install dev dependencies   x = A.solve(b)

pip install -e ".[dev]"

   print(f"Solution:\n{x}")   # Solve using Cramer's rule

# Run tests   x = A.solve(b)

pytest

   print(f"Solution:\\n{x}")

# Run with coverage

pytest --cov=supertropical?? Documentation

```================



## ?? Building DocumentationFull documentation is available at: `GitHub Pages <https://github.com/YOUR_USERNAME/supertropical-algebra>`_



```bash- **Theory Guide**: Mathematical background on supertropical algebra

# Install docs dependencies- **Tutorial**: Interactive Jupyter notebook with executable examples

pip install -e ".[docs]"- **API Reference**: Complete API documentation with examples



# Build HTML docs?? Running Tests

cd docs================

sphinx-build -b html source build

.. code-block:: bash

# Or use make (on Unix/Mac/Windows with make installed)

cd docs   # Install dev dependencies

make html   pip install -e ".[dev]"

````

# Run tests

The documentation will be in `docs/build/index.html`. pytest

## ?? Mathematical Background # Run with coverage

pytest --cov=supertropical

Supertropical algebra extends tropical algebra with ghost elements:

?? Building Documentation

**Operations**:=========================

- **Addition** (?): `a ? b = max(a, b)` with special ghost rules

- **Multiplication** (?): `a ? b = a + b` (classical addition).. code-block:: bash

**Elements**: # Install docs dependencies

- **Tangible**: Regular elements (e.g., `5.0`) pip install -e ".[docs]"

- **Ghost**: Elements marked with ? (e.g., `5.0?`)

- **Zero**: `-8` (additive identity) # Build HTML docs

- **One**: `0` (multiplicative identity) cd docs

  sphinx-build -b html source build

**Key Properties**:

- Matrix permanent replaces determinant # Or use make (on Unix/Mac/Windows with make installed)

- Cramer's rule works for nonsingular matrices (permanent is tangible) cd docs

- Applications in optimization, algebraic geometry, and phylogenetics make html

## ?? ContributingThe documentation will be in `docs/build/index.html`.

Contributions are welcome! Please feel free to submit a Pull Request.?? Mathematical Background

===========================

1. Fork the repository

2. Create your feature branch (`git checkout -b feature/amazing-feature`)Supertropical algebra extends tropical algebra with ghost elements:

3. Commit your changes (`git commit -m 'Add amazing feature'`)

4. Push to the branch (`git push origin feature/amazing-feature`)**Operations**:

5. Open a Pull Request

- **Addition** (?): `a ? b = max(a, b)` with special ghost rules

## ?? License- **Multiplication** (?): `a ? b = a + b` (classical addition)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.**Elements**:

## ?? Authors- **Tangible**: Regular elements (e.g., `5.0`)

- **Ghost**: Elements marked with ? (e.g., `5.0?`)

- **Supertropical Team**- **Zero**: `-8` (additive identity)

- **One**: `0` (multiplicative identity)

## ?? Acknowledgments

**Key Properties**:

- Based on research by Izhakian, Z., & Rowen, L. on supertropical algebra

- Inspired by tropical algebra and max-plus algebra implementations- Matrix permanent replaces determinant

- Cramer's rule works for nonsingular matrices (permanent is tangible)

## ?? Contact- Applications in optimization, algebraic geometry, and phylogenetics

- GitHub: https://github.com/YOUR_USERNAME/supertropical-algebra?? Contributing

- Issues: https://github.com/YOUR_USERNAME/supertropical-algebra/issues===============

---Contributions are welcome! Please feel free to submit a Pull Request.

Made with ?? for mathematical computing1. Fork the repository

2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

# ?? License

This project is licensed under the MIT License - see the `LICENSE <LICENSE>`\_ file for details.

# ?? Authors

- **Supertropical Team**

# ?? Acknowledgments

- Based on research by Izhakian, Z., & Rowen, L. on supertropical algebra
- Inspired by tropical algebra and max-plus algebra implementations

# ?? Contact

- GitHub: `https://github.com/YOUR_USERNAME/supertropical-algebra <https://github.com/YOUR_USERNAME/supertropical-algebra>`\_
- Issues: `https://github.com/YOUR_USERNAME/supertropical-algebra/issues <https://github.com/YOUR_USERNAME/supertropical-algebra/issues>`\_

---

Made with ?? for mathematical computing
