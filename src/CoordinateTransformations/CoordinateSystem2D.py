from sympy import sin, cos, Derivative
import sympy as sp
import numpy as np

class CoordinateSystem2D:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def TransformationMatrix(self):
        x, y = sp.symbols("x y")

        return np.array([[Derivative(self.x1, x).doit(), Derivative(self.x1, y).doit()], [Derivative(self.x2, x).doit(), Derivative(self.x2, y).doit()]])
    def Multiply(self, Matrix, Vector):
        x, y = sp.symbols("x y")
        for i in range(0, len(Matrix)):
            for j in range(0, len(Matrix[i])):
                Matrix[i][j] = Matrix[i][j].subs({x: Vector[0], y: Vector[1]})

        return Matrix.dot(Vector)
