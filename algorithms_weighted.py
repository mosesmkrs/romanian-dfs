# algorithms_weighted.py
# Weighted DFS-exhaustive (slow) + Dijkstra (recommended)

from typing import Dict, List, Optional, Tuple
import heapq


def dfs_shortest(weighted_graph: Dict[str, Dict[str, int]],
                 start: str, goal: str,
                 visited=None, path=None, cost=0, best=None):
    """
    Exhaustive DFS on weighted graph that keeps the minimal-cost path found.
    WARNING: exponential time on large graphs. Good as an exercise.
    Returns dict: {'path': [...], 'cost': x}
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []
    if best is None:
        best = {'path': None, 'cost': float('inf')}

    visited.add(start)
    path.append(start)

    if start == goal:
        if cost < best['cost']:
            best['path'] = list(path)
            best['cost'] = cost
    else:
        for nbr, w in weighted_graph.get(start, {}).items():
            if nbr not in visited:
                dfs_shortest(weighted_graph, nbr, goal, visited, path, cost + w, best)

    path.pop()
    visited.remove(start)
    return best


def dijkstra(weighted_graph: Dict[str, Dict[str, int]],
             start: str, goal: str) -> Tuple[Optional[List[str]], float]:
    """
    Standard Dijkstra algorithm returning (path, total_cost).
    """
    pq = []
    heapq.heappush(pq, (0, start, [start]))
    visited = set()

    while pq:
        dist, node, path = heapq.heappop(pq)
        if node == goal:
            return path, dist
        if node in visited:
            continue
        visited.add(node)
        for nbr, w in weighted_graph.get(node, {}).items():
            if nbr not in visited:
                heapq.heappush(pq, (dist + w, nbr, path + [nbr]))

    return None, float('inf')

