from prakt1 import *

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
    pos_x = 7
    pos_y = -7

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

        # tmp = 0
        # visualize(turn_vector_LM1,Point(1,tmp))
        # tmp = tmp + 1
        # visualize(turn_vector_LM1,Point(1,tmp))
        # tmp = tmp + 1
        # visualize(turn_vector_LM3,Point(1,tmp))
        # tmp = tmp + 1
        # visualize_show()

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

        tmp = 0
        visualize(closest_vec_G1,Point(1,tmp))
        tmp = tmp + 1
        visualize(closest_vec_G2,Point(1,tmp))
        tmp = tmp + 1
        visualize(closest_vec_G3,Point(1,tmp))
        tmp = tmp + 1
        visualize_show()

        tmp = 0
        visualize(turn_vector_G1,Point(1,tmp))
        tmp = tmp + 1
        visualize(turn_vector_G2,Point(1,tmp))
        tmp = tmp + 1
        visualize(turn_vector_G3,Point(1,tmp))
        tmp = tmp + 1
        visualize_show()


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
        c = 0
        Vp = buildVp(Vp_list)
        print("es folget Vp\n")
        for p in Vp_list:
            print(str(p.p.x)+"|"+str(p.p.y))
            visualize(p,Point(pos_x+1,pos_y+c))
            c = c+1
        print("\nVp: "+str(Vp.p.x)+"|"+str(Vp.p.y))

        print("es folget VT\n")
        Vt = buildVt(Vt_list)
        for p in Vt_list:
            print(str(p.p.x)+"|"+str(p.p.y))
            visualize(p,Point(pos_x+2,pos_y+c))
            c = c+1

        print("\nVt: "+str(Vt.p.x)+"|"+str(Vt.p.y))
        V = buildV(Vp, Vt)
        #print("done!")

        #print("Visualisiere")
        visualize(V,Point(pos_x,pos_y))


    print(snapshot)
    print("-------")
    print(retina)



    plt.plot(lm1_x,lm1_y, marker='.', color='r', linestyle='none')
    plt.plot(lm2_x,lm2_y, marker='.', color='r', linestyle='none')
    plt.plot(lm3_x,lm3_y, marker='.', color='r', linestyle='none')
    plt.plot(0,0, marker='X', color='r', linestyle='none')
    visualize_show()
