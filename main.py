import numpy as np
from graph import *
from transport import *

inf = float('inf')

graph_matrix = [
    [0, 4, 3, inf, inf, inf, inf, inf, inf, 8, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [4, 0, 7, inf, inf, inf, inf, inf, inf, 2, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [3, 7, 0, 4, inf, inf, inf, inf, inf, 5, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, 4, 0, 6, inf, inf, inf, 2, 1, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, inf, 6, 0, 5, 7, inf, inf, 4, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, inf, inf, 5, 0, inf, 6, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, inf, inf, 7, inf, 0, 3, 5, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, inf, inf, inf, 6, 3, 0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, inf, 2, inf, inf, 5, inf, 0, inf, 3, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [8, 2, 5, 1, 4, inf, inf, inf, inf, 0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, inf, inf, inf, inf, inf, inf, 3, inf, 0, 7, inf, 6, 2, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 7, 0, 5, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 5, 0, 4, 3, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 6, inf, 4, 0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 2, inf, 3, inf, 0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0, 9, 3, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 9, 0, 5, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 3, 5, 0, 6, 4, inf, inf, inf, inf, inf],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 6, 0, inf, inf, 8, 7, inf, inf],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 4, inf, 0, inf, inf, inf, 8, inf],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 0, 5, inf, inf, inf],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 8, inf, 5, 0, inf, 2, inf],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 7, inf, inf, inf, 0, inf, 5],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 8, inf, 2, inf, 0, inf],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 5, inf, 0]
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
routes = get_routes(flux_matrix, capacity, graph_matrix)

print(get_unused_capacity(capacity, flux_matrix, graph_matrix))
cost = cost_per_unused_capacity(capacity, flux_matrix, graph_matrix)
print(cost)
print(sum(sum(cost)))

for r in routes:
    print(r)
