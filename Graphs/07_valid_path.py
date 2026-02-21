"""
VALID PATH PROBLEMS
===================

WHEN TO USE:
- Check if path exists between two nodes
- Find path with constraints
- Minimum cost path

KEY INSIGHT: Use BFS for shortest, DFS for existence.
Track visited to avoid revisiting.

TIME: O(V + E)  |  SPACE: O(V)
"""

from collections import defaultdict, deque
import heapq

# ============================================
# PATTERN 1: Valid Path in Graph
# ============================================
def valid_path(n, edges, source, destination):
    """Check if path exists from source to destination."""
    if source == destination:
        return True

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set([source])
    stack = [source]

    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor == destination:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return False


# ============================================
# PATTERN 2: Path with Minimum Effort (Dijkstra variant)
# ============================================
def minimum_effort_path(heights):
    """
    Find path from top-left to bottom-right.
    Effort = max absolute difference along path. Minimize this.
    """
    rows, cols = len(heights), len(heights[0])

    # Dijkstra: (effort, row, col)
    heap = [(0, 0, 0)]
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = 0

    while heap:
        effort, r, c = heapq.heappop(heap)

        if r == rows - 1 and c == cols - 1:
            return effort

        if effort > dist[r][c]:
            continue

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                if new_effort < dist[nr][nc]:
                    dist[nr][nc] = new_effort
                    heapq.heappush(heap, (new_effort, nr, nc))

    return 0


# ============================================
# PATTERN 3: Path with Maximum Probability
# ============================================
def max_probability(n, edges, probs, start, end):
    """Find path with maximum success probability."""
    graph = defaultdict(list)
    for (u, v), prob in zip(edges, probs):
        graph[u].append((v, prob))
        graph[v].append((u, prob))

    # Max-heap (negate prob for max behavior)
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
# PATTERN 4: Shortest Path with Alternating Colors
# ============================================
def shortest_alternating_paths(n, red_edges, blue_edges):
    """
    Find shortest path using alternating colors.
    Return distances from 0 to each node.
    """
    graph = defaultdict(lambda: defaultdict(list))
    for u, v in red_edges:
        graph[u]['red'].append(v)
    for u, v in blue_edges:
        graph[u]['blue'].append(v)

    result = [-1] * n
    result[0] = 0

    # BFS: (node, last_color)
    queue = deque([(0, 'red', 0), (0, 'blue', 0)])
    visited = {(0, 'red'), (0, 'blue')}

    while queue:
        node, last_color, dist = queue.popleft()

        next_color = 'blue' if last_color == 'red' else 'red'
        for neighbor in graph[node][next_color]:
            if (neighbor, next_color) not in visited:
                visited.add((neighbor, next_color))
                if result[neighbor] == -1:
                    result[neighbor] = dist + 1
                queue.append((neighbor, next_color, dist + 1))

    return result


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 1971. Find if Path Exists in Graph

Medium:
- 1631. Path With Minimum Effort
- 1514. Path with Maximum Probability
- 1129. Shortest Path with Alternating Colors
- 1334. Find the City With Smallest Number of Neighbors
"""
