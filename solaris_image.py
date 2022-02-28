#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 19:14:42 2022

@author: hubert
"""

import os
import skimage
import rasterio
import solaris as sol
import matplotlib.pyplot as plt
from utils.config import PROJECT_ROOT
from solaris.vector import mask
from rasterio.plot import show

# Get the project root directory
project_path = PROJECT_ROOT
RCNN_ROOT = os.path.abspath(project_path + "Mask_RCNN")
os.chdir(RCNN_ROOT)
print("Printing the current project root dir".format(os.getcwd()))

input_raster = PROJECT_ROOT + "results/Test/inputs/tile_4096-4096.tif"
predicted_raster = PROJECT_ROOT + "results/Test/predicted/tile_4096_4096.tif"

ref_image = rasterio.open(input_raster)
mask_image_rst = rasterio.open(predicted_raster)
mask_image = skimage.io.imread(predicted_raster)

geoms = mask.mask_to_poly_geojson(mask_image, channel_scaling=[1, -1, -1])

# f, ax = plt.subplots(figsize=(10, 8))
# plt.imshow(mask_image)
# plt.show()

fig, (axr, axg, axl) = plt.subplots(1, 3, figsize=(25, 9))
show(ref_image, ax=axr, title="Testing Image")
show(mask_image_rst, ax=axg, title="Pred. without Smooth Blending")
show(mask_image, ax=axl, title="Pred. with Smooth Blending")
plt.show()

# Revert the mask to the original crs and affine tranformation for matching.
result_polys = sol.vector.polygon.georegister_px_df(
    geoms, affine_obj=ref_image.transform, crs=ref_image.crs
)
# unary_union(result_polys['geometry'])
