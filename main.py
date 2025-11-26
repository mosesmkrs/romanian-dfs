# main.py
# Runs DFS (unweighted) and weighted shortest path (Dijkstra),
# prints a comparison table, and draws a combined map with both paths.

from map_data import load_weighted_graph, weighted_to_unweighted, load_coords
from algorithms_dfs import dfs
from algorithms_weighted import dfs_shortest, dijkstra
from map_plotter import draw_map_and_paths
from tabulate import tabulate  # pip install tabulate
import sys

def compare_and_display(start: str, goal: str):
    # load data
    weighted = load_weighted_graph()
    unweighted = weighted_to_unweighted(weighted)
    coords = load_coords()

    # Validate
    if start not in unweighted or goal not in unweighted:
        print("Invalid start/goal. Please use a city from the map.")
        return

    # 1) DFS (unweighted)
    dfs_path = dfs(unweighted, start, goal)

    # 2) Weighted Exhaustive DFS (optional - may be slow)
    dfs_weighted_result = dfs_shortest(weighted, start, goal)
    dfs_weighted_path = dfs_weighted_result.get("path")
    dfs_weighted_cost = dfs_weighted_result.get("cost", float("inf"))

    # 3) Dijkstra (recommended)
    dijkstra_path, dijkstra_cost = dijkstra(weighted, start, goal)

    # Prepare comparison table
    table = [
        ["Algorithm", "Path", "Total Distance (km)"],
        ["DFS (unweighted)", " -> ".join(dfs_path) if dfs_path else "No path", "N/A"],
        ["DFS-weighted (exhaustive)", " -> ".join(dfs_weighted_path) if dfs_weighted_path else "No path", f"{dfs_weighted_cost:.0f}" if dfs_weighted_path else "N/A"],
        ["Dijkstra (weighted)", " -> ".join(dijkstra_path) if dijkstra_path else "No path", f"{dijkstra_cost:.0f}" if dijkstra_path else "N/A"]
    ]

    # print table nicely using tabulate (fall back to simple print if tabulate not installed)
    try:
        print("\nComparison Results:\n")
        print(tabulate(table[1:], headers=table[0], tablefmt="github"))
    except Exception:
        for row in table:
            print("\t".join(row))

    # For plotting: show DFS (unweighted path) and Dijkstra path (best weighted).
    draw_map_and_paths(unweighted, coords, dfs_path=dfs_path, weighted_path=dijkstra_path)


def main():
    print("=== Romania Map — Compare DFS and Shortest Path ===\n")
        # Print all cities (so the user knows the valid options)
    weighted = load_weighted_graph()
    print("Available Cities:")
    for city in sorted(weighted.keys()):
        print(" -", city)
    print()

    print("This program will run both algorithms and show a comparison.\n")
    start = input("Enter start city: ").strip()
    goal = input("Enter goal city: ").strip()

    compare_and_display(start, goal)


if __name__ == "__main__":
    main()
