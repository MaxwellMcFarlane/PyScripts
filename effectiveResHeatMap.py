from gdsii.library import Library
from gdsii.elements import *
import matplotlib.pyplot as plt
import math

class Data:
    pass

def p2pResistance(sRho,W,L):
    res = sRho*W/L
    return res

#check if point given is outside of shape boundary
def p2pResAdv(sRho,P1,P2,boundary,step):
    x1 = P1[0]; y1 = P1[1]
    x2 = P2[0]; y2 = P2[1]
    res = 0
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    while true:
        pass
    return res

#Should return LUT of all resistance values at given point, relative to P0
#using the p2pResAdv function within a resolution of given points
def meshResistance(sRho,W,L,res,refP):
    pass

pathRes = p2pResistance(12,200,3)
pathRes = p2pResAdv(12,[0,0],[5,5],[[0,0][200,0][200,3][0,3]],1)
print(pathRes)

# read a library from a file
# with open('example.GDS', 'rb') as stream:
# with open('/Users/maxwellmcfarlane/github/PyScripts/path.gds', 'rb') as stream:
#     lib = Library.load(stream)
#
# struc = lib.pop(0)
# print(struc.name)
# print(struc.strclass)
# print(len(struc))
# print(struc[0].xy)
# points = struc[0].xy
# polygon = plt.Polygon(points)
# plt.gca().add_patch(polygon)
# plt.axis('scaled')
# plt.show()
