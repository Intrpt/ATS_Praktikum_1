#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np
import matplotlib.pyplot as plt
import math
from Vector import Vector
from Point import Point
from Model import Model
from Landmark import Landmark as LM

# --- MAIN ------
if __name__ == '__main__':
    print("Starte Main")
    
    


# --- FUNCTIONS ------
def example1():
    return 1
def example2():
    return 1


# Beschreibung der Funktion und Head:
# Es werden 2 Vektoren addiert
# addVectors(Vector v1, Vector v2) return vector
def addVectors(v1, v2):
    v = Vector(Point(0,0))
    v.p.x = v1.p.x + v2.p.x
    v.p.y = v1.p.y + v2.p.y
    return v

# Baut das Model auf. Entweder mit dem Retina oder als
# Snapshot
#
#buildmodel(mid_x, mid_y, radius, LM1, LM2, LM3) return model
def buildmodel(mid_x, mid_y, radius, LM1, LM2, LM3):
    m = Model(Point(mid_x,mid_y),radius)
    return m
    #TODO fertigstellen

# Ändert die Position des Models auf dem Graphen
#moveModel(model,mid_x, mid_y) 
def moveModel(model,mid_x, mid_y):
    model.mittelpunkt.x = mid_x
    model.mittelpunkt.y = mid_y
    return model

# Berechnet den Vt Vektor
#buildVt(Pair paare[]) return vektor
def buildVt(paare):
    v = Vector(Point(0,0))
    return v

# Berechnet den Vp Vektor
#buildVp(Pair paare[])  return vektor
def buildVp(paare):
    v = Vector(Point(0,0))
    return v

# Berechnet den fertigen V vektor
#buildV(Vp, Vt) return Vektor
def buildV(Vp, Vt):
    v = Vector(Point(0,0))
    return v

# Bereitet den fertigen Graphen vor
#visualize(Vektor V)

def visualize(V):
    return 1


# In[ ]:




#Berechnung der Schnittpunkte von 2 Kreisen, Return den Schnittpunkt (POINT)
#Input: Landmark circle1, Landmark circle2
#Output: Liste mit den Schnittpunkten
def getIntersection(circle1: LM, circle2: LM):
    #Prüfe, wieviele Schnittpunkte es gibt
    result = []
    c = getDistance(circle1.mittelpunkt,circle2.mittelpunkt)
    if c != 0:
        c = getDistance(circle1.mittelpunkt,circle2.mittelpunkt)
        qx = (math.pow(circle1.radius,2)+math.pow(c,2)-math.pow(circle2.radius,2)) /(2*c)
        if c == 0:
            if circle1.radius != circle2.radius:
                #Es gibt nur einen Schnittpunkt
                qy = math.sqrt(math.pow(circle1.radius,2)-math.pow(qx,2))
                
                x = circle1.mittelpunkt.x +(qx*((circle2.mittelpunkt.x-circle1.mittelpunkt.x)/c))-(qy*((circle2.mittelpunkt.y-circle1.mittelpunkt.y)/c))
                y = circle1.mittelpunkt.y+(qx*((circle2.mittelpunkt.y-circle1.mittelpunkt.y)/c))+(qy*((circle2.mittelpunkt.x-circle1.mittelpunkt.x)/c))
                result.append(Point(x,y))
            else:
                raise ValueError('Kreise sind identisch')
                #print("Achtung!: Kreis(POINT(" + str(circle1.mittelpunkt.x) +"," + str(circle1.mittelpunkt.y) + ")," + str(circle1.radius) + ") und Kreis(POINT(" + str(circle2.mittelpunkt.x) + "," + str(circle1.mittelpunkt.y) + ")," + str(circle1.radius) + ") sind identisch!")
        elif c > 0:
            #Es gibt mehrere Schnittpunkte
            qy1 = math.sqrt(math.pow(circle1.radius,2)-math.pow(qx,2))
            qy2 = qy1*(-1)
            
            x1 = circle1.mittelpunkt.x +(qx*((circle2.mittelpunkt.x-circle1.mittelpunkt.x)/c)) -(qy1*((circle2.mittelpunkt.y-circle1.mittelpunkt.y)/c))
            y1 = circle1.mittelpunkt.y +(qx*((circle2.mittelpunkt.y-circle1.mittelpunkt.y)/c)) +(qy1*((circle2.mittelpunkt.x-circle1.mittelpunkt.x)/c))
                
            x2 = circle1.mittelpunkt.x +(qx*((circle2.mittelpunkt.x-circle1.mittelpunkt.x)/c))-(qy2*((circle2.mittelpunkt.y-circle1.mittelpunkt.y)/c))
            y2 = circle1.mittelpunkt.y+(qx*((circle2.mittelpunkt.y-circle1.mittelpunkt.y)/c))+(qy2*((circle2.mittelpunkt.x-circle1.mittelpunkt.x)/c))

            
            result.append(Point(x1,y1))
            result.append(Point(x2,y2))
        else:
            raise ValueError('Kreise haben keinen Schnittpunkt')
            #print("Pos 2 )Achtung!: Kreis(POINT(" + str(circle1.mittelpunkt.x) +"," + str(circle1.mittelpunkt.y) + ")," + str(circle1.radius) + ") und Kreis(POINT(" + str(circle2.mittelpunkt.x) + "," + str(circle1.mittelpunkt.y) + ")," + str(circle1.radius) + ") haben keinen Schnittpunkt!")
    else:
        raise ValueError('Kreise haben keinen Schnittpunkt')
        #print("Pos 1 ) Achtung!: Kreis(POINT(" + str(circle1.mittelpunkt.x) +"," + str(circle1.mittelpunkt.y) + ")," + str(circle1.radius) + ") und Kreis(POINT(" + str(circle2.mittelpunkt.x) + "," + str(circle1.mittelpunkt.y) + ")," + str(circle1.radius) + ") haben keinen Schnittpunkt!")
    return result


# In[ ]:


#Berechnung der Entfernung zwischen 2 Punkten
def getDistance(p1: Point, p2: Point):
    distance = math.sqrt(math.pow(p1.x-p2.x,2)+math.pow(p1.y-p2.y,2))
    return distance


# In[ ]:


#Bestimme, welcher Punkt dem Basispunkt am nähsten ist, Return der Punkt der am nähsten ist.
#Input: Basispunkt & Liste aus Punkten die vom Basispunkt entfernt sind.
def getClosest(bp:Point, vps):
    if(len(vps) > 0):
        dist = getDistance(bp, vps[0])
        closest = vps[0]
        if(len(vps) > 1):
            for vp in vps:
                tempDistance = getDistance(bp,vp)
                if(tempDistance < dist):
                    closest = vp
                    dist = tempDistance
        return closest
    else:
        raise ValueError('getClosest wurde mit einer leeren Liste (VPS) aufgerufen!')
    return vp


# In[11]:


#Bestimme einen Vektor zwischen 2 Punkten
#Input: Punkt p1, p2
#Output: Vektor P1->P2
def getVec(p1:Point, p2:Point):
    x = p2.x-p1.x
    y = p2.y-p1.y
    return Vector(Point(x,y))


# In[33]:


#Berechne den Winkel zwischen 2 Vektoren
def getAngBetween(v1:Vector, v2:Vector):
    z = v1.p.x * v2.p.x + v1.p.y * v2.p.y
    n = math.sqrt(math.pow(v1.p.x,2)+math.pow(v1.p.y,2))*math.sqrt(math.pow(v2.p.x,2)+math.pow(v2.p.y,2))
    return math.degrees(math.acos(z/n))


# Beschreibung der Funktion und Head:
# Es werden 2 Vektoren multipliziert
# multiplyVectors(Vector v1, Vector v2) return vector
def multiplyVectors(v1, v2):
    v = Vector(Point(0,0))
    v.p.x = v1.p.x * v2.p.x
    v.p.y = v1.p.y * v2.p.y
    return v


# In[30]:


#Berechne den WInkel eines Vektors im Bezug auf den gegeben Kreis.
#Input: Kreis, Vektor
#Output: Winkel
def getAng(circle:LM, v:Vector):
    tempVec = getVec(circle.mittelpunkt,Point(circle.mittelpunkt.x,(circle.mittelpunkt.y)+1))
    return getAngBetween(tempVec, v)
    


# In[26]:


#Berechne den Mittelpunkt-Vektor zwischen 2 Winkeln im Bezug auf den gegeben Kreis
#Input: Kreis, Winkel1, Winkel2;
def getMidVec(ang1, ang2, circle:LM):
    if ang1 == ang2: 
        raise ValueError('Die beiden gegebenen Winkel sind identisch!')
    elif ang1 > ang2:
        ang = ang2+((ang1-ang2)/2)
    else:
        ang = ang1+((ang2-ang1)/2)
    rad = math.radians(ang)
    v1 = getVec(circle.mittelpunkt,Point(circle.mittelpunkt.x,(circle.mittelpunkt.y)+1))
    y = 1
    if circle.mittelpunkt.y != 0:
        y = circle.mittelpunkt.y
    x = (v1.p.x*y*math.cos(rad)+v1.p.y*y*math.sin(rad))/(v1.p.y*math.cos(rad)-v1.p.x*math.sin(rad))
    v = Vector(Point(x,y))
    return v


# In[ ]:


#Vektor negieren
def negVector(v):
    x = v.p.x*(-1)
    y = v.p.y*(-1)
    nV = Vector(Point(x,y))
    return nV


# In[39]:


#Vektor normalisieren mit der Fomel v = sqrt(x²+y²+z²)*Vektor(x,y,z)
def normVector(v):
    factor = math.sqrt(math.pow(v.p.x,2)+math.pow(v.p.y,2))
    factor = 1/factor
    nX = factor*v.p.x
    nY = factor*v.p.y
    nV = Vector(Point(nX,nY))
    return nV


# In[ ]:




