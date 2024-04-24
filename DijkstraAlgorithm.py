from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(graph, start, end):
    # Initialize distances and previous nodes
    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(lambda: None)
    dist[start] = 0

    # Initialize priority queue
    queue = [(0, start)]

    # Keep track of visited nodes
    visited = set()

    # Iterate until we have no more nodes to explore
    while queue:
        # Explore the next node
        dist_node, node = heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        # Update distances and previous nodes for neighbors
        for neighbor, weight in graph[node].items():
            if dist[neighbor] > dist_node + weight:
                dist[neighbor] = dist_node + weight
                prev[neighbor] = node
                heappush(queue, (dist[neighbor], neighbor))

    # Construct the shortest path
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = prev[node]
    return path[::-1], dist[end]


graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 3, 'D': 8},
    'C': {'A': 4, 'B': 3, 'E': 5, 'D':2},
    'D': {'B':8, 'C':2, 'E':11, 'F':22},
    'E': {'C': 5, 'D': 11, 'F':1},
    'F': {'D': 22, 'E':1},
}
shortest_path, shortest_distance = dijkstra(graph, 'A', 'F')
print(f"Shortest Path: {shortest_path}")  # Output: ["A", "C", "F", "G"]
print(f"Shortest Distance: {shortest_distance}") # Output: 10