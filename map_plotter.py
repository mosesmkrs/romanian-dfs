# map_plotter.py
# Draws the map using provided coordinates and highlights paths.
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Optional, Dict, Tuple
from map_data import load_weighted_graph, load_coords, weighted_to_unweighted
from pathlib import Path

OUT_DIR = Path(__file__).parent
OUT_FILE = OUT_DIR / "comparison_paths.png"


def build_graph(weighted: Dict[str, Dict[str, int]]) -> nx.Graph:
    G = nx.Graph()
    # Add weighted edges
    for a, nbrs in weighted.items():
        for b, w in nbrs.items():
            # add edge once (Graph will handle duplicates)
            G.add_edge(a, b, weight=w)
    return G


def draw_map_and_paths(unweighted_graph: Dict[str, List[str]],
                       coords: Dict[str, Tuple[float, float]],
                       dfs_path: Optional[List[str]] = None,
                       weighted_path: Optional[List[str]] = None,
                       title: str = "Romania Map - Comparison"):
    """
    Draw both paths on the same plot:
      - dfs_path: red, dashed
      - weighted_path: blue, solid
    Saves to 'comparison_paths.png' in project root and displays plot.
    """
    # Build NetworkX graph from adjacency
    G = nx.Graph()
    for node, nbrs in unweighted_graph.items():
        for nbr in nbrs:
            G.add_edge(node, nbr)

    # Use provided coordinates
    pos = coords

    plt.figure(figsize=(14, 9))

    # draw base graph (nodes & edges)
    nx.draw_networkx_edges(G, pos, alpha=0.4)
    nx.draw_networkx_nodes(G, pos, node_size=800, node_color="lightgray", edgecolors="black")
    nx.draw_networkx_labels(G, pos, font_size=9)

    # draw dfs path
    if dfs_path and len(dfs_path) > 1:
        dfs_edges = list(zip(dfs_path, dfs_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, width=4, style="dashed", edge_color="red", label="DFS (unweighted)")
        nx.draw_networkx_nodes(G, pos, nodelist=dfs_path, node_color="red", node_size=900)

    # draw weighted path
    if weighted_path and len(weighted_path) > 1:
        w_edges = list(zip(weighted_path, weighted_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=w_edges, width=4, style="solid", edge_color="blue", label="Weighted shortest")
        nx.draw_networkx_nodes(G, pos, nodelist=weighted_path, node_color="blue", node_size=900)

    plt.title(title)
    # legend
    plt.legend()
    plt.axis("off")

    # save and show
    plt.tight_layout()
    plt.savefig(OUT_FILE, dpi=150)
    print(f"Saved comparison figure to: {OUT_FILE}")
    plt.show()
