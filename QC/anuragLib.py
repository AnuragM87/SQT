import numpy as np

class SingleQubitTomography:
    def __init__(self, Nh=0, Nv=0, Nl=0, Nd=0):
        self.Nh = Nh
        self.Nv = Nv
        self.Nl = Nl
        self.Nd = Nd
        self.Ph = 0
        self.Pl = 0
        self.Pd = 0
        self.Pv = 0

    # Getter and Setter for Nh, Nv, Nl, Nd
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

    # Getter and Setter for Probabilities (Ph, Pl, Pd, Pv)
    def set_Ph(self):
        self.Ph = self.Nh / self.Ntotal() if self.Ntotal() > 0 else 0

    def get_Ph(self):
        return self.Ph

    def set_Pl(self):
        self.Pl = self.Nl / self.Ntotal() if self.Ntotal() > 0 else 0

    def get_Pl(self):
        return self.Pl

    def set_Pd(self):
        self.Pd = self.Nd / self.Ntotal() if self.Ntotal() > 0 else 0

    def get_Pd(self):
        return self.Pd

    def set_Pv(self):
        self.Pv = self.Nv / self.Ntotal() if self.Ntotal() > 0 else 0

    def get_Pv(self):
        return self.Pv

    # Display input data
    def inputData(self):
        print(f"Input Data: \nNh={self.get_Nh()}\nNv={self.get_Nv()}\nNl={self.get_Nl()}\nNd={self.get_Nd()}")

    # Calculate total measurements
    def Ntotal(self):
        return self.Nh + self.Nv

    # Calculate probabilities
    def probOfVectors(self):
        self.set_Ph()
        self.set_Pl()
        self.set_Pd()
        self.set_Pv()
        Ph = self.get_Ph()
        Pl = self.get_Pl()
        Pd = self.get_Pd()
        Pv = self.get_Pv()
        print(f"Probabilities:\nPh={Ph:.3f}\nPl={Pl:.3f}\nPd={Pd:.3f}\nPv={Pv:.3f}")
        return round(Ph, 3), round(Pl, 3), round(Pd, 3), round(Pv, 3)

    # Set all vector values
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

    # Generate a column matrix
    def generateMatrix(self):
        self.probOfVectors()
        values = [1, 2 * self.Nh - 1, 2 * self.Nl - 1, 2 * self.Nd - 1]
        matrix = np.array(values).reshape(-1, 1)
        print("Generated Matrix:")
        print(matrix)
        return matrix
