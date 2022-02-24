"""
@author: Steven Ndung'u' and Hubert K

"""
# ## Georeference Masks
# Example found in the workstation workflow
# The aim of this script is to convert prediction patches saved in jp, png, etc to TIF format referencing the metadata of the original satelite imagery


import rasterio as rio
import pathlib
from utils.config import CustomConfig, PROJECT_ROOT


#### Convert the PNG predictions to Rasters Tif format

# converts from png to tiff


def convert_png_to_tif_and_save(input_img_png, save_path, georef_img_tif, idx):
    # Input png image, to convert as geotiff
    img = rio.open(str(input_img_png))
    img = img.read(1)
    # img = img.astype('uint16')
    # img = np.stack((img,)*1, axis=1) #reshape to append the n channels of rgb for compatibility
    # Input image for coordinate reference
    with rio.open(
        str(georef_img_tif)
        + "/"
        + str(input_img_png).replace("jpg", "tif").split("/")[-1]
    ) as naip:
        # open georeferenced.tif for writing

        with rio.open(
            str(save_path)
            + "/"
            + "{}.tif".format(str(input_img_png).split("/")[-1].split(".")[0]),
            "w",
            driver="GTiff",
            count=1,
            height=img.shape[0],
            width=img.shape[1],
            dtype=img.dtype,
            crs=naip.crs,
            transform=naip.transform,
        ) as dst:
            dst.write(img, indexes=1)


# Set the paths
# path of png or jpg image predicted from  smoothing algorithm
input_img_png = PROJECT_ROOT + "results/Test/pred_image/"
input_img_png = pathlib.Path(input_img_png)

# folder with original raster image (from original tif)
georef_img_tif = PROJECT_ROOT + "results/Test/ref_image/"
georef_img_tif = pathlib.Path(georef_img_tif)

# Path to save the outputs
save_path = PROJECT_ROOT + "results/Test/geo_referenced/"
save_path = pathlib.Path(save_path)
input_img_png, georef_img_tif, save_path

# Import the images, convert them to tif and save back in defined folder

images = list(input_img_png.glob("*"))

for idx, val in enumerate(images):
    convert_png_to_tif_and_save(str(val), save_path, georef_img_tif, idx)
