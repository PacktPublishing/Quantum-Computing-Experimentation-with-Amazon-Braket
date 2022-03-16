#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Chapter 10 - Amazon Braket Hybrid Jobs, Pennylane and Containers
#© 2021, 2022 Packt Publishing

#Written by Alex Khan

#QAOA.py 
#use with Chapter 10 - Amazon Braket Hybrid Jobs, Pennylane and Containers.ipynb


# In[1]:


def param_optimizer_device(param1, param2, Q, shots,device):
    lowest_energy=999999
    lowest_param1=0
    lowest_param2=0
    D=np.zeros((len(param1),len(param2)))
    E=[]

    for p1 in range(len(param1)):
        for p2 in range(len(param2)):

            qc=Circuit()
            
            for i in range(len(Q)):
                if Q[i,i]!=0:
                    #print(i,Q[i,i])
                    qc=qc.x(i).h(i)
            
            for i in range(len(Q)):
                if Q[i,i]!=0:
                    qc=qc.rz(i,-2*param1[p1]*Q[i,i])
            for i in range (len(Q)):
                for j in range (len(Q)):
                    if i<j:
                        if Q[i,j]!=0:
                            if device.name=='Aspen-11' or device.name=='Aspen-M-1':
                                qc=qc.cnot(i, j).rz(j, param1[p1]*Q[i,j]).cnot(i, j)
                            else:
                                qc=qc.zz(i,j,2*param1[p1]*Q[i,j])
            for i in range(len(Q)):
                if Q[i,i]!=0:
                    qc=qc.rx(i,2*param2[p2])
            
            task = device.run(qc, shots=shots)
            counts=task.result().measurement_counts

            
            solution=[]
            quantity=[]
            energy=[]
            for keys,values in zip(counts.keys(),counts.values()):
                solution.append(keys)
                quantity.append(values)
                energy.append(sum_energy(Q,keys))
            index=np.argsort(energy)

            D[p1,p2]=energy[index[0]]
            E.append(energy[index[0]])

            if energy[index[0]]<lowest_energy:
                lowest_energy=energy[index[0]]
                lowest_param1=param1[p1]
                lowest_param2=param2[p2]
       
    return(E, lowest_param1, lowest_param2, lowest_energy)


# In[ ]:


def optimize_bqm_device(param1, param2, Q, shots, device):
    
    qc=Circuit()
    # below is specifically for Aspen-M1- matrix
    for i in range(len(Q)):
        if Q[i,i]!=0:
            qc=qc.x(i).h(i)
    # use the code below for most situations
    #qc=qc.x(range(len(Q))).h(range(len(Q)))

    for p in range(len(param1)):
        for i in range(len(Q)):
            if Q[i,i]!=0:
                qc=qc.rz(i,-2*param1[p]*Q[i,i])
        for i in range (len(Q)):
            for j in range (len(Q)):
                if i<j:
                    if Q[i,j]!=0:
                        if device.name=='Aspen-11'or device.name=='Aspen-M-1':
                            qc=qc.cnot(i, j).rz(j, param1[p]*Q[i,j]).cnot(i, j)
                        else:
                            qc=qc.zz(i,j,2*param1[p]*Q[i,j])
        for i in range(len(Q)):
		if Q[i,i]!=0:
                qc=qc.rx(i,2*param2[p])
    
        task = device.run(qc, shots=shots)
        counts=task.result().measurement_counts
        solution=[]
        quantity=[]
        energy=[]
        for keys,values in zip(counts.keys(),counts.values()):
            solution.append(keys)
            quantity.append(values)
            energy.append(sum_energy(Q,keys))
        index=np.argsort(energy)
   
    return(energy[index[0]], solution[index[0]])


# In[3]:


def sum_energy(Q,array):
    vals=[]
    for i in range(len(array)):
        if array[int(i)]=='1':
            vals.append(i)
            
    sum=0
    #print(vals)
    for i in (vals):
        sum+=Q[int(i),int(i)]
    for i in (vals):
        for j in (vals):
            if i<j:
                sum+=Q[int(i),int(j)]
    return(sum)


# In[10]:


import os
import numpy as np
import json
from braket.aws import AwsDevice
from braket.circuits import Circuit
from braket.jobs import save_job_result


def start_here():
    

    print("Test job started!!!!!")
  
    # load input hyperparameters
    hp_file = os.environ["AMZN_BRAKET_HP_FILE"]
    
    print('hyperparameter file:',hp_file)
    
    with open(hp_file, "r") as f:
        hyperparams = json.load(f)
    start = float(hyperparams["start"])
    end = float(hyperparams["end"])
    step = float(hyperparams["step"])
    shots = int(hyperparams["shots"])
    matrix = (hyperparams["matrix"])
    
    #create QAOA parameter range
    param=np.arange(start,end,step,dtype=float)
    print('QAOA param range:',param)
    
    input_dir = os.environ["AMZN_BRAKET_INPUT_DIR"]
    
    filename = f"{input_dir}/input/{matrix}.csv"
    
    print("Loading dataset from:", filename)
    
    file = open(filename)
    Q = np.loadtxt(file, delimiter=",")
    file.close()
    print(Q)
 
    
    device = AwsDevice(os.environ["AMZN_BRAKET_DEVICE_ARN"])
    E, ideal_param1, ideal_param2, lowest_energy=param_optimizer_device(param, param, Q, shots, device)
    print(ideal_param1, ideal_param2, lowest_energy)
    print(E)
    
    print('running optimize_bqm:')
    best_energy, best_solution=optimize_bqm_device([ideal_param1,ideal_param1], [ideal_param2,ideal_param2], Q, shots*10, device)    

    print(best_energy, best_solution)
    
    save_job_result({ "E": E ,"ideal_param1": ideal_param1,"ideal_param2": ideal_param2,"lowest_energy": lowest_energy,  
                    "best_energy": best_energy, "best_solution": best_solution})
    
    print("Test job completed!!!!!")


# In[ ]:




