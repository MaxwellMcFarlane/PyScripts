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

def checkInBound(point,boundary):
    boundary.sort()
    ref = boundary[0]
    i = 1
    while i < len(boundary):
        if ref[0] > point[0] or point[0] > boundary[i][0]:
            if ref[1] > point[1] or point[1] > boundary[i][1]:
                #Both the x and y coordinate are outide the polygon
                #print("Out of Bounds")
                return False
        i += 1
    #print("In Bounds")
    return True

#transforms a given polygon into a 2D list based on unitSize specified
def dividePolygon(boundary,unitSize):
    boundary.sort()
    i = 0; bottom_x = boundary[0][0]; bottom_y = boundary[0][1]; top_x = boundary[-1][0]; top_y = boundary[-1][1];
    #Overestimate Boundary size for easier division & checking
    while i < len(boundary):
        if bottom_x > boundary[i][0]:
            bottom_x = boundary[i][0]
        if bottom_y > boundary[i][1]:
            bottom_y = boundary[i][1]
        if top_x < boundary[i][0]:
            top_x = boundary[i][0]
        if top_y < boundary[i][1]:
            top_y = boundary[i][1]
        i += 1

    bottom = [bottom_x,bottom_y]; top = [top_x,top_y]
    point = bottom
    map = []
    while point[1] <= top_y:
        while point[0] <= top_x:
            if checkInBound(point,boundary):
                # print(point)
                map.append(point)
                print('/n')
                print(map)
            point[0] += unitSize
        point[1] += unitSize
        point[0] = bottom_x
    return map

#Should return LUT of all resistance values at given point, relative to P0
#using the p2pResAdv function within a resolution of given points
def meshResistance(sRho,W,L,res,refP):
    pass

#pathRes = p2pResistance(12,200,3)
list = [[0,0],[10,0],[10,3],[0,3]]
#list = [[0,0],[10,0],[8,3],[0,3]]
map = dividePolygon(list,1)
# print(map)
# map = dividePolygon(list,1)
# checkInBound([1,3],list)
# checkInBound([2,2],list)
# checkInBound([12,20],list)
# pathRes = p2pResAdv(12,[0,0],[5,5],[[0,0],[200,0],[200,3],[0,3]],1)
#print(pathRes)

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
