import numpy as np
import matplotlib.pyplot as plt
from Vector import Vector
from Point import Point
from Model import Model
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
        if ang_tmp_2 > ang_tmp_1:
            size = ang_tmp_2 - ang_tmp_1
        #3b)
        else:
            size = 360 - ang_tmp_2 + ang_tmp_1




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
#visualize(Vektor V)

def visualize(V):
    #TODO virtualisieren
    return 1


