from prakt1 import *


for x in range(0,3):
    print(x)


print("--------------------")
print("Erstelle Landmarks")
print("--------------------")
#(3.5|2)
lm1 = Landmark(Point(3.5,2),1)
#(3.5|-2)
lm2 = Landmark(Point(3.5,-2),1)
#(0|-4)
lm3 = Landmark(Point(0,-4),1)

print("--------------------")
print("Test der FUnktion buildModel")
print("--------------------")

mo = buildmodel(-3,-3,1,lm1,lm2,lm3)
print(mo)


print("--------------------")
print("Test der FUnktion getMidVec")
print("--------------------")
v = getMidVec(133.9, 165, Landmark(Point(0,0),1))
print("Der vektor ist nun: "+str(v.p.x)+"|"+str(v.p.y))

print("--------------------")
print("Test der FUnktion getMidVec")
print("--------------------")
v = getMidVec(105, 74.5, Landmark(Point(0,0),1))
print("Der vektor ist nun: "+str(v.p.x)+"|"+str(v.p.y))

""" print("--------------------")
print("Test von addVectors")
print("--------------------")

vec1 = Vector(Point(1,1))
vec2 = Vector(Point(-2,-2))

ad = addVectors(vec1,vec2)

print("Der vektor ist nun: "+str(ad.p.x)+"|"+str(ad.p.y))

print("--------------------")
print("Test von moveModel")
print("--------------------")

mo = moveModel(mo,-3,-3)
print(mo)


print("--------------------")
print("Test von buildVt")
print("--------------------")

vtpaare = {Vector(Point(2,5)),Vector(Point(5,2)),Vector(Point(-2,5))}

vtsol = buildVt(vtpaare)
print("Der vektor von den Vt paaren ist: "+str(vtsol.p.x)+"|"+str(vtsol.p.y))

print("--------------------")
print("Test von buildVp")
print("--------------------")

vppaare = {Vector(Point(-1,-2)),Vector(Point(-4,-3))}

vpsol = buildVp(vppaare)
print("Der vektor von den Vp paaren ist: "+str(vpsol.p.x)+"|"+str(vpsol.p.y))


print("--------------------")
print("Test von buildV")
print("--------------------")


vv = buildV(vpsol,vtsol)
print("Der vektor von V ist: "+str(vv.p.x)+"|"+str(vv.p.y))


print("--------------------")
print("Test von visualization")
print("--------------------")


visualize(Vector(Point(0,1)),Point(3.5,2))
visualize(Vector(Point(0,-11)),Point(3.5,-2))
visualize(Vector(Point(0,1)),Point(0,-4))

visualize_show()

print("--------------------")
print("Finished Tests")
print("--------------------") """