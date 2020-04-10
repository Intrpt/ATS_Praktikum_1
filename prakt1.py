#!/usr/bin/env python
# coding: utf-8

# In[107]:


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


# In[106]:




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
                print("Achtung!: Kreis(POINT(" + str(circle1.mittelpunkt.x) +"," + str(circle1.mittelpunkt.y) + ")," + str(circle1.radius) + ") und Kreis(POINT(" + str(circle2.mittelpunkt.x) + "," + str(circle1.mittelpunkt.y) + ")," + str(circle1.radius) + ") sind identisch!")
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
            print("Pos 2 )Achtung!: Kreis(POINT(" + str(circle1.mittelpunkt.x) +"," + str(circle1.mittelpunkt.y) + ")," + str(circle1.radius) + ") und Kreis(POINT(" + str(circle2.mittelpunkt.x) + "," + str(circle1.mittelpunkt.y) + ")," + str(circle1.radius) + ") haben keinen Schnittpunkt!")
    else:
        print("Pos 1 ) Achtung!: Kreis(POINT(" + str(circle1.mittelpunkt.x) +"," + str(circle1.mittelpunkt.y) + ")," + str(circle1.radius) + ") und Kreis(POINT(" + str(circle2.mittelpunkt.x) + "," + str(circle1.mittelpunkt.y) + ")," + str(circle1.radius) + ") haben keinen Schnittpunkt!")
    return result


# In[93]:


#Berechnung der Entfernung zwischen 2 Punkten
def getDistance(p1: Point, p2: Point):
    distance = math.sqrt(math.pow(p1.x-p2.x,2)+math.pow(p1.y-p2.y,2))
    return distance


# In[94]:


#Bestimme, welcher Punkt dem Basispunkt am nähsten ist, Return der Punkt der am nähsten ist.
#Input: Basispunkt & Liste aus Punkten die vom Basispunkt entfernt sind.
def getClosest(bp, vps):
    vp = vps[0]
    return vp


# In[95]:


#Bestimme einen Vektor zwischen 2 Punkten
def getVec(p1, p2):
    vec = Vector(Point(0,0))
    return vec


# In[96]:


#Berechne den Winkel zwischen 2 Vektoren
def getAngBetween(v1, v2):
    ang = 12
    return ang


# In[97]:


#Berechne den WInkel eines Vektors im Bezug auf den gegeben Kreis.
#Input: Kreis, Vektor
#Output: Winkel
def getAng(circle, v):
    ang = 12
    return ang
    


# In[98]:


#Berechne den Mittelpunkt-Vektor zwischen 2 Winkeln im Bezug auf den gegeben Kreis
#Input: Kreis, Winkel1, Winkel2;
def getMidVec(circle, ang1, ang2):
    v = Vector(Point(0,1))
    return v


# In[99]:


#Vektor negieren
def negVector(v):
    nV = Vector(Point(0,0))
    return nV


# In[100]:


#Vektor normalisieren mit der Fomel v = sqrt(x²+y²+z²)*Vektor(x,y,z)
def normVector(v):
    nV = Vector(Point(0,0))
    return nV


# In[ ]:




