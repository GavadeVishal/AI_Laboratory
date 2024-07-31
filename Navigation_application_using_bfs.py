from collections import deque

# Define the graph as an adjacency list
graph = {
    'Pathare': ['Pohegaon', 'Kolpewadi'],
    'Shirdi': ['Kopargaon'],
    'Kopargaon': ['Kolpewadi','Shirdi','Yeola'],
    'Kolpewadi': ['Kopargaon'],
    'Pohegaon': ['Pathare', 'Kolpewadi','Kopargoan'],
    'Yeola': ['Kopargaon', 'Kolpewadi'],
}

def bfs_shortest_path(graph, start, goal):
    # Keep track of visited nodes
    visited = set()
    # Queue for BFS
    queue = deque([[start]])
    
    # If the start is the goal, return immediately
    if start == goal:
        return [start]
    
    # Loop until there are nodes still to be checked
    while queue:
        # Pop the first path from the queue
        path = queue.popleft()
        # Get the last node from the path
        node = path[-1]
        
        if node not in visited:
            # Get the neighbors of the node
            neighbors = graph[node]
            # Go through all neighbor nodes, construct a new path, and add it to the queue
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
                # Return the path if the neighbor is the goal
                if neighbor == goal:
                    return new_path
            
            # Mark the node as visited
            visited.add(node)
    
    # If there's no path between the 2 nodes
    return None

# Example usage
start_node = 'Pathare'
goal_node = 'Kopargaon'
path = bfs_shortest_path(graph, start_node, goal_node)

if path:
    print(f"The shortest path from {start_node} to {goal_node} is: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
