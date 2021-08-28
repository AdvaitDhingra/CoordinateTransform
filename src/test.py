from CoordinateTransformations import CoordinateSystem3D, CoordinateSystem2D
import sympy as sp
import numpy as np
from sympy import sin, cos

x, y, z = sp.symbols('x y z')

b = CoordinateSystem2D(2*x, 2*y)

matrix = b.TransformationMatrix();

c = b.Multiply(matrix, np.array([1, 1]))

print(c)


