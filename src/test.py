from CoordinateTransformations import CoordinateSystem2D
import sympy as sp
from sympy import sin, cos
import numpy as np

x, y = sp.symbols('x y')
a = CoordinateSystem2D(x*cos(y), x*sin(y))
matrix = a.TransformationMatrix()
answer = a.Multiply(matrix, np.array([1, 2]))
print(answer)