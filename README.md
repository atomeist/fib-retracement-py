# Fibonacci Retracement (Python)

A simple Python package to calculate Fibonacci retracement levels.

## Installation

Clone this repository and install using pip:

```bash
pip install git+https://github.com/atomeist/fib-retracement-py.git

from fib_retracement import get_fib_retracement

fib = get_fib_retracement(0, 10)
print(fib)


- Create a `.gitignore` file to exclude unnecessary files like cache and build files:
  ```bash
  touch .gitignore
  ```

**Code for `.gitignore`:**
```gitignore
__pycache__/
*.pyc
*.pyo
dist/
build/
*.egg-info/
