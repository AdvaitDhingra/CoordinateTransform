from sympy import sin, cos, Derivative
import numpy as np

class CoordinateSystem2D:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def Transform(self):
        x, y = sp.symbols("x y")

        return np.array([[Derivative(self.x1, x), Derivative(self.x1, y)], [Derivative(self.x2, x), Derivative(self.x2, y)]])