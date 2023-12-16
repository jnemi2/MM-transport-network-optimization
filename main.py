import numpy as np
from graph import *

matrix = [
    [0, 4, 2, float('inf'), float('inf')],
    [4, 0, 1, 3, 2],
    [2, 1, 0, float('inf'), float('inf')],
    [float('inf'), 3, float('inf'), 0, 5],
    [float('inf'), 2, float('inf'), 5, 0]
]

print(find_path(0, 4, matrix))
