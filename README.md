# BASpy

`baspy` is a python package to make it easier to analyse large climate datasets
using Xarray (http://xarray.pydata.org), or Iris (http://scitools.org.uk/iris/), 
or any other python package that can read in netcdf/PP/grib/HDF files.

### 1. Setup package

Package is now pip installable.

```bash
    $> git clone https://github.com/sdat2/baspy.git
    $> git checkout dev
    $> cd baspy
    $> pip install -e .
```

### 2. Define the directory and filename structures of your local datasets

See and edit datasets.py

Once you have set this up all file loading should become transparent

### 3. Usage

Reading data:

```python
    import baspy as bp
 
    ### Retrieve a filtered version of the CMIP5 catalogue as a Pandas DataFrame
    df = bp.catalogue(dataset='cmip5', Model='HadGEM2-CC', RunID='r1i1p1', 
                        Experiment='historical', Var=['tas', 'pr'], 
                        Frequency='mon')

    ### Iterate over rows in catalogue
    for index, row in df.iterrows():

        ### In Xarray
        ds = bp.open_dataset(row)

        ### Or... In Iris
        cubes = bp.get_cube(row)
```

Other Examples:

- [BASpy with Xarray (Notebook)](https://scotthosking.com/notebooks/baspy_using_xarray/)
