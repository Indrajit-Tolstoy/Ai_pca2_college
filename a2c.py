graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 2},
    'C': {'D': 4, 'E': 1}
}

u = input("Enter first vertex: ")
v = input("Enter second vertex: ")

if v in graph.get(u, {}):
    print("Weight =", graph[u][v])
else:
    print("No edge exists")