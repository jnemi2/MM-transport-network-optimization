import numpy as np
from graph import *
from transport import *

inf = float('inf')

graph_matrix = [
    [inf, 5, inf, inf, 6, 8, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [5, inf, 5, inf, 8, 6, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [inf, 5, inf, 5, inf, inf, 6, inf, inf, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, 5, inf, inf, inf, inf, 6, inf, inf, inf, inf, inf, inf, inf, inf],
    [6, 8, inf, inf, inf, 5, inf, inf, 6, inf, inf, inf, inf, inf, inf, inf],
    [8, 6, inf, inf, 5, inf, 5, inf, inf, 6, inf, inf, inf, inf, inf, inf],
    [inf, inf, 6, inf, inf, 5, inf, 5, inf, inf, 6, inf, inf, inf, inf, inf],
    [inf, inf, inf, 6, inf, inf, 5, inf, inf, inf, inf, 6, inf, inf, inf, inf],
    [inf, inf, inf, inf, 6, inf, inf, inf, inf, 5, inf, inf, 6, inf, inf, inf],
    [inf, inf, inf, inf, inf, 6, inf, inf, 5, inf, 5, inf, inf, 6, inf, inf],
    [inf, inf, inf, inf, inf, inf, 6, inf, inf, 5, inf, 5, inf, inf, 6, inf],
    [inf, inf, inf, inf, inf, inf, inf, 6, inf, inf, 5, inf, inf, inf, inf, 6],
    [inf, inf, inf, inf, inf, inf, inf, inf, 6, inf, inf, inf, inf, 5, inf, inf],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, 6, inf, inf, 5, inf, 5, inf],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 6, inf, inf, 5, inf, 5],
    [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 6, inf, inf, 5, inf]
]


flux_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

capacity = capacity_for_flux(flux_matrix, graph_matrix)
print(capacity)
print(net_capacity_difference(capacity))
balance_routes(capacity, graph_matrix)
print(capacity)
routes = get_routes(capacity, graph_matrix)
#for r in routes:
#    print(r)

print(get_unused_capacity(capacity, flux_matrix, graph_matrix))
cost = cost_per_unused_capacity(capacity, flux_matrix, graph_matrix)
print(cost)
print(sum(sum(cost)))

for r in routes:
    print(r)
    