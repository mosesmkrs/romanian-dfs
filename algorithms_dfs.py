# algorithms_dfs.py
# Standard recursive DFS returning one path (unweighted)

from typing import Dict, List, Optional, Set


def dfs(graph: Dict[str, List[str]], start: str, goal: str,
        visited: Optional[Set[str]] = None, path: Optional[List[str]] = None) -> Optional[List[str]]:
    """
    Recursive DFS. Returns one path (list of nodes) or None if not found.
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == goal:
        return list(path)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path)
            if result is not None:
                return result

    path.pop()
    return None

