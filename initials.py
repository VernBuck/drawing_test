# In the routine below, you should draw your initials in perspective
# Vernon Buck
from matlib import *
from drawlib import *

def persp_initials():
    #global perspBoolean
    #perspBoolean = True
    
    gtInitialize()
    gtPerspective (60, -100, 100)
    gtPushMatrix()
    gtTranslate(0, 0, -4)
    
    gtBeginShape ()
    #V of my initials
    gtVertex (-1.0, -1.0, 1.0)
    gtVertex (-1.0,  1.0, 1.0)
    gtVertex (-1.0,  -1.0, 1.0)
    gtVertex (1.0,  1.0, -1.0)
    
    #B of my initials
    gtVertex (1, -1.0, 1.0)
    gtVertex (1, 1.0, 1.0)
    #
    gtVertex (2, -1.0, 1.0)
    gtVertex (2, 1.0, 2.0)
    
    gtVertex (1, 1.0, 1.0)
    
    gtVertex (2, 1.0, 2.0)
    
    gtVertex (1, 1.0, 1.0)
    gtVertex (2, 1.0, 2.0)
    gtVertex (1, -1.0, 1.0)
    gtVertex (2, -1.0, 2.0)
    
    gtVertex (2, -1.0, 2.0)
    gtVertex (2, 1.0, 1.0)
    
    
    gtEndShape()
    
    gtPopMatrix()
    pass