#!/usr/bin/env python
# Import necessary modules
from netCDF4 import Dataset
import numpy as np
import shutil
import sys, getopt

def find_index(lat,lon,lat0,lon0):
    """
    Find and return the (j,i) index of the input data arrays (lat,lon) 
    corresponding to the element closest to input (lat0,lon0). 
    """
    if(lon0 < lon.min()): 
        lon0=lon0+360.
    elif(lon0 > lon.max()): 
        lon0=lon0-360.
    
    jdx = (np.abs(lat - lat0)).argmin()
    idx = (np.abs(lon - lon0)).argmin()
    return jdx,idx
#test: 
#j,i = find_index(lon,lat,lon0,lat0)
#print(j,i,lon[i],lat[j])
#159 480 270.0 -0.280810890730407

def homogenize(var,lat,lon,lat0,lon0):
    """
    Given an input 3D array var(k,j,i) compute and return a 3D array hom(k,j,i)
    where all elements in a layer k are replaced by the same constant value
    calculated from a 4-point average of the values of input array var around the
    point closest to the input lat0,lon0.
    var: 3D array (usually with time,lat,lon axis)
    lat,lon: 1D arrays of latitudes and longitudes corresponding to the second 
    and third axis of var
    lat0,lon0: constant latitude, longitude of the point to homogenize around
    """
    j,i = find_index(lat,lon,lat0,lon0)
    hom = np.zeros_like(var)
    for k in range(0,var.shape[0]):
        hom[k] = 0.25*(var[k,j,i]+var[k,j+1,i]+var[k,j,i+1]+var[k,j+1,i+1])
    return hom


def main(argv):

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputfile", help="path to input data file", required=True, type=str)
    parser.add_argument("--outputfile", help="path to output data file", required=True, type=str)
    parser.add_argument("--variable", help="variable in the input data file to be homogenized", required=True, type=str)
    parser.add_argument("--lon0", help="longitude of the point to be homogenized around", type=float, default=-90)
    parser.add_argument("--lat0", help="lattitude of the point to be homogenized around", type=float, default=0.0)
    args = parser.parse_args()
    in_file = args.inputfile
    out_file = args.outputfile
    varname = args.variable
    lon0 = args.lon0
    lat0 = args.lat0

    shutil.copyfile(in_file,out_file)
    nc_fid = Dataset(out_file, 'r+')

    var= nc_fid.variables[varname][:]
    lon= nc_fid.variables['lon'][:]
    lat= nc_fid.variables['lat'][:]
    hom_var = homogenize(var,lat,lon,lat0,lon0)
    nc_fid.variables[varname][:] = hom_var
    nc_fid.close()


if __name__ == "__main__":
   main(sys.argv[1:])

#Usage examples:
#for var in huss prra prsn psl rlds rsds tas uas vas; do  echo $var;  homogenize_netcdf_forcings.py --inputfile JRA_$var.nc  --outputfile hom_JRA_$var.nc  --variable $var --lon0=-90. --lat0=0.0 ;done
