"""
DIJKSTRA'S ALGORITHM
====================

WHEN TO USE:
- Shortest path in weighted graph
- Non-negative edge weights only
- Single source shortest path

KEY INSIGHT: Greedily select minimum distance node.
Use min-heap for efficiency.

TIME: O((V + E) log V)  |  SPACE: O(V)
"""

import heapq
from collections import defaultdict

# ============================================
# PATTERN 1: Basic Dijkstra
# ============================================
def dijkstra(graph, start, n):
    """
    Find shortest distances from start to all nodes.
    graph[u] = [(v, weight), ...]
    """
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]  # (distance, node)

    while heap:
        d, u = heapq.heappop(heap)

        if d > dist[u]:
            continue  # Skip outdated entry

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(heap, (dist[v], v))

    return dist


# ============================================
# PATTERN 2: Network Delay Time
# ============================================
def network_delay_time(times, n, k):
    """
    Time for signal to reach all nodes from node k.
    times[i] = [u, v, w] means edge from u to v with weight w.
    """
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[k] = 0
    heap = [(0, k)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))

    max_dist = max(dist.values())
    return max_dist if max_dist < float('inf') else -1


# ============================================
# PATTERN 3: Cheapest Flights Within K Stops
# ============================================
def find_cheapest_price(n, flights, src, dst, k):
    """Find cheapest price with at most k stops."""
    graph = defaultdict(list)
    for u, v, price in flights:
        graph[u].append((v, price))

    # (price, city, stops)
    heap = [(0, src, 0)]
    # best[city][stops] = min price to reach city with exactly stops
    best = defaultdict(lambda: defaultdict(lambda: float('inf')))

    while heap:
        price, city, stops = heapq.heappop(heap)

        if city == dst:
            return price

        if stops > k:
            continue

        if price >= best[city][stops]:
            continue
        best[city][stops] = price

        for next_city, next_price in graph[city]:
            heapq.heappush(heap, (price + next_price, next_city, stops + 1))

    return -1


# ============================================
# PATTERN 4: Path with Maximum Probability
# ============================================
def max_probability(n, edges, probs, start, end):
    """Find path with maximum success probability."""
    graph = defaultdict(list)
    for (u, v), p in zip(edges, probs):
        graph[u].append((v, p))
        graph[v].append((u, p))

    # Max-heap (negate for max behavior)
    max_prob = [0.0] * n
    max_prob[start] = 1.0
    heap = [(-1.0, start)]

    while heap:
        neg_prob, node = heapq.heappop(heap)
        prob = -neg_prob

        if node == end:
            return prob

        if prob < max_prob[node]:
            continue

        for neighbor, edge_prob in graph[node]:
            new_prob = prob * edge_prob
            if new_prob > max_prob[neighbor]:
                max_prob[neighbor] = new_prob
                heapq.heappush(heap, (-new_prob, neighbor))

    return 0.0


# ============================================
# PATTERN 5: Shortest Path with Obstacles
# ============================================
def shortest_path(grid, k):
    """
    Shortest path in grid, can eliminate at most k obstacles.
    State: (row, col, obstacles_remaining)
    """
    rows, cols = len(grid), len(grid[0])
    if rows == 1 and cols == 1:
        return 0

    # (steps, row, col, obstacles_left)
    heap = [(0, 0, 0, k)]
    visited = {(0, 0, k)}

    while heap:
        steps, r, c, obs = heapq.heappop(heap)

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_obs = obs - grid[nr][nc]
                if new_obs >= 0 and (nr, nc, new_obs) not in visited:
                    if nr == rows - 1 and nc == cols - 1:
                        return steps + 1
                    visited.add((nr, nc, new_obs))
                    heapq.heappush(heap, (steps + 1, nr, nc, new_obs))

    return -1


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 743. Network Delay Time
- 1514. Path with Maximum Probability
- 1631. Path With Minimum Effort
- 787. Cheapest Flights Within K Stops

Hard:
- 1293. Shortest Path in a Grid with Obstacles Elimination
- 778. Swim in Rising Water
"""
