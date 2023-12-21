
def nodes_to_go_from(origin, matrix):
    nodes = []
    index = 0
    inf = float('inf')
    for weight in matrix[origin]:
        if weight < inf:
            nodes.append(index)
        index += 1
    return nodes

def find_min_index(numbers, indexes):
    min_index = None
    min_value = float('inf')
    
    for index in indexes:
        if 0 <= index < len(numbers):
            if numbers[index] < min_value:
                min_value = numbers[index]
                min_index = index
    
    return min_index


def explore(origin, matrix):
    distances = [float('inf')] * len(matrix)
    distances[origin] = 0
    backtrack = [None] * len(matrix)  # store the index of the node from which the distance was updated
    visited_nodes = set()
    unvisited_nodes = set([origin])

    while len(unvisited_nodes) > 0:
        # select an unvisited node
        current_node = find_min_index(distances, unvisited_nodes)
        current_distance = distances[current_node]
        
        # find adjacent nodes
        adjacent_nodes = set(nodes_to_go_from(current_node, matrix)) - set([current_node])
        # update unvisited nodes
        unvisited_nodes = unvisited_nodes.union(adjacent_nodes) - visited_nodes
        visited_nodes = visited_nodes.union(set([current_node]))
        # update distances
        for adj_node in adjacent_nodes:
            distance_from_here = matrix[current_node][adj_node] + current_distance
            if distance_from_here < distances[adj_node]:
                distances[adj_node] = distance_from_here
                backtrack[adj_node] = current_node  # update shortest path to origin
    
    return distances, backtrack


def get_distances(origin, matrix):
    distances, backtrack = explore(origin, matrix)
    return distances


def get_path(destination, backtrack):
    path = []
    temp_node = destination
    while temp_node is not None:
        path.insert(0, temp_node)
        temp_node = backtrack[temp_node]
    return path


def find_path(origin, destination, matrix):
    distances, backtrack = explore(origin, matrix)
    return get_path(destination, backtrack)