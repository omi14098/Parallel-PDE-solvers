import numpy as np
from math import *
import os
import matplotlib.pyplot as plt

commandStr = 'mpic++ mpi1DPDE.cpp -O0 -march=native -o out'
os.system(commandStr)
error, time = [], []
for nThreads in range(1,17):
  os.system('mpirun -np {0} --oversubscribe ./out 0 1> output.csv'.format(nThreads))
  results=[]
  with open('output.csv', 'r') as f:
  	for line in f:
  		if len(line.split(','))>1:
  			results.append(float(line.split(',')[1]))
  	error.append(results[-1])
  	time.append(results[5])
  	print(results)

plt.title('TEMPO DI ESECUZIONE')
plt.xlabel('NUMERO DI PROCESSORI')
plt.ylabel('t')
plt.plot(range(1,17), time, 'ko-', lw=2)
plt.show()

plt.title('ERRORE MASSIMO')
plt.xlabel('NUMERO DI PROCESSORI')
plt.ylabel('err')
plt.plot(range(1,17), error, 'ko-', lw=2)
plt.show()

mean = np.mean(error)
stddev = np.std(error)
print('errore medio: ', mean)
print('deviazione std: ', stddev)