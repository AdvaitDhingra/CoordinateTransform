import sympy as sp
import numpy as np
from sympy.core.function import Derivative

class CoordinateSystem:
    def __init__(self, x1=0, x2=0, x3=0):
        if (isinstance(x1, int) and isinstance(x2, int) and isinstance(x3, int)):
            self.x1 = x1
            self.x2 = x2
            self.x3 = x3
        else:
            self.x, self.y, self.z = sp.symbols("x y z");
            self.x1 = x1
            self.x2 = x2
            self.x3 = x3 


    def x1(self):
        return self.x1
    def x2(self):
        return self.x2
    def x3(self):
        return self.x3

    
    
    def Transform(SecondCoordinateSystem):

        x, y, z = sp.symbols("x y z")
        a = [sp.Derivative(SecondCoordinateSystem.x1, x), sp.Derivative(SecondCoordinateSystem.x1, y), sp.Derivative(SecondCoordinateSystem.x1, z)]
        b = [sp.Derivative(SecondCoordinateSystem.x2, x), sp.Derivative(SecondCoordinateSystem.x2, y), sp.Derivative(SecondCoordinateSystem.x2, z)]
        c = [sp.Derivative(SecondCoordinateSystem.x3, x), sp.Derivative(SecondCoordinateSystem.x3, y), sp.Derivative(SecondCoordinateSystem.x3, z)]
        return np.array([a,b,c])


