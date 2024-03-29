import numpy as np
import graph


def increment_path_capacity(path, increment, capacity_matrix):
    if len(path) > 1:
        for node in range(len(path) - 1):
            capacity_matrix[path[node]][path[node + 1]] += increment


def get_path_capacity(path, capacity_matrix):
    capacity = float('inf')
    if len(path) > 1:
        for node in range(len(path) - 1):
            capacity = min(capacity, capacity_matrix[path[node]][path[node + 1]])
    return capacity


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
    # max_surplus_node = balance.index(max_surplus)
    max_surplus_node = np.where(balance == max_surplus)[0][0]
    
    distances, backtrack = graph.explore(max_surplus_node, graph_matrix)
    
    balance_distance = [-b * d if b < 0 else float('inf') for b, d in zip(balance.tolist(), distances)]
    
    close_deficit_node = balance_distance.index(min(balance_distance))

    close_deficit = balance[close_deficit_node]
    
    while balance[max_surplus_node] != 0:
        return_path = graph.find_path(max_surplus_node, close_deficit_node, graph_matrix)
        increment_path_capacity(return_path, min(max_surplus, -close_deficit), capacity_matrix)
        # balance again
        balance = net_capacity_difference(capacity_matrix)
        max_surplus = max(balance)
        max_surplus_node = np.where(balance == max_surplus)[0][0]
        distances, backtrack = graph.explore(max_surplus_node, graph_matrix)
        balance_distance = [-b * d if b < 0 else float('inf') for b, d in zip(balance.tolist(), distances)]
        close_deficit_node = balance_distance.index(min(balance_distance))
        close_deficit = balance[close_deficit_node]


def get_unused_capacity(capacity_matrix, flux_matrix, graph_matrix):
    return capacity_matrix - capacity_for_flux(flux_matrix, graph_matrix)


def cost_per_unused_capacity(capacity_matrix, flux_matrix, graph_matrix):
    unused_capacity_cost = get_unused_capacity(capacity_matrix, flux_matrix, graph_matrix)
    node_index = 0
    for node in unused_capacity_cost:
        unused_index = 0
        for unused in node:
            if unused > 0:
                unused_capacity_cost[node_index][unused_index] *= graph_matrix[node_index][unused_index]
            unused_index += 1
        node_index += 1
    return unused_capacity_cost


def get_routes(capacity_matrix, graph_matrix):
    capacity = np.copy(capacity_matrix)
    matrix = np.copy(graph_matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if capacity[i][j] == 0:
                matrix[i][j] = float('inf')
    routes = []
    route_origin = 0
    for o in range(len(capacity)):
        node = capacity[route_origin]
        adj_node_index = 0
        for a in range(len(node)):
            if node[adj_node_index] > 0:
                return_path = graph.find_path(adj_node_index, route_origin, matrix)
                return_path.insert(0, route_origin)
                path_capacity = get_path_capacity(return_path, capacity)
                increment_path_capacity(return_path, -path_capacity, capacity)
                routes.append({'capacity': path_capacity, 'path': return_path})
                # update graph
                for n in range(len(return_path) - 1):
                    if capacity[return_path[n]][return_path[n+1]] == 0:
                        matrix[return_path[n]][return_path[n+1]] = float('inf')
            adj_node_index += 1
        route_origin += 1
    return routes
