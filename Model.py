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
        str_aufbau = "Das Model hat den Mittelpunkt bei: " +str(self.mittelpunkt.x)+"|"+str(self.mittelpunkt.y)
        str_aufbau = str_aufbau + "\n"
        return str_aufbau

        