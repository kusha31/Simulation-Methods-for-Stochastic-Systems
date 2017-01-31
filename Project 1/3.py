#EE 511 - Project 1
#Question 3 [NJGAS Bootstrap Confidence Intervals]

import sys
import matplotlib.pyplot as plt
import numpy as py
import random


def bootstrap(njgas):      # reads NJGAS data from the given file, and calculates 95% confidence interval of mean
  f = open("NJGAS.dat",'rU')
  data = f.readlines()           # pointer would be pointing towards the last line of data
  f.close()
  
  for i in range(0,len(data)):
    data[i]=int(data[i][:-1])        # pointer reads from bottom to top
  print('Sample data = ',data)
  print('Mean of the sample data = ', py.mean(data))
  #print(len(data))

  replicate = data*100                    #Replicate the data 100 times to enhance the randomness of resampling.   

  samples = [[]]*1000                #Create 1000 samples by choosing elemnts from the sampled data
  sample_mean = []                          #list of means for each sample
  
  for i in range(0,len(samples)):  #create 1000 samples
    for j in range(0,len(data)):
      samples[i]=samples[i]+[replicate[random.randint(0,(len(replicate)-1))]]
    if i == 0:
      sample_mean=[py.mean(samples[i])]
    else:
      sample_mean = sample_mean+[py.mean(samples[i])]

  sorted_mean = sorted(sample_mean)                #sort the means in ascending order
  lower = py.percentile(sorted_mean,2.5)      #2.5th percentile
  higher = py.percentile(sorted_mean,97.5)    #97.5th percentile
  interval = higher - lower

  print('95% confidence interval for mean is between ',lower,' and ',higher)
  print('size of the confidence interval = ',interval)

 

def main():
  bootstrap(sys.argv[0])


if __name__ == '__main__':
  main()


