import pickle
import heapq

# Load the graph from the pickle file
def load_graph_from_pickle(file_path):
    with open(file_path, 'rb') as f:
        graph = pickle.load(f)
    return graph

# Function to perform Dijkstra's algorithm with priority queue using heapq
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    previous = {}
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        # Checking if neighbor node exists in the graph
        if current_node not in graph:
            continue
        for neighbor in graph[current_node]:
            # Skipping neighbors with missing or None values
            if neighbor is None:
                continue
            distance = current_distance + 1  
            # Updating the distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Pushing the neighbor to the priority queue
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

# Function to print the result in correct format
def print_result(degree, path):
    l = len(path)
    print(f">> Degree of separation between {path[0]} and {path[l-1]} is {l//2}.")
    for n in range(0, len(path) - 1, 2):
        actor_name = path[n]
        movie_name = path[n + 1]
        next_actor_name = path[n + 2]
        print(f">> {actor_name} has starred with {next_actor_name} in the movie {movie_name}")
    print()


if __name__ == '__main__':
    # Load the graph from pickle file
    graph = load_graph_from_pickle('graph.pickle')

    source_actor = input("Enter the source actor: ")
    target_actor = input("Enter the target actor: ")
    print()
    result = degree_of_separation(graph, source_actor, target_actor)
    if isinstance(result, tuple) and len(result) == 2:
        degree, path = result
        if isinstance(result, tuple):
            degree, path = result
            if (len(path) % 2 != 0):
                print_result(degree, path)
            else:
                print(f"Failed for {path[0]}. Even number of nodes in the path means incorrect path.")
                print(path)
    else:
        print(result)
  
