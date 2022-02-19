# Downloads imagery online and saves locally.

import geopandas as gpd
import os
import gdal
from PIL import Image


# os. getcwd()
os.chdir("E:\\PlotDel_Steven\\sen_proj")


from fpackage.download_data import create_directories, split, download_sat


data_dir = "../"


# create the needed directories
create_directories(data_dir)


# In[11]:


api_key = "AIzaSyCQ47Kk5A8LD0odsoBdBTJ5HjuUp8FnV2k"  # You will need to get your own Google Maps  Static Images
# api key at some point


# In[6]:


file = "Data/area_of_interest.geojson"
save_path = data_dir + "Data/grid/"
split(file, save_path)


# In[16]:


out_path = data_dir + "Data/image/"
download_sat(out_path, save_path, api_key)


# In[18]:


# adding the metadata to the jpg images
p = gpd.read_file(save_path + "grid6.shp")
for i in range(len(p.bounds["minx"])):
    img = os.path.join(out_path + f"image_{i}.jpg")
    image = Image.open(img)
    l = image.size
    nx = l[0]
    ny = l[1]
    ds = gdal.Open(img)
    xmin, ymin, xmax, ymax = (
        p.bounds["minx"][i],
        p.bounds["miny"][i],
        p.bounds["maxx"][i],
        p.bounds["maxy"][i],
    )
    xres = (xmax - xmin) / float(nx)
    yres = (ymax - ymin) / float(ny)
    geotra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nsform = (xmin, xres, 0, ymax, 0, -yres)
    ds.SetGeoTransform(geotransform)
    ds = None
    get_ipython().system(
        'gdal_translate -of Gtiff -a_srs EPSG:4326 "../Data/image/image_{i}.jpg" "../Data/tile/tile_{i}.tif" '
    )


path = data_dir + "Data/tile/"
path_out = data_dir + "Data/out.tif"  # output path
path_out_pred = data_dir + "Data/out_pr.tif"  # output path
