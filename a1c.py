from collections import defaultdict

def build_adjacency_list(edges, is_directed=False):
    """
    Builds an adjacency list representation from a list of edges.
    """
    # defaultdict(list) prevents KeyErrors and avoids messy if/else checks
    graph = defaultdict(list)
    
    for u, v in edges:
        graph[u].append(v)  # Always add the forward edge
        
        if not is_directed:
            graph[v].append(u)  # Add the reverse edge for undirected graphs
            
    # Convert back to a standard dictionary for cleaner printing
    return dict(graph)

edge_list = [('A', 'B'), ('B', 'C'), ('A', 'C')]

print("--- Directed Graph ---")

directed_graph = build_adjacency_list(edge_list, is_directed=True)
for node, neighbors in directed_graph.items():
    print(f"Node {node} points to: {neighbors}")

print("\n--- Undirected Graph ---")

undirected_graph = build_adjacency_list(edge_list, is_directed=False)
for node, neighbors in undirected_graph.items():
    print(f"Node {node} connects to: {neighbors}")