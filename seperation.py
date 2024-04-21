import pickle
import heapq

# Load the graph from the pickle file
def load_graph_from_pickle(file_path):
    with open(file_path, 'rb') as f:
        graph = pickle.load(f)
    return graph

# Define function to find shortest path using Dijkstra's algorithm
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    previous = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph[current_node]:
            distance = current_distance + 1  # Assuming all edges have weight 1
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                previous[neighbor] = current_node

    return distances, previous

# Get the path from source to target
def get_path(previous, target):
    path = []
    current_node = target
    while current_node in previous:
        path.append(current_node)
        current_node = previous[current_node]
    path.append(current_node)
    return path[::-1]

# Example usage
def degree_of_separation(graph, source_actor, target_actor):
    distances, previous = dijkstra(graph, source_actor)
    if target_actor not in distances:
        return "No connection found"
    path = get_path(previous, target_actor)
    degree = distances[target_actor]
    return degree, path

# Load the graph from pickle file
graph = load_graph_from_pickle('graph.pickle')

# Example usage
source_actor = 'Jim Carrey'
target_actor = 'Jeff Daniels'
result = degree_of_separation(graph, source_actor, target_actor)
if isinstance(result, tuple) and len(result) == 2:
    degree, path = result
    print(f"Degree of separation between {source_actor} and {target_actor}: {degree}")
    if isinstance(path, list):
        print("Path:")
        for i in range(len(path) - 1):
            print(f"{path[i]} - {path[i+1]}")
else:
    print(result)  # If result is not a tuple of length 2, print the result directly
