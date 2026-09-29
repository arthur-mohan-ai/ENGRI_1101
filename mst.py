import networkx as nx
import matplotlib.pyplot as plt

def prim(graph, source=0):           # Prim's algorithm for Minimum Spanning Tree
    n = len(graph)
    in_mst = [False] * n             # node already added to the tree
    key = [float('Inf')] * n         # cheapest edge cost to reach each node
    parent = [-1] * n                # parent in the spanning tree
    key[source] = 0

    for _ in range(n):
        # pick the node not in the tree that can be reached most cheaply
        u = min((v for v in range(n) if not in_mst[v]), key=lambda v: key[v])
        in_mst[u] = True
        for v, weight in enumerate(graph[u]):
            if weight > 0 and not in_mst[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u

    edges = [(parent[v], v) for v in range(n) if parent[v] != -1]
    total = sum(key)
    return edges, total

def visualize_graph(graph, tree_edges=None, highlight_node=None, title=""):
    G = nx.Graph()
    for u, row in enumerate(graph):
        for v, weight in enumerate(row):
            if weight > 0 and u < v:
                G.add_edge(u, v, weight=weight)
    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    if tree_edges:
        nx.draw_networkx_edges(G, pos, edgelist=tree_edges,
                               edge_color='red', width=3)
    if highlight_node is not None:
        nx.draw_networkx_nodes(G, pos, nodelist=[highlight_node],
                               node_color='yellow', node_size=2200)
    if title:
        plt.title(title)
    plt.show()

def interactive_prim(graph, source=0):
    n = len(graph)
    in_mst = [False] * n
    key = [float('Inf')] * n
    parent = [-1] * n
    key[source] = 0
    edges = []

    for _ in range(n):
        u = min((v for v in range(n) if not in_mst[v]), key=lambda v: key[v])
        in_mst[u] = True
        if parent[u] != -1:
            edges.append((parent[u], u))
        for v, weight in enumerate(graph[u]):
            if weight > 0 and not in_mst[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
        visualize_graph(graph, tree_edges=edges, highlight_node=u,
                        title=f"added node {u}  |  tree so far: {edges}")
        input("Press Enter to continue to the next iteration...")

    total = sum(key)
    visualize_graph(graph, tree_edges=edges, title=f"final MST, total={total}")
    return edges, total

graph = [
    [0, 4, 2, 0, 0, 0],
    [4, 0, 1, 5, 0, 0],
    [2, 1, 0, 8, 10, 0],
    [0, 5, 8, 0, 2, 6],
    [0, 0, 10, 2, 0, 3],
    [0, 0, 0, 6, 3, 0],
]
source = 0

edges, total = interactive_prim(graph, source)
print("MST edges:", edges)
print("MST total weight:", total)
