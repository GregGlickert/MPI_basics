# To run this scipt make sure MPI is loaded then run
# mpiexec -n 2 nrniv -mpi -python example4.py
# any amount of -n is supported, but two is enough to show the idea
# This script shows that some of the built in functions in pc have barriers built in. 
# while using barriers is very important it is best practice to put them only when needed
# this will maximize the speedup effectives of your mpi code
from neuron import h
import time

pc = h.ParallelContext()

MPI_RANK = int(pc.id())
N_HOSTS = int(pc.nhost())

if MPI_RANK == 0:
    on_rank_list = [1,2,3]
else:
    time.sleep(5)
    on_rank_list = [4,5,6]
    
gathered_list = pc.py_gather(on_rank_list,0)

if MPI_RANK == 0:
    print(f"RANK {MPI_RANK} gathered list {gathered_list}")
