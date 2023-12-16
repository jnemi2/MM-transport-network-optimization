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


def net_capacity_difference(capacity_matrix):
    return np.sum(capacity_matrix, axis=0) - np.sum(capacity_matrix, axis=1)


def balance_routes(capacity_matrix, graph_matrix):
    balance = net_capacity_difference(capacity_matrix)
    max_surplus = max(balance)
    max_deficit = min(balance)
    # max_surplus_node = balance.index(max_surplus)
    max_surplus_node = np.where(balance == max_surplus)[0][0]
    # max_deficit_node = balance.index(max_deficit)
    max_deficit_node = np.where(balance == max_deficit)[0][0]
    while balance[max_surplus_node] != 0:
        return_path = graph.find_path(max_surplus_node, max_deficit_node, graph_matrix)
        increment_path_capacity(return_path, min(max_surplus, -max_deficit), capacity_matrix)
        # balance again
        balance = net_capacity_difference(capacity_matrix)
        max_surplus = max(balance)
        max_deficit = min(balance)
        max_surplus_node = np.where(balance == max_surplus)[0][0]
        max_deficit_node = np.where(balance == max_deficit)[0][0]
        