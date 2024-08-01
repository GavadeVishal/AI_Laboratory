from collections import deque
graph = {
    'Pathare': ['Kolpewadi', 'Pohegaon'],
    'Kolpewadi': ['Pathare', 'Yeola' , 'Kopargaon'],
    'Kopargaon': ['Kolpewadi', 'Shirdi' , 'Yeola'],
    'Yeola': ['Kolpewadi'],
    'Shirdi': ['Kopargaon', 'Pohegaon'],
    'Pohegaon': ['Shirdi']
}
def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])
    if start == goal:
        return [start]
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal:
                    return new_path
            visited.add(node)
    return None
start_node = 'Pathare'
goal_node = 'Kopargaon'
path = bfs_shortest_path(graph, start_node, goal_node)

if path:
    print(f"The shortest path from {start_node} to {goal_node} is: {' -> '.join(path)}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
