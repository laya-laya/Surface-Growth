# -*- coding: utf-8 -*
import numpy as np
import random
import matplotlib.pyplot as plt
size = 200
L=np.zeros(size)
time = size*100
average=np.zeros(time)

T=np.zeros(time)

def index(r):
    a= min(L[r],L[(r+1)%size],L[(r-1)%size])
    if L[r] == a and L[(r+1)%size] != a and L[(r-1)%size] != a :
            i=r
    elif L[r] != a and L[(r+1)%size] == a and L[(r-1)%size] != a:
            i=(r+1)%size
            
    elif L[r] != a and L[(r+1)%size] != a and L[(r-1)%size] ==a:
            i = (r-1)%size
            
    elif L[r] ==a and L[(r+1)%size] ==a and L[(r-1)%size] != a:
        z= random.uniform(0,1)
        if z<0.5:
                i=r
        else:
                i=(r+1)%size
    elif L[r]==a and L[(r+1)%size] != a and L[(r-1)%size] == a:
        z=random.uniform(0,1)
        if z<0.5:
                i=r
                
        else:
            
            
                i=(r-1)%size
                
    elif L[r] != a and L[(r+1)%size] == a and L[(r-1)%size] == a:
        z=random.uniform(0,1)
        if z<0.5:
                i=(r-1)%size
                
        else:
                i=(r+1)%size
                
    elif L[r]==a and L[(r+1)%size] ==a and L[(r-1)%size] == a:
            
            i=r
            
    return i
for t in range(0,int(time/4)):
    
    r=int(random.uniform(0,size))
    i=index(r)
    L[i]=L[i]+1
    plt.scatter(i,L[i],color='gray',marker='s' , s=5)


for t in range(int(time/4),int(time/2)):
    
    r=int(random.uniform(0,size))
    i=index(r)
    L[i]=L[i]+1
    plt.scatter(i,L[i],color='black',marker='s' , s=5)

for t in range(int(time/2),int(3*time/4)):
    
    r=int(random.uniform(0,size))
    i=index(r)
    L[i]=L[i]+1
    plt.scatter(i,L[i],color='white',marker='s' , s=5)
   
            
            
for t in range(int(3*time/4),time):
    
    r=int(random.uniform(0,size))
    i=index(r)
    L[i]=L[i]+1
    plt.scatter(i,L[i],color='gray',marker='s' , s=5)
        
        
            
         
        
        
            
    
                
            
        
    
            
    
        
            
        
            
       