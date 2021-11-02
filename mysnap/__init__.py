
""" mysnap init """

__version__ = '0.0.1'

import logging

from .classes import Band, Product
from .utils import normalize, tiles

logging.basicConfig(format = '%(asctime)s | %(levelname)s: %(message)s',
                    datefmt = "%Y-%m-%d %H:%M:%S",
                    level = logging.WARNING)

