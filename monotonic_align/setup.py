from distutils.core import setup
# from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

# extensions = [
#     Extension('my_module', ['my_module.pyx'], cython_directives={'language_level': '3'})
# ]

setup(
    name="monotonic_align",
    ext_modules=cythonize("core.pyx"，language_level=3),
    include_dirs=[numpy.get_include()],
)
