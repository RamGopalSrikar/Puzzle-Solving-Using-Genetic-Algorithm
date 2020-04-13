
import numpy as np
import puzzleDraw as pd
import crossover as cr
import parent_selection as ps
import copy
import json



def version_one(npop,gen,pop_dict,high_fitness_org,mu):
    
    pop_gen=copy.deepcopy(pop_dict)
    temp=dict()
    bestsolution=dict()
    high_fitness=copy.deepcopy(high_fitness_org)
    avg_fit=[]
    high_fit=[]
    org_gen=copy.deepcopy(gen)
    sigma=5
    count_m=0
    while(gen>0):
        
        gen=gen-1
        popc=dict()
        popp=dict()
        count=0
        count2=npop
        count1=0
        fitness_sum=0
        pdf=[0 for i in range(0,npop)]
        cdf=[0 for i in range(0,npop)]
        for item in pop_gen.values():
            fitness_sum=fitness_sum+item['fitness']
        m=0
        for it in pop_gen.values():
            cdf[m]=it['fitness']/fitness_sum
            if(m>0):
                pdf[m]=pdf[m-1]+cdf[m]
            else:
                pdf[m]=cdf[m]
            m=m+1
            if(m>=npop):
                break
            
        pdf[m-1]=1  
        #diversity calculation
#        sr=diversity(pop_gen,cdf,npop)
#        diver_val.append(sr)
#        print('diversity :{}'.format(sr))
        for j in range(npop//2):
            p1,p2=ps.exponential_ranking(pop_gen,npop,cdf)
            gamma=0.1
            c1,c2=cr.crossover_uniform(p1,p2,gamma,mu,org_gen-gen,sigma)
            
            if(c1['fitness']>high_fitness):
                bestsolution=copy.deepcopy(c1)
                high_fitness=c1['fitness']
                
            if(c2['fitness']>high_fitness):
                bestsolution=copy.deepcopy(c2)
                high_fitness=c2['fitness']
            
            popc[str(count)]=copy.deepcopy(c1)
            popc[str(count+1)]=copy.deepcopy(c2)
            count=count+2
            
            pop_gen[str(count2)]=copy.deepcopy(c1)
            pop_gen[str(count2+1)]=copy.deepcopy(c2)
            count2=count2+2
            
            popp[str(count1)]=copy.deepcopy(p1)
            popp[str(count1+1)]=copy.deepcopy(p2)
            count1=count1+2
        
        pop_ordered=sorted(pop_gen.items(),key=lambda x: x[1]['fitness'], reverse=True)
        
        i=0
        temp.clear()
        
        for item1 in pop_ordered:
            temp[str(i)]=pop_gen[item1[0]]
            i=i+1
            if(i>npop):
                break
#        temp=ss.deterministic_crowding(pop_gen1,popc,npop)   
        pd.draw2(json.dumps(temp[str(0)]))
        print('highest fitness :{} for generation {}'.format(temp[str(0)]['fitness'],org_gen-gen))        
        pop_gen.clear()
        pop_gen=copy.deepcopy(temp)
        
        avg_fitness=0
        
        for item in pop_gen.values():
            avg_fitness=avg_fitness+item['fitness']
        
        avg_fit.append(avg_fitness/npop)
        high_fit.append(pop_gen[str(0)]['fitness'])
        k=len(high_fit)
        if(k>1):
            if(high_fit[-1]==high_fit[-1]):
                count_m+=1
                if(count_m>=10):
                    if(sigma>0.1):
                        sigma=sigma-0.1
                        print('sigma changed to {}'.format(sigma))
                    else:
                        sigma=0.1
            else:
                count_m=0
        
        
    
    print('best fit graphical')    
    pd.draw2(json.dumps(pop_gen[str(0)]))
    
    return high_fit,avg_fit
            
                
def diversity(pop_gen,cdf,npop):
    tou=0
    no_pieces=len(pop_gen['0']['puzzle'])
    for i in range(npop):
        for j in range(npop):
            k=distance(pop_gen[str(i)],pop_gen[str(j)],no_pieces)**2
            tou=tou+cdf[i]*cdf[j]*(k)
        
    
    return tou
    

def distance(c_ind,p_ind,no_pieces):
    dist1=0
    
    for list1 in c_ind['puzzle']:
        for list2 in p_ind['puzzle']:
            if(list1[2]**2 +list1[3]**2==list2[2]**2+list2[3]**2):
                dist1=dist1+np.sqrt((list1[0]-list2[0])**2 + (list1[1]-list2[1])**2)
            
    return dist1     