#!/usr/bin/env python
# coding: utf-8

# In[26]:


#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np
import matplotlib.pyplot as plt
import math
from Vector import Vector
from Point import Point
from Model import Model
import numpy as np
from Landmark import Landmark



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

    for x in range(0,3):
        # Wir wählen den ersten Landmark aus
        if x == 0:
            LM_Working_on = LM1
        elif x == 1:
            LM_Working_on = LM2
        elif x == 2:
            LM_Working_on = LM3

        # Muss 3 mal gemacht werden
        # 2a) Wir berechnen die Entfernungen vom Snapshot mittelpunkt(=0,0) zum Mittelpunkt der Landmarks.
        ent_model_zu_LM_Working_on = getDistance(m.mittelpunkt,LM_Working_on.mittelpunkt)
        # Create fake LM
        # 2b) Snapshotkreis radius auf die größe der berechneten Entfernungen vergrößern
        LM_fake = Landmark(m.mittelpunkt,ent_model_zu_LM_Working_on)
        # 2c) Die Schnittpunkte zwischen dem vergrößerten snapshot Radius und dem Landmark-kreis berechnet (Schnittpunkt1, Schnittpunkt2)
        intersection1, intersection2 = getIntersection(LM_fake,LM_Working_on)
        # 2d)
        Schnittpunkt1 = Vector(intersection1)
        Schnittpunkt2 = Vector(intersection2)
        # 2e) Wir speichern die entfernung zwischen den beiden Schnittpunkten. (Als WInkel in grad)
        ang_tmp = getAngBetween(Schnittpunkt1,Schnittpunkt2)
        ang_tmp_1 = getAngBetween(Vector(Point(0,0+1)),Vector(Point(Schnittpunkt1.p.x-mid_x,Schnittpunkt1.p.y-mid_y)))
        if m.mittelpunkt.x > Schnittpunkt1.p.x:
            ang_tmp_1 = 360 -ang_tmp_1
        ang_tmp_2 = getAngBetween(Vector(Point(0,0+1)),Vector(Point(Schnittpunkt2.p.x-mid_x,Schnittpunkt2.p.y-mid_y)))
        if m.mittelpunkt.x > Schnittpunkt2.p.x:
            ang_tmp_2 = 360 -ang_tmp_2
        # 2f) Wir erstellen je einen Vektor von Snapshotkreis mittelpunkt zum Landmark mittelpunkt und speichern ihn.
        tmp_p = Point(LM_Working_on.mittelpunkt.x - m.mittelpunkt.x, LM_Working_on.mittelpunkt.y - m.mittelpunkt.y)
        vec_model_lm_mittelpunkt = Vector(tmp_p)

        #3a)
        size = 0
        if ang_tmp_2 > ang_tmp_1:
            size = ang_tmp_2 - ang_tmp_1
        #3b)
        else:
            size = 360 - ang_tmp_2 + ang_tmp_1

        # Kann Falsch sein -------------------------------------------------------------------------------------

        if x == 0:
            # LM1 (G1) abarbeiten
            m.vec_mid_LM1 = vec_model_lm_mittelpunkt
            
                
            
            if mid_x < 0:
                m.ang_1_LM1 = ang_tmp_1
                m.ang_2_LM1 = ang_tmp_2
            else:
                if ang_tmp_1 > ang_tmp_2:
                    m.ang_1_LM1 = ang_tmp_1
                    m.ang_2_LM1 = ang_tmp_2
                else:
                    m.ang_1_LM1 = ang_tmp_2
                    m.ang_2_LM1 = ang_tmp_1
                
            m.ang_mid_LM1 = ((ang_tmp_2 - ang_tmp_1) / 2) + ang_tmp_1
            m.size_LM1 = size
            

        elif x == 1:
            # LM2 (G2) abarbeiten
            m.vec_mid_LM2 = vec_model_lm_mittelpunkt
            
            if mid_x < 0:
                m.ang_1_LM2 = ang_tmp_1
                m.ang_2_LM2 = ang_tmp_2
            else:
                if ang_tmp_1 > ang_tmp_2:
                    m.ang_1_LM2 = ang_tmp_1
                    m.ang_2_LM2 = ang_tmp_2
                else:
                    m.ang_1_LM2 = ang_tmp_2
                    m.ang_2_LM2 = ang_tmp_1
            
            m.ang_mid_LM2 = ((ang_tmp_2 - ang_tmp_1) / 2) + ang_tmp_1
            m.size_LM2 = size
            
            
        elif x == 2:
            # LM3 (G3) abarbeiten
            m.vec_mid_LM3 = vec_model_lm_mittelpunkt
            if mid_x < 0:
                m.ang_1_LM3 = ang_tmp_1
                m.ang_2_LM3 = ang_tmp_2
            else:
                if ang_tmp_1 > ang_tmp_2:
                    m.ang_1_LM3 = ang_tmp_1
                    m.ang_2_LM3 = ang_tmp_2
                else:
                    m.ang_1_LM3 = ang_tmp_2
                    m.ang_2_LM3 = ang_tmp_1
            
            m.ang_mid_LM3 = ((ang_tmp_2 - ang_tmp_1) / 2) + ang_tmp_1
            m.size_LM3 = size
            

            
            # Alle G werte berechnen
            # Für G1
            if m.ang_1_LM2 > m.ang_2_LM1:
                m.ang_mid_G1 =  ((m.ang_1_LM2 - m.ang_2_LM1) / 2) + m.ang_2_LM1
                m.size_G1 = m.ang_1_LM2 - m.ang_2_LM1
            
            else:
                m.ang_mid_G1 =  ((m.ang_2_LM1 - m.ang_1_LM2 ) / 2) + m.ang_1_LM2 
                m.size_G1 = m.ang_2_LM1 - m.ang_1_LM2
            m.vec_mid_G1 = getMidVec(m.ang_2_LM1,m.ang_1_LM2,Landmark(m.mittelpunkt,m.radius))

            # Für G2
            if m.ang_1_LM3 > m.ang_2_LM2:
                m.ang_mid_G2 =  ((m.ang_1_LM3 - m.ang_2_LM2) / 2) + m.ang_2_LM2
                m.size_G2 = m.ang_1_LM3 - m.ang_2_LM2
            else:
                m.ang_mid_G2 =  ((m.ang_2_LM2 - m.ang_1_LM3 ) / 2) + m.ang_1_LM3 
                m.size_G2 = m.ang_2_LM2 - m.ang_1_LM3

            m.vec_mid_G2 = getMidVec(m.ang_2_LM2,m.ang_1_LM3,Landmark(m.mittelpunkt,m.radius))

            # Für G3
            if m.ang_1_LM1 > m.ang_2_LM3:
                m.ang_mid_G3 =  ((m.ang_1_LM1 - m.ang_2_LM3) / 2) + m.ang_2_LM3
                m.size_G3 = 360 - (m.ang_1_LM1 - m.ang_2_LM3)
            else:
                m.ang_mid_G3 =  ((m.ang_2_LM3 - m.ang_1_LM1 ) / 2) + m.ang_1_LM1
                m.size_G3 = 360 - (m.ang_2_LM3 - m.ang_2_LM1)
            #m.size_G3 = getAngBetween(LM1.mittelpunkt,LM3.)
            m.vec_mid_G3 = getMidVec(m.ang_2_LM3,m.ang_1_LM1,Landmark(m.mittelpunkt,m.radius))

  
    return m



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
    for value in paare:
        v.p.x = v.p.x + normVector(value).p.x
        v.p.y = v.p.y + normVector(value).p.y
    return v

# Berechnet den Vp Vektor
#buildVp(Pair paare[])  return vektor
def buildVp(paare):
    v = Vector(Point(0,0))
    for value in paare:
        v.p.x = v.p.x + normVector(value).p.x
        v.p.y = v.p.y + normVector(value).p.y
    return v

# Berechnet den fertigen V vektor
#buildV(Vp, Vt) return Vektor
def buildV(Vp, Vt):
    v = Vector(Point(0,0))
    v.p.x = Vt.p.x + 3 * Vp.p.x
    v.p.y = Vt.p.y + 3 * Vp.p.y
    return v

# Bereitet den fertigen Graphen vor
#visualize(Vektor V, Point p)

def visualize(v,p):
    #TODO virtualisieren
    # Config
    # Dimension ist 14*14
    #grid_dimension = 14
    # Create the Grid
    #x = np.arange(-grid_dimension/2, grid_dimension/2+1, 1)
    #y = np.arange(-grid_dimension/2, grid_dimension/2+1, 1)
    #xx, yy = np.meshgrid(x, y)
    #grid = np.zeros((grid_dimension+1, grid_dimension+1))
    #x,y = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))

    u = v.p.x
    v = v.p.y

    plt.quiver(p.x,p.y,u,v)
    
    return 1

def visualize_show():
    plt.show()
    plt.close()
    return 1

# In[ ]:


def orthogonalVector(v:Vector,ang):
    if ang:
        return Vector(Point(v.p.y*(-1),v.p.x))
    else:
        return Vector(Point(v.p.y,v.p.x*(-1)))

#Berechnung der Schnittpunkte von 2 Kreisen, Return den Schnittpunkt (POINT)
#Input: Landmark circle1, Landmark circle2
#Output: Liste mit den Schnittpunkten
def getIntersection(circle1: Landmark, circle2: Landmark):
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
def getClosest(bp:Vector, vps):
    if(len(vps) > 0):
        dist = getAngBetween(bp, vps[0])
        closest = vps[0]
        if(len(vps) > 1):
            for vp in vps:
                tempDistance = getAngBetween(bp,vp)
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
    temp = z/n
    if temp > 1:
        temp = 1
    elif temp < -1:
        temp = -1
    temp = math.acos(temp)
    return math.degrees(temp)



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
def getAng(circle:Landmark, v:Vector):
    tempVec = getVec(circle.mittelpunkt,Point(circle.mittelpunkt.x,(circle.mittelpunkt.y)+1))
    return getAngBetween(tempVec, v)
    


# In[26]:


#Berechne den Mittelpunkt-Vektor zwischen 2 Winkeln im Bezug auf den gegeben Kreis
#Input: Kreis, Winkel1, Winkel2;
""" def getMidVec(ang1, ang2, circle:Landmark):
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
    return v """

#Berechne den Mittelpunkt-Vektor zwischen 2 Winkeln im Bezug auf den gegeben Kreis
#Input: Kreis, Winkel1, Winkel2;
def getMidVec(ang1, ang2, circle:Landmark):
    if ang1 == ang2: 
        raise ValueError('Die beiden gegebenen Winkel sind identisch!')

    if ang2 < ang1:
        #Überlauf
        ang2= ang2+360

    ang = ang2+((ang1-ang2)/2)
    rad = math.radians(90-ang)

    x=math.cos(rad)
    y=math.sin(rad)

    #v1 = getVec(circle.mittelpunkt,Point(circle.mittelpunkt.x,(circle.mittelpunkt.y)+1))
    #y = 1
    #if circle.mittelpunkt.y != 0:
    #    y = circle.mittelpunkt.y
    #x = (v1.p.xymath.cos(rad)+v1.p.yymath.sin(rad))/(v1.p.ymath.cos(rad)-v1.p.xmath.sin(rad))
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
def normVector(v:Vector):
    factor = math.sqrt(math.pow(v.p.x,2)+math.pow(v.p.y,2))
    factor = 1/factor
    nX = factor*v.p.x
    nY = factor*v.p.y
    nV = Vector(Point(nX,nY))
    return nV


# In[ ]:




# In[27]:


# --- MAIN ------
if __name__ == '__main__':
    #Landmarks initialisieren
    print("=====Landmarks initialisieren=====")
    print("Landmark besteht aus Mittelpunkt(X,Y) & Radius")
    print("Landmark 1)")
    print("Mittelpunkt X:")
    lm1_x = 3.5
    print("Mittelpunkt Y:")
    lm1_y = 2
    print("Radius:")
    rad1 = 0.5
    print("===============================")
    print("Landmark 2)")
    print("Mittelpunkt X:")
    lm2_x = 3.5
    print("Mittelpunkt Y:")
    lm2_y = -2
    print("Radius:")
    rad2 = 0.5
    print("===============================")
    print("Landmark 3)")
    print("Mittelpunkt X:")
    lm3_x = 0
    print("Mittelpunkt Y:")
    lm3_y = -4
    print("Radius:")
    rad3 = 0.5
    
    LM1 = Landmark(Point(lm1_x,lm1_y),rad1)
    LM2 = Landmark(Point(lm2_x,lm2_y),rad2)
    LM3 = Landmark(Point(lm3_x,lm3_y),rad3)
    
    
    #Snapshot Model entwickeln
    #print("=====Snapshot model wird erstellt=====")
    snapshotKreis = buildmodel(0, 0, 1, LM1, LM2, LM3)
    #print("done!")
    
    #Snapshot model laden und auf Position X, Y verschieben
    retina_radius = 2
    for pos_x in range(-7,8):
        for pos_y in range(-7,8):
            if(not(pos_x == 0 and pos_y == 0) and not(pos_x == lm1_x and pos_y == lm1_y) and not(pos_x == lm2_x and pos_y == lm2_y) and not(pos_x == lm3_x and pos_y == lm3_y)):

                #print("=====Snapshot model wird verschoben=====")
                snapshot = moveModel(snapshotKreis,pos_x,pos_y)
                #print("done!")

                #Retina Model entwickeln
                #print("=====Retina model wird erstellt=====")
                retina = buildmodel(pos_x, pos_y, retina_radius, LM1, LM2, LM3)
                #print("done!")

                #Retina & Snapshot vergleichen
                #print("=====Retina & Snapshot model wird verglichen=====")
                #Paare bilden
                    #turn Vektor:
                #print("    1)Turn Vektoren für LM bilden")
                closest_vec_LM1 = getClosest(snapshot.vec_mid_LM1,[retina.vec_mid_LM1,retina.vec_mid_LM2,retina.vec_mid_LM3])
                closest_vec_LM2 = getClosest(snapshot.vec_mid_LM2,[retina.vec_mid_LM1,retina.vec_mid_LM2,retina.vec_mid_LM3])
                closest_vec_LM3 = getClosest(snapshot.vec_mid_LM3,[retina.vec_mid_LM1,retina.vec_mid_LM2,retina.vec_mid_LM3])
                closest_vec_LM1_ang = getAng(Landmark(Point(pos_x,pos_y),retina_radius), closest_vec_LM1)
                closest_vec_LM2_ang = getAng(Landmark(Point(pos_x,pos_y),retina_radius), closest_vec_LM2)
                closest_vec_LM3_ang = getAng(Landmark(Point(pos_x,pos_y),retina_radius), closest_vec_LM3)
                turn_vector_LM1 = orthogonalVector(closest_vec_LM1,snapshot.ang_mid_LM1 > closest_vec_LM1_ang)
                turn_vector_LM2 = orthogonalVector(closest_vec_LM2,snapshot.ang_mid_LM2 > closest_vec_LM2_ang)
                turn_vector_LM3 = orthogonalVector(closest_vec_LM3,snapshot.ang_mid_LM3 > closest_vec_LM3_ang)


                #print("    1)Turn Vektoren für G bilden")
                closest_vec_G1 = getClosest(snapshot.vec_mid_G1,[retina.vec_mid_G1,retina.vec_mid_G2,retina.vec_mid_G3])
                closest_vec_G2 = getClosest(snapshot.vec_mid_G2,[retina.vec_mid_G1,retina.vec_mid_G2,retina.vec_mid_G3])
                closest_vec_G3 = getClosest(snapshot.vec_mid_G3,[retina.vec_mid_G1,retina.vec_mid_G2,retina.vec_mid_G3])
                closest_vec_G1_ang = getAng(Landmark(Point(pos_x,pos_y),retina_radius), closest_vec_G1)
                closest_vec_G2_ang = getAng(Landmark(Point(pos_x,pos_y),retina_radius), closest_vec_G2)
                closest_vec_G3_ang = getAng(Landmark(Point(pos_x,pos_y),retina_radius), closest_vec_G3)
                turn_vector_G1 = orthogonalVector(closest_vec_G1,snapshot.ang_mid_G1 > closest_vec_G1_ang)
                turn_vector_G2 = orthogonalVector(closest_vec_G2,snapshot.ang_mid_G2 > closest_vec_G2_ang)
                turn_vector_G3 = orthogonalVector(closest_vec_G3,snapshot.ang_mid_G3 > closest_vec_G3_ang)

                #Wann werden die turn_vector negiert???

                Vt_list = [turn_vector_LM1,turn_vector_LM2,turn_vector_LM3,turn_vector_G1,turn_vector_G2,turn_vector_G3]
                #print("    1) done")

                    #Approach Vektor:
                #print("    2)Approach Vektoren bilden")
                    #1. Approach Vektor:
                if closest_vec_LM1 is retina.vec_mid_LM1:
                    size_retina_LM1 = retina.size_LM1
                elif closest_vec_LM1 is retina.vec_mid_LM2:
                    size_retina_LM1 = retina.size_LM2
                elif closest_vec_LM1 is retina.vec_mid_LM3:
                    size_retina_LM1 = retina.size_LM3
                else:
                    print("Error: Approach Vektoren bilden failed (LM)")

                if closest_vec_LM2 is retina.vec_mid_LM1:
                    size_retina_LM2 = retina.size_LM1
                elif closest_vec_LM2 is retina.vec_mid_LM2:
                    size_retina_LM2 = retina.size_LM2
                elif closest_vec_LM2 is retina.vec_mid_LM3:
                    size_retina_LM2 = retina.size_LM3
                else:
                    print("Error: Approach Vektoren bilden failed (LM)")

                if closest_vec_LM3 is retina.vec_mid_LM1:
                    size_retina_LM3 = retina.size_LM1
                elif closest_vec_LM3 is retina.vec_mid_LM2:
                    size_retina_LM3 = retina.size_LM2
                elif closest_vec_LM3 is retina.vec_mid_LM3:
                    size_retina_LM3 = retina.size_LM3
                else:
                    print("Error: Approach Vektoren bilden failed (LM)")



                if closest_vec_G1 is retina.vec_mid_G1:
                    size_retina_G1 = retina.size_G1
                elif closest_vec_G1 is retina.vec_mid_G2:
                    size_retina_G1 = retina.size_G2
                elif closest_vec_G1 is retina.vec_mid_G3:
                    size_retina_G1 = retina.size_G3
                else:
                    print("Error: Approach Vektoren bilden failed (G)")

                if closest_vec_G2 is retina.vec_mid_G1:
                    size_retina_G2 = retina.size_G1
                elif closest_vec_G2 is retina.vec_mid_G2:
                    size_retina_G2 = retina.size_G2
                elif closest_vec_G2 is retina.vec_mid_G3:
                    size_retina_G2 = retina.size_G3
                else:
                    print("Error: Approach Vektoren bilden failed (G)")


                if closest_vec_G3 is retina.vec_mid_G1:
                    size_retina_G3 = retina.size_G1
                elif closest_vec_G3 is retina.vec_mid_G2:
                    size_retina_G3 = retina.size_G2
                elif closest_vec_G3 is retina.vec_mid_G3:
                    size_retina_G3 = retina.size_G3
                else:
                    print("Error: Approach Vektoren bilden failed (G)")


                Vp_list = []

                if snapshot.size_LM1 > size_retina_LM1:
                    Vp_list.append(closest_vec_LM1)
                else:
                    Vp_list.append(negVector(closest_vec_LM1))


                if snapshot.size_LM2 > size_retina_LM2:
                    Vp_list.append(closest_vec_LM2)
                else:
                    Vp_list.append(negVector(closest_vec_LM2))

                if snapshot.size_LM3 > size_retina_LM3:
                    Vp_list.append(closest_vec_LM3)
                else:
                    Vp_list.append(negVector(closest_vec_LM3))

                if snapshot.size_G1 > size_retina_G1:
                    Vp_list.append(closest_vec_G1)
                else:
                    Vp_list.append(negVector(closest_vec_G1))

                if snapshot.size_G2 > size_retina_G2:
                    Vp_list.append(closest_vec_G2)
                else:
                    Vp_list.append(negVector(closest_vec_G2))

                if snapshot.size_G3 > size_retina_G3:
                    Vp_list.append(closest_vec_G3)
                else:
                    Vp_list.append(negVector(closest_vec_G3))


                #print("    2)done!")


                #print("done!")

                #print("Generiere Vt & Vp")
                Vp = buildVp(Vp_list)
                Vt = buildVt(Vt_list)
                V = buildV(Vp, Vt)
                #print("done!")

                #print("Visualisiere")
                visualize(V,Point(pos_x,pos_y))
    plt.plot(lm1_x,lm1_y, marker='.', color='r', linestyle='none')
    plt.plot(lm2_x,lm2_y, marker='.', color='r', linestyle='none')
    plt.plot(lm3_x,lm3_y, marker='.', color='r', linestyle='none')
    plt.plot(0,0, marker='X', color='r', linestyle='none')
    visualize_show()


# In[ ]:




