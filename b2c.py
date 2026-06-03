graph = {
    'A':['B','C'],
    'B':['D'],
    'C':['E'],
    'D':[],
    'E':[]
}

# DLS
def dls(node, goal, limit):
    if node == goal:
        return True

    if limit <= 0:
        return False

    for child in graph[node]:
        if dls(child, goal, limit-1):
            return True
    return False

print(dls('A', 'E', 2))

# ID
def ids(start, goal, max_depth):
    for depth in range(max_depth+1):
        if dls(start, goal, depth):
            return depth

print("Found at depth:", ids('A', 'E', 5))