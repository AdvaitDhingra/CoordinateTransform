import sympy as sp
import numpy as np
from sympy import Derivative, Symbol, sin, cos


class CoordinateSystem3D:
    def __init__(self, x1=0, x2=0, x3=0):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

    def TransformationMatrix(self):

        x, y, z = sp.symbols("x y z")

        return np.array([
            [sp.Derivative(self.x1, x).doit(), sp.Derivative(self.x1, y).doit(), sp.Derivative(self.x1, z).doit()],
            [sp.Derivative(self.x2, x).doit(), sp.Derivative(self.x2, y).doit(), sp.Derivative(self.x2, z).doit()],
            [sp.Derivative(self.x3, x).doit(), sp.Derivative(self.x3, y).doit(), sp.Derivative(self.x3, z).doit()]])

    def Multiply(self, Matrix, Vector):
        x, y, z = sp.symbols("x y z")
        for i in range(0, len(Matrix)):
            for j in range(0, len(Matrix[i])):
                Matrix[i][j] = Matrix[i][j].subs({x: Vector[0], y: Vector[1], z: Vector[2]})

        return Matrix.dot(Vector)
