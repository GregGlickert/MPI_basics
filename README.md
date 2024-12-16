# MPI_basics
## A repo showing off some examples of using MPI with the NEURON software
### Each .py file has a header that briefly discusses the script
#### All the scripts are set up to be ran on the command line. MPI will need to be loaded before running the scripts. This loading of MPI will be different on each HPC. You can run the command
```
module avail
```
#### on your HPC and look for what the MPI module is called on your HPC. It should be something like openmpi, mpich or intel_mpi, but this will depend on the computer. Then load the module with the command
```
module load MODULE_NAME
```
 It is possible the MPI is already loaded on your computer this can be especially true if you are running on a local computer. Just try running either
``` 
mpiexec --version
``` 
or 
```
mpirun --version
```
#### If one  of those commands works then you are set up with MPI loaded. Then to run the examples in this repo use the command
``` 
mpiexec -n 2  nrniv -mpi -python exampleX.py 
``` 
#### replacing X with the example number you would like to run.
