## Here's how to compile the ocean-ice model (MOM6-SIS2 on gaea)
(cd builds;  ./linux-build.bash -m gaea -p ncrc5.intel23 -t repro -f mom6sis2 )

## MOM6SIS2COBALT Single-column model

### Get the INPUT datasets needed for the experiment
#### Grid and grid dependent input files
(mkdir -p exps/datasets/grids; cd exps/datasets/grids; wget ftp://ftp.gfdl.noaa.gov/pub/Niki.Zadeh/OM4_datasets/OM4_single_column_grid.tar.gz; tar zxvf OM4_single_column_grid.tar.gz)

#### IC
(mkdir -p exps/datasets/; cd exps/datasets/; wget ftp://ftp.gfdl.noaa.gov/perm/Alistair.Adcroft/MOM6-testing/obs.tgz; tar zxvf obs.tgz)

#### CORE2 NYF Forcing files(854MB)
(mkdir -p exps/datasets/forcings; cd exps/datasets/forcings; wget ftp://ftp.gfdl.noaa.gov/perm/Alistair.Adcroft/MOM6-testing/CORE.tgz; tar xvf CORE.tgz)

#### Oceanbiogeochemistry initialization/flux dataset (963MB)
Needed only for COBALT experiments
(mkdir -p exps/datasets/OceanBGC_dataset;   cd exps/datasets/OceanBGC_dataset;   wget ftp://ftp.gfdl.noaa.gov/pub/Niki.Zadeh/OM4_datasets/OceanBGC_dataset.tar.gz;     tar zxvf OceanBGC_dataset.tar.gz)

### Check all data is available for the single_column experiment
cd exps/MOM6SIS2COBALT.single_column

find INPUT/ -xtype l

Note: If data_table points to data_table.CORE2 then INPUT/JRA_* links need not be present

### Run the single_column experiment (1 core on gaea)
cd exps/MOM6SIS2COBALT.single_column; mkdir RESTART

srun -n 1 ../../builds/build/gaea-ncrc5.intel23/ocean_ice/repro/MOM6SIS2 |& tee stdout.ncrc5.intel23.repro.n1

## MOM6SIS2COBALT Global 1/2 degree model

### Get the INPUT datasets needed for the experiment
#### Grid and grid dependent input files
(mkdir -p exps/datasets/grids; cd exps/datasets/grids; wget ftp://ftp.gfdl.noaa.gov/pub/Niki.Zadeh/OM4_datasets/OM4global_p5.tar.gz; tar zxvf OM4global_p5.tar.gz)

#### IC
(mkdir -p exps/datasets/; cd exps/datasets/; wget ftp://ftp.gfdl.noaa.gov/perm/Alistair.Adcroft/MOM6-testing/obs.tgz; tar zxvf obs.tgz)

#### CORE2 NYF Forcing files(854MB)
(mkdir -p exps/datasets/forcings; cd exps/datasets/forcings; wget ftp://ftp.gfdl.noaa.gov/perm/Alistair.Adcroft/MOM6-testing/CORE.tgz; tar xvf CORE.tgz)

#### Oceanbiogeochemistry initialization/flux dataset (963MB)
Needed only for COBALT experiments
(mkdir -p exps/datasets/OceanBGC_dataset;   cd exps/datasets/OceanBGC_dataset;   wget ftp://ftp.gfdl.noaa.gov/pub/Niki.Zadeh/OM4_datasets/OceanBGC_dataset.tar.gz;     tar zxvf OceanBGC_dataset.tar.gz)

### Check all data is available for the single_column experiment
cd exps/MOM6SIS2COBALT.global_halfdegree

find INPUT/ -xtype l

### Run the global 1/2 degree experiment (128 core)
cd exps/MOM6SIS2COBALT.global_halfdegree; mkdir RESTART

#### gaea-ncrc5 machine with intel comiler
srun -n 128 ../../builds/build/gaea-ncrc5.intel23/ocean_ice/repro/MOM6SIS2 |& tee stdout.ncrc5.intel23.repro.n128

#### amdbox with nvhpc compiler (runs out of memory)
source ../../builds/lscamd50/nvhpc23.7.env ; mpirun -n 128 ../../builds/build/lscamd50-nvhpc23.7//ocean_ice/repro/MOM6SIS2 | & tee stdout.lscamd50.nvhpc23.7.repro.n128

