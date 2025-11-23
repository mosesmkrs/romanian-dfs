# romania_dfs.py
# Depth-First Search implementation on the Romanian Map with user input

def build_romania_map():
    """
    Returns the standard Romanian map used in AI textbooks.
    """
    return {
        'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
        'Zerind': ['Arad', 'Oradea'],
        'Oradea': ['Zerind', 'Sibiu'],
        'Timisoara': ['Arad', 'Lugoj'],
        'Lugoj': ['Timisoara', 'Mehadia'],
        'Mehadia': ['Lugoj', 'Drobeta'],
        'Drobeta': ['Mehadia', 'Craiova'],
        'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
        'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
        'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
        'Fagaras': ['Sibiu', 'Bucharest'],
        'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
        'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
        'Giurgiu': ['Bucharest'],
        'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
        'Hirsova': ['Urziceni', 'Eforie'],
        'Eforie': ['Hirsova'],
        'Vaslui': ['Urziceni', 'Iasi'],
        'Iasi': ['Vaslui', 'Neamt'],
        'Neamt': ['Iasi']
    }


def dfs(graph, start, goal, visited=None, path=None):
    """
    Recursive Depth-First Search that returns one path from start to goal.
    This does not guarantee the shortest or best path.
    """
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path)
            if result is not None:
                return result

    # backtrack
    path.pop()
    return None


def main():
    graph = build_romania_map()
    
    print("Available Cities:")
    for city in graph.keys():
        print("-", city)
    print("\n")

    start_city = input("Enter start city: ").strip()
    goal_city = input("Enter goal city: ").strip()

    # Input validation
    if start_city not in graph:
        print(f"Error: {start_city} is not a valid city.")
        return
    if goal_city not in graph:
        print(f"Error: {goal_city} is not a valid city.")
        return

    result = dfs(graph, start_city, goal_city)

    if result:
        print("\nDFS Path from", start_city, "to", goal_city, ":")
        print(" -> ".join(result))
    else:
        print("No path found.")


if __name__ == "__main__":
    main()
