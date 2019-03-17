from matplotlib import pyplot as plt
from numpy import linalg as LA
from scipy import linalg as SA
import numpy as np
t0 = 1
U = lambda x: 0
size = 100
array = []
for i in range(size):
    this = []
    for j in range(size):
        if (i==j):
            this.append(2*t0 + U(i))
        elif (abs(i-j) == 1):
            this.append(-1*t0)
        else:
            this.append(0)
    array.append(this)
print(np.array(array))
#valua, vector = SA.eig(array)
value, vector = LA.eig(array)
idx = np.argsort(value)
print(vector.shape)
fig, ax = plt.subplots(1, 2)
fig.suptitle('Hamitonian size: {0}x{0}'.format(size))
ax[0].plot(value[idx],'ro')
ax[0].set_title('eigenvalues')
while 1:
    for j,i in enumerate(np.rot90(vector[:,idx])):
        ax[1].set_title('eigenvector N:'+str(j))
        ax[1].plot(abs(i),'b')
        plt.pause(0.15)
        ax[1].cla()
        if (j>20):
            break
    ax[1].set_title('Restarting')
    plt.pause(0.2)
##ax[1].plot(abs(vector[:,idx][0]),'b')
##ax[1].plot(abs(vector[:,idx][25]),'r')
##    plt.pause(2)
fig.show()
