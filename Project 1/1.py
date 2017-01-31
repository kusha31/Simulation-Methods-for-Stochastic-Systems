#EE 511 - Project 1
#Question 1 [Coins Coins Everywhere...]

import sys
import random
import numpy as ny
import matplotlib.pyplot as plt

heads=[3,9,7,8,7,8,9,4,8,7,5,7,7,8,7,2,8,10,6,10,7,5,8,9,4,9,3,8,7,4,8,5,5,7,6,4,4,7,3,7,5,6,6,4,8,6,6,6,7,5]  # number of heads from each experiment of 13 coin tosses   		
print(heads)
X=ny.arange(1,51,1)
plt.subplot(3,1,1)                               #Scatter Plot
plt.axis([0,51,0,15])
plt.plot(X,heads,'r*')
plt.xlabel('Experiment #',labelpad = -5)
plt.ylabel('Number of Heads')
plt.grid(True)



tally=[]            #running tally of cumulative number of heads/total number of coin flips
tally1 = []
#new_tally = []

def main():
  for i in range(0,50):
    if i == 0 :
      tally = [heads[i]]
    else :
      tally = tally + [sum(heads[0:i+1])]
      tally1 = tally
      print(tally1)


  """for j in range(0,len(tally1)):
    if j == 0:
      new_tally = [tally[j]/13]
    else:
      new_tally = new_tally.append(tally[j]/((13*j)+13))
      print(new_tally)"""
    
  for i in range(13,13*50+1,13):
    tally[i/13-1] = tally[i/13-1]*1.0/i
 
  
  
  #print(tally)
  
  
  
  plt.subplot(3,1,2)
  plt.hist(heads,bins=13,range=(0,13))                 #Histogram  
  plt.axis([0,15,0,20])
  plt.xlabel('Number of heads',labelpad = -5)
  plt.ylabel('Frequency of occurance')
  plt.grid(True)
   
  plt.subplot(3,1,3)
  plt.axis([0,51,0,1])
  plt.plot(X,tally1,'b-')
  plt.xlabel('Experiment Number',labelpad = -5)    #Running Tally 
  plt.ylabel('(# of Heads)/(# of coin tosses)')
  plt.grid(True)
  
  plt.show()

if __name__=='__main__':
  main()
