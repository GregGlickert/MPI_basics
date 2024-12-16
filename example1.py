# To run this scipt make sure MPI is loaded then run
# mpiexec -n 2 nrniv -mpi -python example1.py
# any amount of -n is supported, but two is enough to show the idea
# You can change the rank_to_broadcast
# This scipt is to show that you can take info from 1 RANK and give that python object
# to all other RANKS. 
from neuron import h

pc = h.ParallelContext()

MPI_RANK = int(pc.id())
N_HOSTS = int(pc.nhost())

if MPI_RANK == 0:
    on_rank_list = [1,2,3,4]
else:
    on_rank_list = [6,7,8,9]

rank_to_broadcast = 0 # change the rank to see how the print out changes
broadcasted_list = pc.py_broadcast(on_rank_list,rank_to_broadcast)

print(f"{MPI_RANK} rank list contains {broadcasted_list}")
    