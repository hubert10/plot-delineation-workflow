"""
The code here hepls at cleaning grayscale image to
whitten image and darken other parts
"""
import os
import numpy as np
import skimage
from os import listdir
from os.path import isfile
from tkinter import *
from tkinter import Tcl
import skimage.io as io
import pandas as pd
from utils.config import PROJECT_ROOT
from scipy import ndimage

# Get the project root directory
project_path = PROJECT_ROOT
os.chdir(PROJECT_ROOT)


def whitten_image_darken_else_filtering(input_img_path, save_path):
    """
    This function is used to filter the image directly after it is out from the deep learning
    """
    nlyTIFF = [
        os.path.join(input_img_path, f)
        for f in listdir(input_img_path)
        if isfile(os.path.join(input_img_path, f)) and f.endswith(".jpg")
    ]
    nlyTIFF = Tcl().call("lsort", "-dict", nlyTIFF)

    if len(nlyTIFF) >= 2:
        for i in range(len(nlyTIFF)):
            grayscale = io.imread(nlyTIFF[i], plugin="matplotlib")
            median_filtered = ndimage.median_filter(grayscale, size=3)
            threshold = skimage.filters.threshold_li(median_filtered)
            predicted = np.uint8(median_filtered > threshold) * 255
            io.imsave(
                os.path.join(save_path, "predict_{}.tif".format(int(i))), predicted
            )

    elif len(nlyTIFF) == 1:
        from PIL import Image
        Image.MAX_IMAGE_PIXELS = 1000000000
        grayscale = io.imread(nlyTIFF[0], plugin="matplotlib")
        median_filtered = ndimage.median_filter(grayscale, size=3)
        threshold = skimage.filters.threshold_li(grayscale)
        predicted = np.uint8(median_filtered > threshold) * 255
        io.imsave(os.path.join(save_path, "predict.tif"), predicted)
    else:
        print("No jpg file given in the path provided")


input_path = PROJECT_ROOT + "results/Test/pred_image/"
save_path = PROJECT_ROOT + "results/Test/final/"
# Function call
whitten_image_darken_else_filtering(input_path, save_path)
