📘 Romanian Map Search System – README
A complete AI search project implementing DFS (unweighted), Weighted DFS (exhaustive), and Dijkstra’s Algorithm, combined with graph visualization using fixed coordinates from JSON files.
This system loads all data (graph & coordinates) dynamically so you never rewrite anything.
The project automatically:
✔ Loads Romania map edges + distances from map_graph.json
✔ Loads fixed city coordinates from map_coords.json
✔ Runs DFS (unweighted)
✔ Runs DFS Weighted Shortest Path (exhaustive)
✔ Runs Dijkstra (fast, optimal)
✔ Produces a comparison table
✔ Generates a graphical visualization comparing paths
✔ Saves the figure to comparison_paths.png

📁 Project Structure
PROJECT/
│
├── main.py
├── map_data.py
├── algorithms_dfs.py
├── algorithms_weighted.py
├── map_plotter.py
│
├── map_graph.json
├── map_coords.json
│
└── comparison_paths.png   (generated after running main.py)


📌 1. What the System Does
This project demonstrates multiple AI search algorithms on the Romania Road Map Problem, a classical problem in Artificial Intelligence.
It performs:
✔ A. DFS Search (Unweighted)


Uses adjacency list only


Ignores road distances


Finds a path from Start → Goal


Not guaranteed to be optimal


Visualized in red dashed lines



✔ B. DFS Shortest Path (Weighted Exhaustive Search)


Uses all road distances


Explores ALL possible paths via DFS


Keeps the minimum-cost path


Computationally expensive (exponential)


Output included in comparison table (not plotted by default)



✔ C. Dijkstra’s Algorithm (Weighted Optimal Shortest Path)


Finds guaranteed shortest route


Uses priority queue


Efficient, scalable


Visualized in blue solid lines



📌 2. What the Program Outputs
When you run:
python3 main.py

The program:
✔ Prompts for:


Start city


Goal city


✔ Runs all search algorithms
✔ Displays a table comparing the algorithms
Example:
AlgorithmPathTotal Distance (km)DFS (unweighted)Arad → Sibiu → Rimnicu Vilcea → …N/ADFS Weighted (exhaustive)Arad → Sibiu → Fagaras → Bucharest450Dijkstra (weighted)Arad → Sibiu → Fagaras → Bucharest450
✔ Shows a graphical map


DFS path: Red dashed


Dijkstra path: Blue solid


Nodes placed using coordinates from map_coords.json


Saved automatically as:


comparison_paths.png


📌 3. JSON Files
map_graph.json
Contains all cities with weighted distances.
This JSON acts as the single source of truth for the graph structure.
Example:
"Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140}


map_coords.json
Contains fixed coordinates for each city for stable plotting.
Example:
"Arad": [0.12, 0.70]

Coordinates are normalized (0.0 → 1.0).

📌 4. Module Breakdown
📄 main.py


Main entry point


Always runs DFS, Weighted DFS, Dijkstra


Prints comparison table


Calls map plotter to draw both paths



📄 map_data.py
Provides:


load_weighted_graph()


weighted_to_unweighted()


load_coords()


This ensures no duplication across files.

📄 algorithms_dfs.py


Classical unweighted recursive DFS


Returns the first path found



📄 algorithms_weighted.py
Contains two algorithms:


dfs_shortest(): exhaustive weighted DFS


dijkstra(): optimal shortest path



📄 map_plotter.py


Builds graph using NetworkX


Uses coordinates from JSON


Draws:


DFS path (red, dashed)


Dijkstra path (blue, solid)




Saves image to comparison_paths.png



📌 5. Installation
Install required packages:
pip install networkx matplotlib tabulate


📌 6. Running the Project
Run:
python3 main.py

Enter:
Enter start city: Arad
Enter goal city: Bucharest

You will receive:


Comparison table printed to terminal


Graphical visualization showing both paths


Saved image: comparison_paths.png



📌 7. Notes & Customization
✔ Modify coordinates
Edit map_coords.json to reposition cities.
✔ Modify graph weights
Edit map_graph.json for new distances.
✔ Disable Weighted DFS (optional)
If runtime becomes slow:
# comment out dfs_shortest in main.py


📌 8. Future Enhancements (Optional)
I can add any of the following:


BFS support


Uniform Cost Search (UCS)


A* Search with heuristics


GUI interface (Tkinter / PyQt)


Path expansion animation


Export results to CSV/PDF


Web UI via Flask/FastAPI


Just tell me what you want next.

🎉 README Complete
If you want, I can generate:
📘 PDF version
📘 GitHub-Friendly version
📘 Screenshots for documentation
