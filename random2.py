
import numpy as np
import random
import matplotlib.pyplot as plt
size = 200
L=np.zeros(size)
time = size*10000
average=np.zeros(10000)
std=np.zeros(10000)
T=np.zeros(10000)

for i in range(0,50):
    count=0
    L=np.zeros(size)
    for t in range(0,time):
    
        r=int(random.uniform(0,size))
    
        L[r]=L[r]+1
        
        if t % 10*size == 0:
            average[count] += np.average(L)
            std[count]+=np.std(L)
            T[count]=count
            count=count+1
   # -------------------------------------------------
   # groji e graphici
   
    #if t >= 0 and t < 25*size:
     #   plt.scatter(r,L[r],color='gray',marker='s' , s=5)
    #if t >= 25*size and t <= 50*size:
     #   plt.scatter(r,L[r],color='white',marker='s' , s=5)
    #if t >= 50*size and t <= 75*size:
       # plt.scatter(r,L[r],color='black',marker='s' , s=5)
   # if t >= 75 and  t < 100*size:
      #  plt.scatter(r,L[r],color='gray',marker='s' , s=5)
 
  #----------------------------------------------------------
average=average/50

std= std/50    

#plt.scatter(np.log(T),np.log(std))

g=open("laya.txt" , "w")
for j in range(0,count):
    g.write(str(std[j]))
    g.write("\n")
g.close()
g=open("layaa.txt" , "w")
for j in range(0,count):
    
    g.write(str(T[j]))
    g.write("\n")
g.close()