
import logging

logger = logging.getLogger(__name__)

import numpy as np

def normalize(x, factor=None):
    """ Normalize an array of values.

    Args:
        factor (float): a normalizing factor, defaults to max array value
    Returns:
        np.array: a normalized array
    """
    if factor:
        return x / factor
    else:
        return x / np.amax(x)

def tiles(arr, size=64, same=True):
    """ Split a multidimensional array in tiles of a given size.

    Args:
        arr (array): a multidimensional array
        size (int): size of the tile in pixels, defaults to 64
        same (bool): keep only tiles that have the given size, defaults to `True`
    Returns:
        np.array: an array of tiles
    """
    tiles = []

    for i in range(0, arr.shape[0], size):
        for j in range(0, arr.shape[1], size):
            tiles.append(arr[i:i+size, j:j+size, :])

    if same:
        tiles = [t for t in tiles if t.shape[0]==size and t.shape[1]==size]

    return np.array(tiles)

