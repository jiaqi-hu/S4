#!/usr/bin/python3

#https://github.com/victorliu/S4/issues/75

import S4

import numpy as np
from pprint import pprint as pprint

S = S4.New(Lattice=((1,0),(0,1)),NumBasis=100)
S.SetMaterial('Vacuum',1)
S.SetMaterial(Name='Silicon',Epsilon=12+0.01j)
S.AddLayer('top',0,'Vacuum')
S.AddLayer('slab',0.5,'Silicon')
S.AddLayerCopy('bottom',0,'top')
#S.SetRegionCircle('slab','Vacuum',(0,0),0.2)
S.SetRegionEllipse(
        S4_Layer = 'slab',
        S4_Material = 'Vacuum',
        Center = (0,0),
        Angle = 30,            # in degrees
        Halfwidths = (0.3,0.4) # semi-axis lengths
)
S.SetExcitationPlanewave((0, 0), 1, 0)
S.SetFrequency(0.4)

t,_,b = [S.GetPowerFlux(l) for l in ('top','slab','bottom')]
print('top in',t[0])
print('top out',t[1])
print('bottom out',b[0])
print('all out',-t[1]+b[0])
    
