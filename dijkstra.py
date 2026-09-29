import networkx as nx
import matplotlib.pyplot as plt

def get_path(parent, source, sink):
    path = []
    v = sink
    while v != -1:
        path.insert(0, v)
        if v == source:
            break
        v = parent[v]
    return path

def dijkstra(graph, source):
    n = len(graph)
    dist = [float('Inf')] * n        # shortest distance to each node so far
    visited = [False] * n            # node is "settled"
    parent = [-1] * n                # which node we came from
    dist[source] = 0

    for _ in range(n):
        # pick the unvisited node with the smallest distance
        u = min((v for v in range(n) if not visited[v]), key=lambda v: dist[v])
        visited[u] = True
        for v, weight in enumerate(graph[u]):
            if weight > 0 and not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
    return dist, parent

def visualize_graph(graph, highlight_nodes=None, highlight_edges=None, title=""):
    G = nx.Graph()
    for u, row in enumerate(graph):
        for v, weight in enumerate(row):
            if weight > 0 and u < v:
                G.add_edge(u, v, weight=weight)
    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    if highlight_nodes:
        nx.draw_networkx_nodes(G, pos, nodelist=highlight_nodes,
                               node_color='yellow', node_size=2200)
    if highlight_edges:
        nx.draw_networkx_edges(G, pos, edgelist=highlight_edges,
                               edge_color='red', width=3)
    if title:
        plt.title(title)
    plt.show()

def interactive_dijkstra(graph, source, sink):
    n = len(graph)
    dist = [float('Inf')] * n
    visited = [False] * n
    parent = [-1] * n
    dist[source] = 0

    for _ in range(n):
        u = min((v for v in range(n) if not visited[v]), key=lambda v: dist[v])
        visited[u] = True
        updated_edges = []
        for v, weight in enumerate(graph[u]):
            if weight > 0 and not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                updated_edges.append((u, v))
        visualize_graph(graph, highlight_nodes=[u],
                        highlight_edges=updated_edges,
                        title=f"settling node {u}, dist[u]={dist[u]}")
        input("Press Enter to continue to the next iteration...")

    path = get_path(parent, source, sink)
    visualize_graph(graph,
                    highlight_nodes=path,
                    highlight_edges=[(path[i], path[i+1]) for i in range(len(path)-1)],
                    title=f"shortest path {source} -> {sink}: {dist[sink]}")
    return dist, parent, path

graph = [
    [0, 4, 2, 0, 0, 0],
    [4, 0, 1, 5, 0, 0],
    [2, 1, 0, 8, 10, 0],
    [0, 5, 8, 0, 2, 6],
    [0, 0, 10, 2, 0, 3],
    [0, 0, 0, 6, 3, 0],
]
source = 0
sink = 5

dist, parent, path = interactive_dijkstra(graph, source, sink)
print("Shortest distances from", source, ":", dist)
print("Shortest path", source, "->", sink, ":", path, "length", dist[sink])
