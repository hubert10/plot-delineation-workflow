"""
Created on FEB 02/02 at Manobi Africa/ ICRISAT 

@Contributors: Pierre C. Traore - ICRISAT/ Manobi Africa
          Steven Ndung'u' - ICRISAT/ Manobi Africa
          Joel Nteupe - Manobi Africa
          John bagiliko - ICRISAT Intern
          Rosmaelle Kouemo - ICRISAT Intern
          Hubert Kanyamahanga - ICRISAT/ Manobi Africa
          Glorie Wowo -  ICRISAT/ Manobi Africa
"""
import cv2
import json
import os
import PIL
import numpy as np
from datetime import datetime
from skimage import io, color
import matplotlib.pyplot as plt
import skimage.io as io
import matplotlib.image as mpimg
from tkinter import Tcl
from utils.config import CustomConfig, PROJECT_ROOT
from IPython import get_ipython

# Get the project root directory
project_path = PROJECT_ROOT
RCNN_ROOT = os.path.abspath(project_path)
os.chdir(RCNN_ROOT)

end_time = datetime.now()
now = datetime.now()  # current date and time
time = now.strftime("%m%d%Y_%H%M")
img = cv2.imread(PROJECT_ROOT + "results/Test/geo_referenced/debi_tiguet_image.tif")  # BGR
# img = cv2.imread(PROJECT_ROOT + "samples/split_images/tile22.tif")  # BGR
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

io.imsave(
    os.path.join(PROJECT_ROOT + "results/Test/geo_referenced", "RGB_tile{}{}".format(str(time), ".tif")),
    img,
)
