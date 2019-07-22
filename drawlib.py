# Drawing Routines, like OpenGL
# Vernon Buck

from matlib import *

#global values to save and apply to other code
def gtOrtho(left, right, bottom, top, near, far):
    #set all values to global to have them saved
    global left_saved
    left_saved = left
    global right_saved
    right_saved = right
    global bottom_saved
    bottom_saved = bottom
    global top_saved
    top_saved = top
    global near_saved
    near_saved = near
    global far_saved
    far_saved = far
    global orthoBoolean
    orthoBoolean = True 
    global perspBoolean
    perspBoolean = False
    #make the other boolean false here
    pass

#global values to save and apply to later code
def gtPerspective(fov, near, far):
    global perspBoolean
    perspBoolean = True
    global orthoBoolean
    orthoBoolean = False 
    global fov_saved
    fov_saved = fov
    global near_saved
    near_saved = near
    global far_saved
    pass

#makes list to hold coordinates
def gtBeginShape():
    global vertList
    vertList = []
    pass

#draws all of the coordinates
#also resets the bool values for gtVertex
def gtEndShape():
    global vertList
    for i in range(0,len(vertList),2):
        startPoints = vertList[i]
        endPoints = vertList[i+1]
        line(startPoints[0], startPoints[1], endPoints[0], endPoints[1])
    vertList = []
    orthoBoolean = False
    perspBoolean = False
    pass

#populates list that holds coordinates
def gtVertex(x, y, z):
    #gets ctm value from hw 1a code
    global ctm
    ctm = gtGetMatrix()
    newMatrix = [[0]*4 for m in range(4)] 
    for m in range(4):
        newMatrix[m][m] = 0 
        
    newMatrix[0][0] = x
    newMatrix[1][0] = y
    newMatrix[2][0] = z
    newMatrix[3][0] = 1

    #creates projected matrix
    valueMatrix = gtMultiplication(ctm, newMatrix)
        
    tempx = valueMatrix[0][0]
    tempy = valueMatrix[1][0]
    tempz = valueMatrix[2][0]

    innerList = []
    #Determines whether orthogonal or perspective drawing methods  are used applies the equations and
    #puts points gained from equation into (x,y) pair and then into another array to be traversed
    if (orthoBoolean == True):     
        newX = (width/(right_saved - left_saved)) * (tempx - left_saved)
        newY = (height/(bottom_saved - top_saved)) * (tempy - top_saved)
        innerList.append(newX)
        innerList.append(newY)
        vertList.append(innerList)
    if (perspBoolean == True):
        truefov = tan(radians(fov_saved)/2)
        newX = (tempx / abs(tempz))
        newY = tempy / (abs(tempz) * -1)    
        newX2 = (newX + radians(fov_saved)) * (width/ (2*radians(fov_saved)))
        newY2 = (newY + radians(fov_saved)) * (height/ (2*radians(fov_saved)))
        innerList.append(newX2)
        innerList.append(newY2)
        vertList.append(innerList)
    pass