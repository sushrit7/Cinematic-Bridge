import pickle
import heapq

# Load the graph from the pickle file
def load_graph_from_pickle(file_path):
    with open(file_path, 'rb') as f:
        graph = pickle.load(f)
    return graph

def load_title_from_pickle():
    with open("title.pickle", 'rb') as f:
        title = pickle.load(f)
    return title

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

def get_movie(movie_id):
    title_data = load_title_from_pickle()
    movies = []
    for movie in movie_id:
        movie_name = title_data.get(movie, None)
        # print(movie_name)
        movies.append(movie_name)
    return movies


def print_result(degree, path, source_actor, target_actor):
    movie_names = get_movie(path)
    print(f">> Degree of separation between {source_actor} and {target_actor} is {degree//2}.")
    for n in range(0, len(path) - 1, 2):
        actor_name = path[n]
        movie_name = movie_names[n + 1]
        next_actor_name = path[n + 2]
        print(f">> {actor_name} has starred with {next_actor_name} in the movie {movie_name}")


if __name__ == '__main__':
    # Load the graph from pickle file
    graph = load_graph_from_pickle('graph.pickle')

    # Example usage
    source_actor = 'Jim Carrey'
    target_actor = 'Jeff Daniels'
    result = degree_of_separation(graph, source_actor, target_actor)
    if isinstance(result, tuple) and len(result) == 2:
        degree, path = result
        print_result(degree, path, source_actor, target_actor)
    #     print(f"Degree of separation between {source_actor} and {target_actor}: {degree/2}")
    #     if isinstance(path, list):
    #         print("Path:")
    #         for i in range(len(path) - 1):
    #             print(f"{path[i]} - {path[i+1]}")
    # else:
    #     print(result)  # If result is not a tuple of length 2, print the result directly
