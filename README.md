# MOM6-SIS2-BGC examples
This is a repo for quick building/runing coupled ocean-ice-biogeochemistry tests.
Presently included is an experimental setup for running a global 1/2 degree MOM6-SIS2-COBALT test.

## How to compile the model (on gaea)

(cd build;  ./linux-build-mom6sis2.bash -m gaea -p intel16 -t prod )

## How to get the INPUT datasets needed for the experiments in this repo

cd exps/.datasets

#Grid specification and grid dependent forcing files (2.5GB)

(mkdir OM4p5_grid_dataset; cd OM4p5_grid_dataset; wget ftp://ftp.gfdl.noaa.gov/pub/Niki.Zadeh/OM4_datasets/OM4p5_grid_v20180227.tar.gz; tar zxvf OM4p5_grid_v20180227.tar.gz)

#Oceanbiogeochemistry initialization/flux dataset (963MB)

(mkdir OceanBGC_dataset;   cd OceanBGC_dataset;   wget ftp://ftp.gfdl.noaa.gov/pub/Niki.Zadeh/OM4_datasets/OceanBGC_dataset.tar.gz;     tar zxvf OceanBGC_dataset.tar.gz)

#CORE2 IAF focings, approximately (34GB, individual datafiles more than 2GB, takes ~1hr to get)

mkdir CORE2_IAF_1948-2009_dataset

pushd CORE2_IAF_1948-2009_dataset

wget https://data1.gfdl.noaa.gov/~nnz/mom4/COREv2/data_IAF/CORRECTED/combined_years/ncar_precip.1948-2009.23OCT2012.nc ; ln -s ncar_precip.1948-2009.23OCT2012.nc core2_precip.nc

wget https://data1.gfdl.noaa.gov/~nnz/mom4/COREv2/data_IAF/CORRECTED/combined_years/ncar_rad.1948-2009.23OCT2012.nc    ; ln -s ncar_rad.1948-2009.23OCT2012.nc    core2_rad.nc

wget https://data1.gfdl.noaa.gov/~nnz/mom4/COREv2/data_IAF/CORRECTED/combined_years/slp.1948-2009.23OCT2012.nc         ; ln -s slp.1948-2009.23OCT2012.nc         core2_slp.nc

wget https://data1.gfdl.noaa.gov/~nnz/mom4/COREv2/data_IAF/CORRECTED/combined_years/q_10.1948-2009.23OCT2012.nc        ; ln -s q_10.1948-2009.23OCT2012.nc        core2_q_10.nc

wget https://data1.gfdl.noaa.gov/~nnz/mom4/COREv2/data_IAF/CORRECTED/combined_years/t_10.1948-2009.23OCT2012.nc        ; ln -s t_10.1948-2009.23OCT2012.nc        core2_t_10.nc

wget https://data1.gfdl.noaa.gov/~nnz/mom4/COREv2/data_IAF/CORRECTED/combined_years/u_10.1948-2009.23OCT2012.nc        ; ln -s u_10.1948-2009.23OCT2012.nc        core2_u_10.nc

wget https://data1.gfdl.noaa.gov/~nnz/mom4/COREv2/data_IAF/CORRECTED/combined_years/v_10.1948-2009.23OCT2012.nc        ; ln -s v_10.1948-2009.23OCT2012.nc        core2_v_10.nc

popd

#Test, the following command returns the list of broken data links, hence should not return anything

find exps/OM4p5_CORE2_IAF_COBALT/INPUT/ -xtype l

## How to run a test for 1/2 degree model using 180 cores on gaea
cd exps/OM4p5_CORE2_IAF_COBALT

srun -n 180 ../../builds/build/gaea-intel16/ocean_ice/prod/MOM6 |& tee stdout.n180.1

