# -*- coding: utf-8 -*-
import numpy as np
import copy
import random
def top_candidates(pop_gen,npop):
    pop_ordered=sorted(pop_gen.items(),key=lambda x: x[1]['fitness'], reverse=True)
        
    i=0
    
    temp=dict()
    for item1 in pop_ordered:
        temp[str(i)]=pop_gen[item1[0]]
        i=i+1
        if(i>npop):
            break
    return temp


def top_rand_candidates(pop_gen,npop):
     pop_ordered=sorted(pop_gen.items(),key=lambda x: x[1]['fitness'], reverse=True)
     q=np.random.permutation(npop)
     i=0
     n=round(npop*0.1)
     list_remove=[]
     temp=dict()
     for item in pop_ordered:
         temp[str(i)]=pop_gen[item[0]]
         list_remove.append(int(item[0]))
         i=i+1
         if(i>n):
             break
    
     for j in q:
         if not(j not in list_remove):
             temp[str(i)]=pop_gen[str(j)]
             i=i+1
        
         if i>npop:
             break
     return temp
 
def crowding(pop_gen,popc,npop):
    temp=dict()
    no_pieces=len(popc['0']['puzzle'])
    for i in range(npop):
        tempmin=dict()
        mindist=np.inf
        for j in range(npop):
            dist=distance(popc[str(j)],pop_gen[str(i)],no_pieces)
            if(dist<mindist):
                mindist=dist
                tempmin=popc[str(j)]
        if(pop_gen[str(i)]['fitness']>=tempmin['fitness']):
            temp[str(i)]=popc[str(i)]
        else:
            temp[str(i)]=tempmin
    
    
    
    return temp
                
 
def deterministic_crowding(pop_gen,popc,npop):
    temp=dict()
    no_pieces=len(popc['0']['puzzle'])
    i=0
    temp=copy.deepcopy(pop_gen)
    
    while(True):
        q=random.randint(0,npop-1)
        q1=random.randint(0,npop-1)
        p1=copy.deepcopy(pop_gen[str(q)])
        p2=copy.deepcopy(pop_gen[str(q1)])
        d11=distance(popc[str(i)],p1,no_pieces)
        d22=distance(popc[str(i+1)],p2,no_pieces)
        d12=distance(popc[str(i)],p2,no_pieces)
        d21=distance(popc[str(i+1)],p1,no_pieces)
        
        if d11+d22<d12+d21:
            if(popc[str(i)]['fitness']>p1['fitness']):
                temp[str(q)]=popc[str(i)]
            
            if(popc[str(i+1)]['fitness']>p2['fitness']):
                temp[str(q1)]=popc[str(i+1)]
            
        else:
            if(popc[str(i)]['fitness']>p2['fitness']):
                temp[str(q1)]=popc[str(i)]
            
            if(popc[str(i+1)]['fitness']>p1['fitness']):
                temp[str(q)]=popc[str(i+1)]
            
        i=i+2
        if i>=npop:
            break
    return temp
        
            

def distance(c_ind,p_ind,no_pieces):
    dist1=0
    for list1 in c_ind['puzzle']:
        for list2 in p_ind['puzzle']:
            if(list1[2]**2 +list1[3]**2==list2[2]**2+list2[3]**2):
                dist1=dist1+np.sqrt((list1[0]-list2[0])**2 + (list1[1]-list2[1])**2)
            
    return dist1