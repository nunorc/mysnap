
""" Classes definitions. """

import logging
logger = logging.getLogger(__name__)

import os, glob, re
from pathlib import Path
import rasterio as rio
import numpy as np
from xml.dom import minidom
from collections import namedtuple

def _sort_alphanum(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]

    return sorted(data, key=alphanum_key)

class Band:
    """ A wrapper for storing an individual band.

    Attributes:
      filename (str): source file (.img file)
    """
    def __init__(self, filename):
        i = rio.open(filename)
        
        self.name = Path(filename).stem.lower()
        self.desc = i.descriptions[0]
        self.array = i.read(1).astype('float32')
        self.filename = filename
        self.rio = rio

class Product:
    """ A wrapper for storing bands from a product in BEAM-DIMAP format.
    
    Attributes:
      filename (str): source file (.dim file)
    """
    def __init__(self, filename):
        if filename.startswith('~'):
            filename = filename.replace('~', os.environ['HOME'])

        if not os.path.isfile(filename):
            logging.warning(f"File not found: { filename }")

        self.filename = filename
        self.datadir = filename.replace('.dim', '.data')
        self.bands = []
        self.meta = None

        self._load_meta()
        self._load_bands()

    def _load_meta(self):
        data = []

        doc = minidom.parse(self.filename)
        for tag in ['NCOLS', 'NROWS', 'NBANDS']:
            nodes = doc.getElementsByTagName(tag)
            if len(nodes) > 0:
                data.append(int(nodes[0].firstChild.data))

        Meta = namedtuple('Meta', 'ncols nrows nbands')
        self.meta = Meta(*data)

    def _load_bands(self):
        for file in glob.glob(os.path.join(self.datadir, '*.img')):
            b = Band(file)
            self.bands.append(b.name)
            
            self.__setattr__(b.name, b)

        self.bands = _sort_alphanum(self.bands)


    def stack(self, bands, quantiles=None, min=None, max=None, normalize=None):
        """ Stack a collection of bands.

        Args:
            bands (list): a list of band names
            quantiles (tuple): clip band values between quantiles, e.g. `[0.025, 0.975]`, defaults to `None`
            min (int): clip band values below this threshold, defaults to `None`
            max (int):  clip band values above this threshold, defaults to `None`
            normalize (func): a function to normalize band array, defaults to `None`
        Returns:
            np.array: a stack of band arrays
        """
        l = []

        for b in bands:
            a = self.__getattribute__(b).array

            if quantiles:
                qs = np.quantile(a, quantiles)
                a = np.clip(a, qs[0], qs[1])

            if min or max:
                a = np.clip(a, min, max)

            if normalize:
                a = normalize(a)
            
            l.append(a)
        
        arr = np.stack(l, axis=-1)

        return arr

