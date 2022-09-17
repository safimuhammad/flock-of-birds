import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import squareform, pdist, cdist

angles = 2*math.pi*np.random.rand(5)
vel = np.array(list(zip(np.sin(angles),np.cos(angles))))
pos = [640/2.0 , 380/2.0] + 10*np.random.rand(2*5).reshape(5,2)
degree_Conv= angles *(180/math.pi)
plt.plot(vel[:,0],vel[:,1],'o')
arr=np.array([[1,2,3,42,43]])
plt.show()
print(vel[: ,0],vel)
x = squareform(pdist(pos))
plt.plot(x,'o')
plt.show()
d = x<25
test = np.array([[1 ,3],[3,2]])
print(x.sum(axis=1))
print(test.sum(axis=1))
print(d.dot(pos))
print(test.shape)