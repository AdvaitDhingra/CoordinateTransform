from CoordinateTransformations import CoordinateSystem3D, CoordinateSystem2D
import sympy as sp
from sympy import sin, cos

x, y, z = sp.symbols('x y z')

a = CoordinateSystem3D(x*sin(z)*cos(y), x*sin(y)*sin(z), x*cos(z))
b = CoordinateSystem2D(x*cos(y), x*sin(y))

print(a.Transform())
print(b.Transform())

