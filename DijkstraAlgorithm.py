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
 