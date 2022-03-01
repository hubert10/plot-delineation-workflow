#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Friday May 20 16:31:20 2020

@author: hubert K.
"""
import os
import pandas as pd
import geopandas as gpd
from utils.config import PROJECT_ROOT
from utils.make_dir import create_dir
from utils.config import roi_image

# Get the project root directory
os.chdir(PROJECT_ROOT)
print("Printing the current project root dir".format(os.getcwd()))

input_raster = PROJECT_ROOT + "results/Test/refs/debi_tiguet_image/"
# input_raster = PROJECT_ROOT + "results/Test/inputs/tile_4096_4096/"
geo_raster = PROJECT_ROOT + "results/Test/savedfiles/debi_tiguet_image/"

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

input_raster = gpd.read_file(input_raster + "debi_tiguet_image.shp")
geo_raster = gpd.read_file(geo_raster + "debi_tiguet_image.shp")

raster = gpd.sjoin(input_raster, geo_raster, how="inner", predicate="within")
raster = raster.drop(["index_right"], axis=1)
print(f"Number of ground truth plots: {input_raster.shape}")
print(f"Number of predicted plots: {geo_raster.shape}")
print()
print(f"Number of plots well predicted: {len(raster)}")
print(raster.head())
