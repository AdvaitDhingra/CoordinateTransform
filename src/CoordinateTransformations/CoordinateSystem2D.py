from sympy import sin, cos, Derivative
import sympy as sp
import numpy as np

class CoordinateSystem2D:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        self.x, self.y = sp.symbols('x y')

    def TransformationMatrix(self):
        return np.array([[Derivative(self.x1, self.x).doit(), Derivative(self.x1, self.y).doit()], [Derivative(self.x2, self.x).doit(), Derivative(self.x2, self.y).doit()]])
    def Multiply(self, Matrix, Vector):
        for i in range(0, len(Matrix)):
            for j in range(0, len(Matrix[i])):
                Matrix[i][j] = Matrix[i][j].subs({self.x: Vector[0], self.y: Vector[1]})

        return Matrix.dot(Vector)
