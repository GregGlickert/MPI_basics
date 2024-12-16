# To run this scipt make sure MPI is loaded then run
# mpiexec -n 2 nrniv -mpi -python example3.py
# any amount of -n is supported, but two is enough to show the idea
# This script is to show an example of why a barrier is important
# if one core is taking longer than the other 
# and you have a process that takes info from all other RANKS
# you need to ensure a barrier is in place
# comment out the barrier on line 45 and see how the ouput of the script changes!

from neuron import h
import pandas as pd
import time
import glob

pc = h.ParallelContext()

MPI_RANK = int(pc.id())
N_HOSTS = int(pc.nhost())

if MPI_RANK == 0:
    data = [1,2,3]
    label = []
    for i in range(len(data)): label.append(MPI_RANK)
    data = {'RANK': label,'Fake_data': data}
    df = pd.DataFrame(data)
    df.to_csv(f"{MPI_RANK}.csv",index=False)

else:
    data = ['NULL','NULL','NULL']
    label = []
    for i in range(len(data)): label.append(MPI_RANK)
    data = {'RANK': label,'Fake_data': data}
    df = pd.DataFrame(data)
    df.to_csv(f"{MPI_RANK}.csv",index=False)
    # fake way to have one core take longer than the other
    time.sleep(5)
    data = [4,5,6]
    label = []
    for i in range(len(data)): label.append(MPI_RANK)
    data = {'RANK': label,'Fake_data': data}
    df = pd.DataFrame(data)
    df.to_csv(f"{MPI_RANK}.csv",index=False)

# without the barrier the dataframe will contain NULLS     
pc.barrier()

if MPI_RANK == 0:
    # Use glob to find all .csv files
    csv_files = glob.glob("*.csv")
    combined_df = pd.concat([pd.read_csv(file) for file in csv_files], ignore_index=True)
    print(f"Combined DataFrame: on rank {MPI_RANK}")
    print(combined_df)
    
    