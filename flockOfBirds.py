import math
import numpy as np
import matplotlib.pyplot as plt

width, height  = 640 , 480
startingPoint= 2.0
N = 20
pos = [width/startingPoint,height/startingPoint] + 10*np.random.rand(2*N).reshape(N,2)
angles = 2*math.pi*np.random.rand(N)
vel = np.array(list(zip(np.sin(angles), np.cos(angles))))
plt.imshow(pos, interpolation='nearest')
plt.show()
#drawing the boids now 