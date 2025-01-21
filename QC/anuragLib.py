class Vectors:
    def __init__(self, Nh=0, Nv=0, Nl=0, Nd=0):
        self.Nh = Nh
        self.Nv = Nv
        self.Nl = Nl
        self.Nd = Nd

    def get_Nh(self):
        return self.Nh

    def set_Nh(self, Nh):
        self.Nh = Nh

    def get_Nv(self):
        return self.Nv

    def set_Nv(self, Nv):
        self.Nv = Nv

    def get_Nl(self):
        return self.Nl

    def set_Nl(self, Nl):
        self.Nl = Nl

    def get_Nd(self):
        return self.Nd

    def set_Nd(self, Nd):
        self.Nd = Nd

    def inputData(self):
        print(f"input Data: \nNh={self.get_Nh()}\nNv={self.get_Nv()}\nNl={self.get_Nl()}\nNd={self.get_Nd()}")

    def Ntotal(self):
        return self.Nh + self.Nv

    def probOfVectors(self):
        Ph=self.Nh/self.Ntotal()
        Pl=self.Nl/self.Ntotal()
        Pd=self.Nd/self.Ntotal()
        print(f"Ph={Ph}\nPl={Pl}\nPd={Pd}")
        return Ph,Pl,Pd
    
    def setAllVectors(self):
        print("Enter the values for Nh, Nv, Nl, Nd")
        inputNh = int(input("Nh: "))
        inputNv = int(input("Nv: "))
        inputNl = int(input("Nl: "))
        inputNd = int(input("Nd: "))
        self.set_Nh(inputNh)
        self.set_Nv(inputNv)
        self.set_Nl(inputNl)
        self.set_Nd(inputNd)
        print("Values set successfully")



