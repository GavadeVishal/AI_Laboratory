from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    bfs_order = []
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            bfs_order.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return bfs_order
graph = {
    'A': ['D'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'C', 'F'],
    'D': ['B','A'],
    'E': ['B', 'F'],
    'F': ['C']
}
start_node = 'A'
bfs_result = bfs(graph, start_node)
print("BFS Order:", bfs_result)
