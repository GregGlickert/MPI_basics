# To run this scipt make sure MPI is loaded then run
# mpiexec -n 2 nrniv -mpi -python example2.py
# any amount of -n is supported, but two is enough to show the idea
# you can change the rank that is gathered
# This scipt will take all of info from every RANK and gather it onto a single RANK
# the example has it as a list but any python object should work
from neuron import h

pc = h.ParallelContext()

MPI_RANK = int(pc.id())
N_HOSTS = int(pc.nhost())

on_rank_list = [f"Hi! am i am the info on RANK {MPI_RANK}"]

rank_to_gather_on = 0 # change change me if you want 
gathered_list = pc.py_gather(on_rank_list,rank_to_gather_on)
print(f"{MPI_RANK} Rank has on rank list {on_rank_list} and gathered list {gathered_list }")
