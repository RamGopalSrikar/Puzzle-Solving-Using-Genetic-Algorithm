# -*- coding: utf-8 -*-
import random
import copy
import fitnessEval as fit
import mutate
def arthematic_crossover(p1,p2,gamma,mu):
    c1=copy.deepcopy(p1)
    c2=copy.deepcopy(p2)
   
    
#    alpha=0.3
    count=0
    for list1 in p1['puzzle']:
        alpha=random.uniform(-gamma,1+gamma)
        alpha1=random.uniform(-gamma,1+gamma)
        for list2 in p2['puzzle']:
            
            if(list1[2]**2 +list1[3]**2==list2[2]**2+list2[3]**2):
                c1['puzzle'][count][0]=int(list1[0]*alpha+(1-alpha)*list2[0])
                c1['puzzle'][count][1]=int(list1[1]*alpha1+(1-alpha1)*list2[1])
                c2['puzzle'][count][0]=int(list2[0]*alpha+(1-alpha)*list1[0])
                c2['puzzle'][count][1]=int(list2[1]*alpha1+(1-alpha1)*list1[1])
                count=count+1
                break
              
        
        
    
    c1m=mutate.mutate(c1,mu)
    c2m=mutate.mutate(c2,mu)
    
    fit.fitnessEval(c1m)
    fit.fitnessEval(c2m)
            
    

    return c1m,c2m

def arith_crossover(p1,p2,gamma,mu,gen,sigma):
    #non unifrom muation
    c1=copy.deepcopy(p1)
    c2=copy.deepcopy(p2)
   
    
#    alpha=0.3
    count=0
    for list1 in p1['puzzle']:
        alpha=random.uniform(-gamma,1+gamma)
        for list2 in p2['puzzle']:
            if(list1[2]**2 +list1[3]**2==list2[2]**2+list2[3]**2):
                c1['puzzle'][count][0]=int(list1[0]*alpha+(1-alpha)*list2[0])
                c1['puzzle'][count][1]=int(list1[1]*alpha+(1-alpha)*list2[1])
                c2['puzzle'][count][0]=int(list2[0]*alpha+(1-alpha)*list1[0])
                c2['puzzle'][count][1]=int(list2[1]*alpha+(1-alpha)*list1[1])
                count=count+1
                break
              
        
        
    
    c1m=mutate.non_uniform_mutate(c1,mu,gen,sigma)
    c2m=mutate.non_uniform_mutate(c2,mu,gen,sigma)
    
    fit.fitnessEval(c1m)
    fit.fitnessEval(c2m)
            
    

    return c1m,c2m

def crossover_uniform(p1,p2,gamma,mu,gen,sigma):
    #non unifrom mutation
    c1=copy.deepcopy(p1)
    c2=copy.deepcopy(p2)
   
    
#    alpha=0.3
    count=0
    for list1 in p1['puzzle']:
        
        for list2 in p2['puzzle']:
            if(list1[2]**2 +list1[3]**2==list2[2]**2+list2[3]**2):
                if(random.uniform(0,1)<0.5):
                    c1['puzzle'][count][0]=list2[0]
                    c2['puzzle'][count][0]=list1[0]   
                    
                if(random.uniform(0,1)<0.5):
                    c1['puzzle'][count][1]=list2[1]
                    c2['puzzle'][count][1]=list1[1]
                count=count+1
                break
              
        
        
    
    c1m=mutate.non_uniform_mutate(c1,mu,gen,sigma)
    c2m=mutate.non_uniform_mutate(c2,mu,gen,sigma)
    
    fit.fitnessEval(c1m)
    fit.fitnessEval(c2m)
            
    

    return c1m,c2m

def crossover_uniform2(p1,p2,gamma,mu,gen,sigma):
    #uniform mutation
    c1=copy.deepcopy(p1)
    c2=copy.deepcopy(p2)
   
    
#    alpha=0.3
    count=0
    for list1 in p1['puzzle']:
        
        for list2 in p2['puzzle']:
            if(list1[2]**2 +list1[3]**2==list2[2]**2+list2[3]**2):
                if(random.uniform(0,1)<0.5):
                    c1['puzzle'][count][0]=list2[0]
                    c2['puzzle'][count][0]=list1[0]   
                    
                if(random.uniform(0,1)<0.5):
                    c1['puzzle'][count][1]=list2[1]
                    c2['puzzle'][count][1]=list1[1]
                count=count+1
                break
              
        
        
    
    c1m=mutate.mutate1(c1,mu)
    c2m=mutate.mutate1(c2,mu)
    
    fit.fitnessEval(c1m)
    fit.fitnessEval(c2m)
            
    

    return c1m,c2m



def crossover_self(p1,mu,gen,npop):
    count=0
    p=len(p1['puzzle'])
    c1=copy.deepcopy(p1)
    for list1 in p1['puzzle']:
        number=random.randint(0,p-1)
        while(number==count):
            number=random.randint(0,p-1)
        if(random.uniform(0,1)<=0.1):
            c1['puzzle'][number][0]=list1[0]
            c1['puzzle'][count][0]=p1['puzzle'][number][0]  
            c1['puzzle'][number][1]=list1[1]
            c1['puzzle'][count][1]=p1['puzzle'][number][1]  
            
        if(random.uniform(0,1)<=0.1):
            c1['puzzle'][count][2]=list1[3]
            c1['puzzle'][count][3]=list1[2]
        
        count=count+1
    fit.fitnessEval(c1)
    
    return c1
        
        
    
        

def crossover_binaryrep(p1,p2,gamma,mu):
    c1=copy.deepcopy(p1)
    c2=copy.deepcopy(p2)
   
    #single point crossover
#    alpha=0.3
    count=0
    for list1 in p1['puzzle']:
        point=round(random.uniform(0.4,0.7)*8)
        for list2 in p2['puzzle']:
            if(list1[2]**2 +list1[3]**2==list2[2]**2+list2[3]**2):
                if(list1[0]<0):
                    list1[0]=0
                if(list1[1]<0):
                    list1[1]=0
                if(list2[0]<0):
                    list2[0]=0
                if(list2[1]<0):
                    list2[1]=0
                p1_s1=adjust_len("{0:b}".format(list1[0]))
                p1_s2=adjust_len("{0:b}".format(list1[1]))
                p2_s1=adjust_len("{0:b}".format(list2[0]))
                p2_s2=adjust_len("{0:b}".format(list2[1]))
                
                c1_s1,c2_s1=single_point(p1_s1,p2_s1,point)
                c1_s2,c2_s2=single_point(p1_s2,p2_s2,point)
                
                #mutation
                mu=0.1
                c1m_s1=mutate.mutate3(c1_s1,mu)
                c1m_s2=mutate.mutate3(c1_s2,mu)
                c2m_s1=mutate.mutate3(c2_s1,mu)
                c2m_s2=mutate.mutate3(c2_s2,mu)
                
                
                c1['puzzle'][count][0]=int(c1m_s1,2)
                c1['puzzle'][count][1]=int(c1m_s2,2)
                c2['puzzle'][count][0]=int(c2m_s1,2)
                c2['puzzle'][count][1]=int(c2m_s2,2)
                
                count=count+1
                break
              
        
        
    
    c1m=mutate.mutate_rotate(c1,0.2)
    c2m=mutate.mutate_rotate(c2,0.2)
    
    fit.fitnessEval(c1m)
    fit.fitnessEval(c2m)
            
    

    return c1m,c2m



def adjust_len(s,l=8):
    diff=8-len(s)
    if(diff>0):
        for i in range(0,diff):
            s='0'+s
    return s

def single_point(s1,s2,point):
    
    temp1=s1[0:point]+s2[point:-1]+s2[-1]
    temp2=s2[0:point]+s1[point:-1]+s1[-1]
    
    return temp1,temp2
    
    