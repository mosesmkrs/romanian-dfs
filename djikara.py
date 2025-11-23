# romania_dijkstra.py
# Dijkstra's algorithm for shortest path in weighted Romanian map

import heapq

romania_weighted_map = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

def dijkstra(graph, start, goal):
    pq = []  # priority queue of (distance, city, path)
    heapq.heappush(pq, (0, start, [start]))
    visited = set()

    while pq:
        dist, current, path = heapq.heappop(pq)

        if current == goal:
            return path, dist

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(pq, (dist + cost, neighbor, path + [neighbor]))

    return None, float('inf')


def main():
    print("Available Cities:")
    for city in romania_weighted_map.keys():
        print("-", city)
    print("\n")

    start_city = input("Enter start city: ").strip()
    goal_city = input("Enter goal city: ").strip()

    if start_city not in romania_weighted_map or goal_city not in romania_weighted_map:
        print("Invalid city entered.")
        return

    path, distance = dijkstra(romania_weighted_map, start_city, goal_city)

    if path:
        print("\nShortest path (Dijkstra) from", start_city, "to", goal_city, ":")
        print(" -> ".join(path))
        print("Total distance:", distance, "km")
    else:
        print("No path found.")


if __name__ == "__main__":
    main()
