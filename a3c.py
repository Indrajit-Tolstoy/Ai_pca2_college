graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['E']
}

def find_path(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path

    for node in graph[start]:
        if node not in path:
            p = find_path(graph, node, end, path)
            if p:
                return p

    return None

print(find_path(graph, 'A', 'D')) 