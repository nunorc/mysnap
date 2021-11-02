
from setuptools import setup, find_packages
from mysnap import __version__

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setup(name = 'mysnap',
      version = __version__,
      url = 'https://github.com/nunorc/mysnap',
      author = 'Nuno Carvalho',
      author_email = 'narcarvalho@gmail.com',
      description = 'utilities for working with ESA SNAP toolbox products',
      long_description = long_description,
      long_description_content_type = 'text/x-rst',
      license = 'MIT',
      packages = find_packages(),
      install_requires = ['rasterio', 'numpy'])

