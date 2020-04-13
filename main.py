# -*- coding: utf-8 -*-

# NAME:RAM GOPAL SRIKAR KATAKAM
# STUDENT ID: 40106010
import version_one as one
from generator import generate
import json
import fitnessEval as fit
import puzzleDraw as pd
import matplotlib.pyplot as plt
import statistics as st
import numpy as np
import random

#paramter tuning
npop=300
gen=400
    
#plotting details
best_fitness1=[]
avg_fitness1=[]
mean_bestfit1=[]
stddev_bestfit1=[]
mean_avgfit1=[]
stddev_avgfit1=[]

#no of runs
run=3   
#puzzle gneration

for i in range(0,run):
    print('run {}'.format(i))
    random.seed(100*(i+1))
    generate(npop)
    with open("population.json",'r') as o:
        pop_dict=json.loads(o.read())
    
    with open("solution.json",'r') as o:
        pop_sol=json.loads(o.read())
    
    high_fitness=0          
    for j in range(0,npop):
        fit.fitnessEval(pop_dict[str(j)])
        if(pop_dict[str(j)]['fitness']>high_fitness):
            key_value=i
            high_fitness=pop_dict[str(j)]['fitness']
    
    print('{} run '.format(i))
    print('version one')
    pd.draw2(json.dumps(pop_dict[str(key_value)]))
    pd.draw2(json.dumps(pop_sol))
    best1,avg1=one.version_one(npop,gen,pop_dict,high_fitness,0.1)
    best_fitness1.append(best1)
    avg_fitness1.append(avg1)

for i in range(0,gen):
    x1=np.asarray(best_fitness1)
    y1=np.asarray(avg_fitness1)
    mean_bestfit1.append(st.mean(x1[:,i]))
    stddev_bestfit1.append(st.stdev(x1[:,i]))
    
    mean_avgfit1.append(st.mean(y1[:,i]))
    stddev_avgfit1.append(st.stdev(y1[:,i]))
    


plt.plot(mean_bestfit1,'r--')
plt.xlim(0,gen)
plt.xlabel('generations')
plt.ylabel('mean')
plt.title('(GA)  version mean of maximum fitness')
plt.grid(True)
plt.legend()
plt.show()     

plt.plot(stddev_bestfit1,'r--')
plt.xlim(0,gen)
plt.xlabel('generations')
plt.ylabel('standered deviation')
plt.title('(GA)  version  standered deviation of maximum  fitness')
plt.grid(True)
plt.legend()
plt.show()  

plt.plot(mean_avgfit1,'r--')
plt.xlim(0,gen)
plt.xlabel('generations')
plt.ylabel('mean')
plt.title('(GA)  version  mean of average fitness')
plt.grid(True)
plt.legend()
plt.show()     

plt.plot(stddev_avgfit1,'r--')
plt.xlim(0,gen)
plt.xlabel('generations')
plt.ylabel('standered deviation')
plt.title('(GA)  version standered deviations of average fitness')
plt.grid(True)
plt.legend()
plt.show()  


    

        



    



    

