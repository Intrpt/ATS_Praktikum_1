import numpy as np
import matplotlib.pyplot as plt
from Vector import Vector
from Point import Point
from Model import Model

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


