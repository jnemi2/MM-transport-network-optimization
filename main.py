import numpy as np
from graph import *
from transport import *

graph_matrix = [
    [0, 4, 2, float('inf'), float('inf')],
    [4, 0, 1, 3, 2],
    [2, 1, 0, float('inf'), float('inf')],
    [float('inf'), 3, float('inf'), 0, 5],
    [float('inf'), 2, float('inf'), 5, 0]
]

flux_matrix = [
    [0, 0, 2, 0, 90],
    [4, 0, 0, 0, 0],
    [2, 0, 0, 0, 0],
    [50, 3, 0, 0, 0],
    [0, 0, 0, 50, 0]
]

capacity = capacity_for_flux(flux_matrix, graph_matrix)
print(capacity)
print(net_capacity_difference(capacity))
balance_routes(capacity, graph_matrix)
print(capacity)
routes = get_routes(capacity, graph_matrix)
#print(get_path_capacity([1,4,1], capacity))
for r in routes:
    print(r)
