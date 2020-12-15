# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 01:09:39 2018

@author: lili
"""

import numpy as np
import random
import matplotlib.pyplot as plt
size = 200

time = size*30000
average=np.zeros(30000)
std=np.zeros(30000)
T=np.zeros(30000)

for i in range(0,60):
    count=0
    L=np.zeros(size)                
    for t in range(0,time):
        
        r=int(random.uniform(0,size))
        h= max(L[r],L[(r+1)%size],L[(r-1)%size])
        if L[r] == h and L[(r+1)%size] != h and L[(r-1)%size] != h :
        
            L[r]=L[r]+1
        
        
        elif L[r] != h and L[(r+1)%size] == h and L[(r-1)%size] != h:
        
            L[r]=L[(r+1)%size]
        elif L[r] != h and L[(r+1)%size] != h and L[(r-1)%size] == h:
        
            L[r] = L[(r-1)%size]
        elif L[r] == h and L[(r+1)%size] == h and L[(r-1)%size] != h:
        
            z= random.uniform(0,1)
            if z<0.5:
            
                L[r]=L[r]+1
            else:
                L[r]=L[(r+1)%size]
            
        elif L[r]== h and L[(r+1)%size] != h and L[(r-1)%size] == h:
            z=random.uniform(0,1)
            if z<0.5:
                L[r]=L[r]+1
                
            else:
            
                L[r]=L[(r-1)%size]
        elif L[r] != h and L[(r+1)%size] == h and L[(r-1)%size] == h:
            z=random.uniform(0,1)
            if z<0.5:
                L[r]=L[(r-1)%size]
                
            else:
                L[r]=L[(r+1)%size]
        elif L[r]== h and L[(r+1)%size] == h and L[(r-1)%size] == h:
            
            L[r]=L[r]+1
        
        
        if t%size == 0:
            average[count] += np.average(L)
            std[count]+=np.std(L)
            T[count]=count
            count=count+1
    
average=average/60

std= std/60  
    
plt.plot(np.log(T),np.log(std))

g=open("12.txt" , "w")
for j in range(0,count):
    g.write(str(std[j]))
    g.write("\n")
g.close()
g=open("123.txt" , "w")
for j in range(0,count):
    
    g.write(str(T[j]))
    g.write("\n")
g.close()       
    
g=open("124.txt" , "w")
for j in range(0,count):
    g.write(str(average[j]))
    g.write("\n")
g.close()        
    