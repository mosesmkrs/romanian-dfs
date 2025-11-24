# map_data.py
# Loads the graph (weights) and coordinates from JSON files and exposes helpers.

import json
from pathlib import Path
from typing import Dict, List, Tuple

BASE = Path(__file__).parent

GRAPH_FILE = BASE / "map_graph.json"
COORDS_FILE = BASE / "map_coords.json"


def load_weighted_graph() -> Dict[str, Dict[str, int]]:
    with open(GRAPH_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def weighted_to_unweighted(weighted: Dict[str, Dict[str, int]]) -> Dict[str, List[str]]:
    """Convert weighted adjacency dict to simple adjacency lists (undirected)."""
    g = {}
    for a, nbrs in weighted.items():
        g.setdefault(a, [])
        for b in nbrs.keys():
            g.setdefault(b, [])
            if b not in g[a]:
                g[a].append(b)
            if a not in g[b]:
                g[b].append(a)
    return g


def load_coords() -> Dict[str, Tuple[float, float]]:
    with open(COORDS_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)
    # convert lists to tuples
    return {k: tuple(v) for k, v in raw.items()}


if __name__ == "__main__":
    # quick test
    wg = load_weighted_graph()
    ug = weighted_to_unweighted(wg)
    coords = load_coords()
    print("Weighted nodes:", len(wg))
    print("Unweighted nodes:", len(ug))
    print("Coords loaded:", len(coords))

