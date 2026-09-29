import networkx as nx
import matplotlib.pyplot as plt
def bfs(residual_graph, source, sink, parent):
    visited = [False] * len(residual_graph)
    queue = [source]
    visited[source] = True

    while queue:
        u = queue.pop(0)
        for v, capacity in enumerate(residual_graph[u]):
            if not visited[v] and capacity > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False
def ford_fulkerson(graph, source, sink):#one iteration of the Ford-Fulkerson algorithm
    residual_graph = [row[:] for row in graph] 
    parent = [-1] * len(graph)
    max_flow = 0
    bfs(residual_graph, source, sink, parent)

    while bfs(residual_graph, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow
def visualize_residual_graph(residual_graph):
    G = nx.DiGraph()
    for u, row in enumerate(residual_graph):
        for v, capacity in enumerate(row):
            if capacity > 0:
                G.add_edge(u, v, capacity=capacity)
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()
def visualize_path(residual_graph, path):
    G = nx.DiGraph()
    for u, row in enumerate(residual_graph):
        for v, capacity in enumerate(row):
            if capacity > 0:
                G.add_edge(u, v, capacity=capacity)
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    if path:
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    plt.show()
def interactive_ford_fulkerson(graph, source, sink):
    residual_graph = [row[:] for row in graph]
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(residual_graph, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        path = []
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            path.insert(0, s)
            s = parent[s]
        path.insert(0, source)

        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

        visualize_residual_graph(residual_graph)
        visualize_path(residual_graph, path)
        input("Press Enter to continue to the next iteration...")

    return max_flow
graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]
source = 0
sink = 5
max_flow = interactive_ford_fulkerson(graph, source, sink)
print("Max Flow:", max_flow)