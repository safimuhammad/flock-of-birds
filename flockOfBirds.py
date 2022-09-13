import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import squareform, pdist, cdist



def boidPosition():
    width, height  = 640 , 480
    startingPoint= 2.0
    N = 20
    pos = [width/startingPoint,height/startingPoint] + 10*np.random.rand(2*N).reshape(N,2)
    angles = 2*math.pi*np.random.rand(N)
    vel = np.array(list(zip(np.sin(angles), np.cos(angles))))

    



def applyBoundries(pos):

    deltaR = 2.0
    

    for coords in pos:
        if coords[0]> width + deltaR:
            coords[0] = -deltaR
        if coords[0] < - deltaR:
            coords[0] = width + deltaR
        if coords[1] > height + deltaR:
            coords[1] = - deltaR
        if coords[1]  < - deltaR:
            coords[1] = height + deltaR
        
def test2(pos , radius):
    distMatrix = squareform(pdist(pos))
    D = distMatrix < radius
    vel= pos*D.sum(axis=1).reshape(N,1) - D.dot(pos)
    return vel


def applyRules(self):
    # rule#1 separation
    D = distMatrix < 25.0
    vel = self.pos*D.sum(axis=1).reshape(self.N,1) - D.dot(self.pos)
    self.limit(vel, self.maxRuleVel)

    # Rule#2 Alignment
    vel2 = D.dot(self.vel)
    self.limit(vel2,self.maxRuleVel)
    vel += vel2 

    # Rule#3 cohesion
    vel3 = D.dot(self.pos) - self.pos
    self.limit(vel3,self.maxRuleVel)
    vel += vel3