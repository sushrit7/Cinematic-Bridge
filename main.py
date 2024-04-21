import pickle
from collections import deque

# Load the graph from the pickle file
def load_graph_from_pickle(file_path):
    with open(file_path, 'rb') as f:
        graph = pickle.load(f)
    return graph

# Function to find the degree of separation between Jim Carrey and another actor
def FL_jim5(actor_name):
    # Load the graph
    graph = load_graph_from_pickle('graph.pickle')
    
    # Check if the actor is Jim Carrey
    if actor_name == 'Jim Carrey':
        return 0, actor_name, None
    
    # Initialize the queue for BFS
    queue = deque([(0, 'Jim Carrey', None)])  # (Degree of separation, actor, movie)
    visited = set()
    
    while queue:
        degree, current_actor, movie = queue.popleft()
        visited.add(current_actor)
        
        if current_actor == actor_name:
            if degree == 1:
                return degree, actor_name, movie
            else:
                path = [movie]
                while current_actor != 'Jim Carrey':
                    if current_actor not in graph:
                        return float('inf'), actor_name, None  # No connection found
                    current_actor, movie = graph[current_actor][0], graph[current_actor][1] if len(graph[current_actor]) > 1 else None
                    path.append(movie)
                return degree, actor_name, path[::-1]
        
        if current_actor in graph:
            for neighbor in graph[current_actor]:
                if neighbor not in visited:
                    queue.append((degree + 1, neighbor, graph[neighbor][1] if len(graph[neighbor]) > 1 else None))
    
    return float('inf'), actor_name, None  # No connection found


# Example usage
actor_name = 'Jeff Daniels'
degree, actor, info = FL_jim5(actor_name)

if degree == 0:
    print(f"The degree of separation between Jim Carrey and {actor} is {degree}.")
elif degree == 1:
    print(f"The degree of separation between Jim Carrey and {actor} is {degree}.")
    print(f"{actor} has starred with Jim Carrey in the movie {info}.")
else:
    print(f"The degree of separation between Jim Carrey and {actor} is {degree}.")
    print(f"Chain of movies: {' -> '.join(info)}")
