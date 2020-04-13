class Model:
    """docstring for Model"""
    #vec_mid_LM1,vec_mid_LM2, vec_mid_LM3;
    #ang_mid_LM1, ang_mid_LM2, ang_mid_LM3;
    #ang_1_LM1, ang_2_LM1, ang_1_LM2, ang_2_LM2, ang_1_LM3, ang_2_LM3;  ( gesehn auf den gesammten Kreis, im Uhrzeigersinn)
    #size_LM1, size_LM2, size_LM3
    #size_G1, size_G2, size_G3
    #ang_mid_G1, ang_mid_G2, ang_mid_G3
    #vec_mid_G1, vec_mid_G2, vec_mid_G3

    def __init__(self, mittelpunkt, radius):
        super(Model, self).__init__()
        self.mittelpunkt = mittelpunkt
        self.radius = radius
        self.vec_mid_LM1 = self.vec_mid_LM2 = self.vec_mid_LM3 = None
        self.ang_mid_LM1 = self.ang_mid_LM2 = self.ang_mid_LM3 = None
        self.ang_1_LM1 = self.ang_2_LM1 = self.ang_1_LM2 = self.ang_2_LM2 = self.ang_1_LM3= self.ang_2_LM3 = None
        self.size_LM1 = self.size_LM2 = self.size_LM3 = None
        self.size_G1 = self.size_G2 =self.size_G3 = None
        self.ang_mid_G1 = self.ang_mid_G2 = self.ang_mid_G3 = None
        self.vec_mid_G1 = self.vec_mid_G2 = self.vec_mid_G3 = None

    def __str__(self):
        str_aufbau = "----\nDas Model hat den Mittelpunkt bei: " +str(self.mittelpunkt.x)+"|"+str(self.mittelpunkt.y)
        str_aufbau = str_aufbau + "\nDer Radius ist: "+ str(self.radius)
        str_aufbau = str_aufbau + "\nvec_mid_LM1: "+str(self.vec_mid_LM1.p.x)+"|"+str(self.vec_mid_LM1.p.y)
        str_aufbau = str_aufbau + "\nvec_mid_LM2: "+str(self.vec_mid_LM2.p.x)+"|"+str(self.vec_mid_LM2.p.y)
        str_aufbau = str_aufbau + "\nvec_mid_LM3: "+str(self.vec_mid_LM3.p.x)+"|"+str(self.vec_mid_LM3.p.y)
        str_aufbau = str_aufbau + "\nvec_mid_G1: "+str(self.vec_mid_G1.p.x)+"|"+str(self.vec_mid_G1.p.y)
        str_aufbau = str_aufbau + "\nvec_mid_G2: "+str(self.vec_mid_G2.p.x)+"|"+str(self.vec_mid_G2.p.y)
        str_aufbau = str_aufbau + "\nvec_mid_G3: "+str(self.vec_mid_G3.p.x)+"|"+str(self.vec_mid_G3.p.y)

        str_aufbau = str_aufbau + "\n"
        
        str_aufbau = str_aufbau + "\nang_mid_LM1: "+str(self.ang_mid_LM1)+"°"
        str_aufbau = str_aufbau + "\nang_mid_LM2: "+str(self.ang_mid_LM2)+"°"
        str_aufbau = str_aufbau + "\nang_mid_LM3: "+str(self.ang_mid_LM3)+"°"
        str_aufbau = str_aufbau + "\nang_mid_G1: "+str(self.ang_mid_G1)+"°"
        str_aufbau = str_aufbau + "\nang_mid_G2: "+str(self.ang_mid_G2)+"°"
        str_aufbau = str_aufbau + "\nang_mid_G3: "+str(self.ang_mid_G3)+"°"



        str_aufbau = str_aufbau + "\n"


        str_aufbau = str_aufbau + "\nsize_LM1: "+str(self.size_LM1)+"°"
        str_aufbau = str_aufbau + "\nsize_LM2: "+str(self.size_LM2)+"°"
        str_aufbau = str_aufbau + "\nsize_LM3: "+str(self.size_LM3)+"°"
        str_aufbau = str_aufbau + "\nsize_G1: "+str(self.size_G1)+"°"
        str_aufbau = str_aufbau + "\nsize_G2: "+str(self.size_G2)+"°"
        str_aufbau = str_aufbau + "\nsize_G3: "+str(self.size_G3)+"°"

        str_aufbau = str_aufbau + "\nang_1_LM1: "+str(self.ang_1_LM1)+"°"
        str_aufbau = str_aufbau + "\nang_2_LM1: "+str(self.ang_2_LM1)+"°"
        str_aufbau = str_aufbau + "\nang_1_LM2: "+str(self.ang_1_LM2)+"°"
        str_aufbau = str_aufbau + "\nang_2_LM2: "+str(self.ang_2_LM2)+"°"
        str_aufbau = str_aufbau + "\nang_1_LM3: "+str(self.ang_1_LM3)+"°"
        str_aufbau = str_aufbau + "\nang_2_LM3: "+str(self.ang_2_LM3)+"°"


        str_aufbau = str_aufbau + "\n----"
        return str_aufbau

        