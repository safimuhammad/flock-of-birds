import math
import numpy as np
import matplotlib.pyplot as plt

angles = 2*math.pi*np.random.rand(5)
vel = np.array(list(zip(np.sin(angles),np.cos(angles))))
degree_Conv= angles *(180/math.pi)
plt.plot(vel[:,0],vel[:,1],'o')
plt.show()
# print(vel[: ,0],vel)