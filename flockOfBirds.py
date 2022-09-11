import math
import numpy as np
import matplotlib.pyplot as plt


def boidPosition():
    width, height  = 640 , 480
    startingPoint= 2.0
    N = 20
    pos = [width/startingPoint,height/startingPoint] + 10*np.random.rand(2*N).reshape(N,2)
    angles = 2*math.pi*np.random.rand(N)
    vel = np.array(list(zip(np.sin(angles), np.cos(angles))))


def applyBoundries(pos):
    testVal = []
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
        



