# Visualizations of algos of Cornell ENGRI 1101 Eng Ops: Data and Decisions

Taught by the aloha shirt lover prof. Frans Schalekamp.

## What's inside

| File | Algorithm | What it shows |
|------|-----------|---------------|
| `ford_fulkerson.py` | Ford–Fulkerson (max flow / min cut) | Residual graph + the augmenting path highlighted in red each round |
| `dijkstra.py` | Dijkstra (single-source shortest path) | Each node being "settled", then the final shortest path in red |
| `tsp.py` | Traveling Salesman (exact brute force) | Every candidate tour, tracking the best one found so far |
| `mst.py` | Minimum Spanning Tree (Prim's) | The tree growing edge by edge |

## Notes

- `tsp.py` is exact but **O(n!)** — brute force over every tour. Keep the graph small (≤ 6 cities) or you'll be pressing Enter for a long time.
- All four files share the same style: an algorithm function, a `visualize_*` function, an interactive driver, and a `print(...)` result at the end.
