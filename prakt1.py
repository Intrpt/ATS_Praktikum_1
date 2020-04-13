import numpy as np
import matplotlib.pyplot as plt
from Vector import Vector
from Point import Point
from Model import Model
import numpy as np
from Landmark import Landmark

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

    for x in range(0,2):
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
        ang_tmp_1 = getAngBetween(Vector(Point(0,1)),Schnittpunkt1)
        ang_tmp_2 = getAngBetween(Vector(Point(0,1)),Schnittpunkt2)
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
            m.ang_1_LM1 = ang_tmp_1
            m.ang_2_LM1 = ang_tmp_2
            m.ang_mid_LM1 = ((ang_tmp_2 - ang_tmp_1) / 2) + ang_tmp_1
            m.size_LM1 = size
        elif x == 1:
            # LM2 (G2) abarbeiten
            m.vec_mid_LM2 = vec_model_lm_mittelpunkt
            m.ang_1_LM2 = ang_tmp_1
            m.ang_2_LM2 = ang_tmp_2
            m.ang_mid_LM2 = ((ang_tmp_2 - ang_tmp_1) / 2) + ang_tmp_1
            m.size_LM2 = size
        elif x == 2:
            # LM3 (G3) abarbeiten
            m.vec_mid_LM3 = vec_model_lm_mittelpunkt
            m.ang_1_LM3 = ang_tmp_1
            m.ang_2_LM3 = ang_tmp_2
            m.ang_mid_LM3 = ((ang_tmp_2 - ang_tmp_1) / 2) + ang_tmp_1
            m.size_LM3 = size
            # Alle G werte berechnen
            # Für G1
            if m.ang_1_LM2 > m.ang_2_LM1:
                m.ang_mid_G1 =  ((m.ang_1_LM2 - m.ang_2_LM1) / 2) + m.ang_2_LM1
            elif m.ang_1_LM2 < m.ang_2_LM1:
                m.ang_mid_G1 =  (((m.ang_1_LM2+360) - m.ang_2_LM1) / 2) + m.ang_2_LM1
            if m.ang_1_LM2 > m.ang_2_LM1:
                m.size_G1 = m.ang_1_LM2 - m.ang_2_LM1
            else:
                m.size_G1 = 360 - m.ang_1_LM2 + m.ang_2_LM1
            m.vec_mid_G1 = getMidVec(m.ang_2_LM1,m.ang_1_LM2)

            # Für G2
            if m.ang_1_LM3 > m.ang_2_LM2:
                m.ang_mid_G2 =  ((m.ang_1_LM3 - m.ang_2_LM2) / 2) + m.ang_2_LM2
            elif m.ang_1_LM3 < m.ang_2_LM2:
                m.ang_mid_G2 =  (((m.ang_1_LM3+360) - m.ang_2_LM2) / 2) + m.ang_2_LM2
            if m.ang_1_LM3 > m.ang_2_LM2:
                m.size_G2 = m.ang_1_LM3 - m.ang_2_LM2
            else:
                m.size_G2 = 360 - m.ang_1_LM3 + m.ang_2_LM2
            m.vec_mid_G2 = getMidVec(m.ang_2_LM2,m.ang_1_LM3)

            # Für G3
            if m.ang_1_LM1 > m.ang_2_LM3:
                m.ang_mid_G3 =  ((m.ang_1_LM1 - m.ang_2_LM3) / 2) + m.ang_2_LM3
            elif m.ang_1_LM1 < m.ang_2_LM3:
                m.ang_mid_G3 =  (((m.ang_1_LM1+360) - m.ang_2_LM3) / 2) + m.ang_2_LM3
            if m.ang_1_LM1 > m.ang_2_LM3:
                m.size_G3 = m.ang_1_LM1 - m.ang_2_LM3
            else:
                m.size_G3 = 360 - m.ang_1_LM1 + m.ang_2_LM3
            m.vec_mid_G2 = getMidVec(m.ang_2_LM3,m.ang_1_LM1)

  
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
    v.p.x = Vp.p.x + 3 * Vt.p.x
    v.p.y = Vp.p.y + 3 * Vt.p.y
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
