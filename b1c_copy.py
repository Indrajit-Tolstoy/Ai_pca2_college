from collections import deque

my_graph = {
    'A':['B','C'],
    'B':['D'],
    'C':['E'],
    'D':[],
    'E':[]
}

def unified_search(graph, start, target, method='bfs'):
    # Queue stores the entire path, not just the node
    agenda = deque([[start]]) 
    visited = {start}
    
    while agenda:
        # distinct logic: popleft for BFS, pop for DFS
        path = agenda.popleft() if method == 'bfs' else agenda.pop()
        current = path[-1]
        
        if current == target:
            return path
            
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                agenda.append(path + [neighbor])
    return None

# Usage:
bfs_path = unified_search(my_graph, 'A', 'C', method='bfs')
print(bfs_path)
dfs_path = unified_search(my_graph, 'A', 'C', method='dfs')
print(dfs_path)