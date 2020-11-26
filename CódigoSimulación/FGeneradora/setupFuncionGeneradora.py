from setuptools import setup
from Cython.Build import cythonize

setup(
    name='FuncionGeneradora',
    ext_modules=cythonize("FuncionGeneradora.pyx"),
    zip_safe=False,
)
