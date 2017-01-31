#EE 511 - Project 1
#Question 4 [Unfair Confidence...]

import sys
import random
import numpy as py
import matplotlib.pyplot as plt 

heads = [4, 11, 8, 7, 9, 10, 9, 7, 10, 11, 11, 10,7, 8, 7, 6, 6, 8, 6, 6, 10, 10, 9, 11, 9, 10, 10, 7, 11, 10, 10, 6, 7, 7, 7, 9, 11, 9, 9, 7, 7, 10, 10, 2, 8, 11, 11, 9, 5, 11]

tally=[]  #Probability of heads in each experiment,i.e.,# of Heads in 13 coin flips/13

def bootstrap(x):       #input parameter is a list that has probability of heads in each experiment
  samples = []            #create a list of 1000 samples by randomly selecting values from the input paramater list
  
  for i in range(0,1000):
    samples = samples+[x[random.randint(0,(len(x)-1))]]
 
  sorted_samples = sorted(samples)

  lower = py.percentile(sorted_samples,2.5)
  higher = py.percentile(sorted_samples,97.5)
  interval = higher - lower

  print('95% confidence interval for Probability of Heads is between ',lower,' and ',higher)
  print('size of the confidence interval = ',interval)

def main():
  for i in range(0,len(heads)):
    if i == 0 :
      tally = [heads[i]/13.0]
    else :  
      tally = tally + [heads[i]/13.0]  
    

  print(heads)
  print(tally) 
  
  bootstrap(tally) 
 


if __name__=='__main__':
  main()
