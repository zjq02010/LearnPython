import pymodis
import wx
import os
import gdal


pymodis.convertmodis_gdal.convertModisGDAL(
    hdfname=r"E:\MOD16A2.A2003001.h21v03.006.2017097160655.hdf",
    prefix="E:\MOD16A2.A2003001.h21v03.006.2017097160655",
    subset="(1)",
    res=0.01,
    outformat="GTiff",
    epsg=3857,
    wkt=None,
    resampl='NEAREST_NEIGHBOR',  # 重采样方法
    vrt=False
)
