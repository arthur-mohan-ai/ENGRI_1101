import itertools
import networkx as nx
import matplotlib.pyplot as plt

def tsp_bruteforce(dist, start):
    n = len(dist)
    other = [v for v in range(n) if v != start]
    best_cost = float('Inf')
    best_tour = None

    for perm in itertools.permutations(other):
        tour = [start] + list(perm) + [start]
        cost = 0
        ok = True
        for i in range(len(tour) - 1):
            w = dist[tour[i]][tour[i + 1]]
            if w == 0:               # missing edge -> this tour is invalid
                ok = False
                break
            cost += w
        if ok and cost < best_cost:
            best_cost = cost
            best_tour = tour
    return best_cost, best_tour

def visualize_tour(dist, tour, title=""):
    G = nx.Graph()
    for u, row in enumerate(dist):
        for v, w in enumerate(row):
            if w > 0 and u < v:
                G.add_edge(u, v, weight=w)
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000)
    if tour:
        tour_edges = [(tour[i], tour[i+1]) for i in range(len(tour)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=tour_edges,
                               edge_color='red', width=3)
    if title:
        plt.title(title)
    plt.show()

def interactive_tsp(dist, start):
    n = len(dist)
    other = [v for v in range(n) if v != start]
    best_cost = float('Inf')
    best_tour = None

    for perm in itertools.permutations(other):
        tour = [start] + list(perm) + [start]
        cost = 0
        ok = True
        for i in range(len(tour) - 1):
            w = dist[tour[i]][tour[i + 1]]
            if w == 0:
                ok = False
                break
            cost += w
        if ok and cost < best_cost:
            best_cost = cost
            best_tour = tour
        visualize_tour(dist, tour,
                       title=f"tour {tour}  cost={cost}   best={best_cost}")
        input("Press Enter to continue to the next candidate tour...")

    visualize_tour(dist, best_tour, title=f"BEST tour {best_tour}  cost={best_cost}")
    return best_cost, best_tour

dist = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 15],
    [25, 30, 20, 15, 0],
]
start = 0

best_cost, best_tour = interactive_tsp(dist, start)
print("Best tour:", best_tour)
print("Best cost:", best_cost)
