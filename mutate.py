# -*- coding: utf-8 -*-
import numpy as np
from random import gauss
from random import random
import copy

def mutate(C,mu):
    Cm=copy.deepcopy(C)
    
    count=0
    length=C['length']
    width=C['width']
    val1=round(mu*length)
    val2=round(mu*width)
    for list1 in C['puzzle']:
        if(np.random.uniform(0,1)<=mu):
            Cm['puzzle'][count][2]=list1[3]
            Cm['puzzle'][count][3]=list1[2]
            Cm['puzzle'][count][1]=list1[1]+random.randint(-val2,val2)
            Cm['puzzle'][count][0]=list1[0]+random.randint(-val1,val1)
            
            if(Cm['puzzle'][count][0]>list1[3]):
                Cm['puzzle'][count][0]=list1[3]
            elif(Cm['puzzle'][count][0]<0):
                Cm['puzzle'][count][0]=0
                
            if(Cm['puzzle'][count][1]>list1[2]):
                Cm['puzzle'][count][1]=list1[2]
            elif(Cm['puzzle'][count][1]<0):
                Cm['puzzle'][count][1]=0
                
                
                
        count=count+1
        

    return Cm

def mutate1(C,mu):
    Cm=copy.deepcopy(C)
    
    count=0
    
    for list1 in C['puzzle']:
        if(np.random.uniform(0,1)<=mu):
            Cm['puzzle'][count][2]=list1[3]
            Cm['puzzle'][count][3]=list1[2]
            Cm['puzzle'][count][1]=list1[1]+np.random.randint(-20,20)
            Cm['puzzle'][count][0]=list1[0]+np.random.randint(-20,20)
        count=count+1
        

    return Cm

def mutate_binary(C_s,mu):
    Cm_s=''
    for i in range(len(C_s)):
        r=np.random.uniform(0,1)
        if(r<=mu):
            if(C_s[i]=='0'):
                Cm_s=Cm_s+'1'
            else:
                Cm_s=Cm_s+'0'
        else:
            Cm_s=Cm_s+C_s[i]
        
        
    
    return Cm_s


def mutate_rotate(C,mu):
    Cm=copy.deepcopy(C)
    
    count=0
    for list1 in C['puzzle']:
        if(np.random.uniform(0,1)<=mu):
            Cm['puzzle'][count][2]=list1[3]
            Cm['puzzle'][count][3]=list1[2]
        count=count+1
    return Cm

def non_uniform_mutate(C,mu,gen,sigma):
    Cm=copy.deepcopy(C)
    count=0
    for list1 in C['puzzle']:
        if(np.random.uniform(0,1)<=mu):
               Cm['puzzle'][count][2]=list1[3]
               Cm['puzzle'][count][3]=list1[2]
               Cm['puzzle'][count][1]=round(list1[1]+gauss(0.5,sigma))
               Cm['puzzle'][count][0]=round(list1[0]+gauss(0.5,sigma))
        
        count=count+1
    return Cm
    
    
    
    