#EE 511 - Project 1
#Question 2 [So Unfair]

import sys
import random
import numpy as np
import matplotlib.pyplot as plt 

heads = [4, 11, 8, 8, 9, 10, 9, 7, 10, 11, 11, 10,7, 8, 8, 10, 6, 8, 6, 6, 10, 10, 9, 11, 9, 10, 10, 7, 11, 10, 10, 6, 7, 9, 7, 9, 11, 9, 9, 7, 11, 10, 10, 2, 8, 11, 11, 9, 5, 11]
print(heads)
X=np.arange(1,51,1)
plt.subplot(3,1,1)                               #Scatter Plot
plt.axis([0,51,0,14])
plt.plot(X,heads,'r*')
plt.xlabel('Experiment Number',labelpad = -5)
plt.ylabel('Number of Heads')
plt.grid(True)
   

tally = []            #running tally of total number of heads/total number of coin flips


def main():
  for i in range(0,50):
    if i == 0 :
      tally = [heads[i]]
    else : 
      tally = tally + [sum(heads[0:i+1])]
    

  for i in range(13,13*50+1,13):
    tally[i/13-1] = tally[i/13-1]*1.0/i

 
  print(tally)

  

  
  plt.subplot(3,1,2)                               #Histogram
  plt.axis([0,14,0,25])
  plt.hist(heads,bins=13,range=(0,13))
  plt.xlabel('Number of heads',labelpad = -5)
  plt.ylabel('frequency of occurance')
  plt.grid(True)
   

  plt.subplot(3,1,3)                               #Running Tally
  plt.plot(X,tally,'b-')
  plt.axis([0,51,0,1])
  plt.xlabel('Experiment Number',labelpad = -5)
  plt.ylabel('(# of Heads)/(# of coin tosses)')
  plt.grid(True)
  plt.show()

if __name__=='__main__':
  main()
