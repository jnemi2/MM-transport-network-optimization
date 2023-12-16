import numpy as np
import graph


def increment_path_capacity(path, increment, capacity_matrix):
    if len(path) > 1:
        for node in range(len(path) - 1):
            capacity_matrix[path[node]][path[node + 1]] += increment


def capacity_for_flux(flux, graph_matrix):
    capacity = np.zeros((len(flux), len(flux)), dtype=int)
    origin_index = 0
    for origin in flux:
        destination = 0
        for f in origin:
            if f > 0:
                path = graph.find_path(origin_index, destination, graph_matrix)
                increment_path_capacity(path, f, capacity)
            destination += 1
        origin_index += 1
    return capacity
