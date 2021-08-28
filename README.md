# CoordinateTransform

This is a Python tool intended to be used to transform Vectors (and one day Tensors) to different Coordinate Systems.

These coordinate systems can be completely arbitrary, as they just require a coordinate system transformation formula.

## Example:

```python
from CoordinateTransformations import CoordinateSystem2D
import sympy as sp
from sympy import sin, cos 
import numpy as np

x, y = sp.symbols('x y')
a = CoordinateSystem2D(x*cos(y), x*sin(y))
matrix = a.TransformationMatrix()
answer = a.Multiply(matrix, np.array([1, 2]))
print(answer)
```
output:
``[-2*sin(2) + cos(2) 2*cos(2) + sin(2)]``.
In an ideal senario it would calculate the values but this isnt the case at the moment.



