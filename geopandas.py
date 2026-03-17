import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

#ler csv
df = pd.read_csv(r".\dados.csv")

#criargeodataframe
gdf = gpd.GeoDataFrame(df,
                       geometry = gpd.points_from_xy(
                           df.lon, df.lat),
                           crs = "EPSG:4326"
                       )

print(gdf.head())