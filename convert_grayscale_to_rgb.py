import cv2
import os
from datetime import datetime
from skimage import io
import skimage.io as io
from utils.config import PROJECT_ROOT

# Get the project root directory
project_path = PROJECT_ROOT
RCNN_ROOT = os.path.abspath(project_path)
os.chdir(RCNN_ROOT)
path_to_image = PROJECT_ROOT + "results/Test/geo_referenced/gray_debi_tiguet_image.tif"
end_time = datetime.now()
now = datetime.now()  # current date and time
time = now.strftime("%m%d%Y_%H%M")
img = cv2.imread(path_to_image)  # BGR
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

io.imsave(
    os.path.join(
        PROJECT_ROOT + "results/Test/geo_referenced",
        "RGB_{}{}{}".format(str(path_to_image).split("/")[-1].split("/")[0], str(time), ".tif"),
    ),
    img,
)
