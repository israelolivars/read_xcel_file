import numpy as np

path2= 'channel2.txt'
com= np.loadtxt(path2,dtype=str,delimiter=",")

for i in range(len(com)):
    print(com[i])