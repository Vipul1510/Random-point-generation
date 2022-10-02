import math
import random

import matplotlib.pyplot as plt

def trisample(A, B, C):
    """
    Given three vertices A, B, C, 
    sample point uniformly in the triangle
    """
    r1 = random.random()
    r2 = random.random()

    s1 = math.sqrt(r1)

    x = A[0] * (1.0 - s1) + B[0] * (1.0 - r2) * s1 + C[0] * r2 * s1
    y = A[1] * (1.0 - s1) + B[1] * (1.0 - r2) * s1 + C[1] * r2 * s1

    return (x, y)

random.seed(312345)
A = (0, 0)
B = (math.pi, 0)
C = (math.pi/3, math.e)
points = [trisample(A, B, C) for _ in range(10000)]

xx, yy = zip(*points)
plt.title("Generating Random locations within a triangular domain")
plt.scatter(xx, yy, s=0.2)
plt.show()
