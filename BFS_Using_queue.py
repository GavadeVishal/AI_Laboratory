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
    '1': ['2', '4'],
    '2': ['3'],
    '3': [ ],
    '4': ['2','5'],
    '5': ['2', '3'],
}
start_node = '1'
bfs_result = bfs(graph, start_node)
print("BFS Order:", bfs_result)
