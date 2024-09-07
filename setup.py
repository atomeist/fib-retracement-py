from setuptools import setup, find_packages

setup(
    name="fib_retracement_py",
    version="0.1.0",
    description="A Python tool to calculate Fibonacci retracement levels",
    author="atomeist",
    author_email="keyur.atomeist@gmail.com",
    packages=find_packages(),
    install_requires=[],  # No dependencies for this simple package
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
