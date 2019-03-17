from matplotlib import pyplot as plt
from numpy import linalg as LA
import numpy as np
E0 = 2
t1 = -1
t2 = -1
array =[]
size = 5
for i in range(size**2):
    this = []
    for j in range(size**2):
        if (abs(i-j)==1 ):
            this.append(t1)
        elif (abs(i-j)== size):
            this.append(t2)
        elif (i==j):
            this.append(E0)
        else:
            this.append(0)
    array.append(this)
print(np.array(array))
valua, vector = LA.eig(array)
plt.plot( np.sort(valua) ,'rx')
plt.show()
