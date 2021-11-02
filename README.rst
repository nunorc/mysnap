
mysnap
===========================

An experimental package with simple utilities for quickly importing
and handling ESA SNAP toolbox products in BEAM-DIMAP format.

Quick Start
---------------------------

Install package from the git repository:

.. code-block:: bash

    $ pip install git+https://github.com/nunorc/mysnap@master

Open a product, build images by stacking bands, and split in tiles.

.. code-block:: python

    import mysnap

    # product filename in beam-dimap format
    filename = '~/Products/subset_2021_resampled.dim'

    # load product from file
    product = mysnap.Product(filename)

    # check rasterized size of image and number of bands
    product.meta.ncols, product.meta.nrows, product.meta.nbands  # 2312, 2312, 43

    # get list of bands
    product.bands  # ['b1', 'b2', 'b3', ...

    # access individual band
    product.b1.name    # 'b1'
    product.b1.desc    # 'B1 (443.0)'
    product.b1.array   # array([[1731., 1731., 1731., ...
    product.b1.array.shape   # (2312, 2312)

    # build a stacked array of selected bands
    bands = ['b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b8a', 'b11', 'b12']
    arr = product.stack(bands, normalize=mysnap.normalize)
    arr.shape   # (2312, 2312, 10)

    # split stack in 64x64 tiles
    tiles = mysnap.tiles(arr, size=64)
    tiles.shape   # (1296, 64, 64, 10)

    # build a rgb image
    bands = ['b4', 'b3', 'b2']
    rgb = product.stack(bands, normalize=mysnap.normalize)

Acknowledgments
---------------------------

Raster data imported with `rasterio <https://rasterio.readthedocs.io/en/latest/>`_.
Thank you to `ESA <https://www.esa.int/>`_,
the authors of the `SNAP Toolbox <https://step.esa.int/main/toolboxes/snap/>`_,
and upstream packages and products.

