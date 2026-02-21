"""
MINIMUM SPANNING TREE (Kruskal's & Prim's)
==========================================

WHEN TO USE:
- Connect all nodes with minimum total edge weight
- Network design (minimum cable/road)
- Clustering

KEY INSIGHT:
- Kruskal's: Sort edges, add smallest that doesn't create cycle
- Prim's: Grow tree from any node, always add minimum edge

TIME: O(E log E) or O(E log V)  |  SPACE: O(V)
"""

import heapq
from collections import defaultdict

# ============================================
# Union-Find for Kruskal's
# ============================================
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


# ============================================
# PATTERN 1: Kruskal's Algorithm
# ============================================
def kruskal(n, edges):
    """
    Find MST weight using Kruskal's.
    edges = [(u, v, weight), ...]
    """
    edges.sort(key=lambda x: x[2])  # Sort by weight
    uf = UnionFind(n)
    mst_weight = 0
    edges_used = 0

    for u, v, weight in edges:
        if uf.union(u, v):
            mst_weight += weight
            edges_used += 1
            if edges_used == n - 1:
                break

    return mst_weight if edges_used == n - 1 else -1


# ============================================
# PATTERN 2: Prim's Algorithm
# ============================================
def prim(n, edges):
    """
    Find MST weight using Prim's.
    edges = [(u, v, weight), ...]
    """
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = [False] * n
    heap = [(0, 0)]  # (weight, node) - start from node 0
    mst_weight = 0
    edges_used = 0

    while heap and edges_used < n:
        weight, u = heapq.heappop(heap)
        if visited[u]:
            continue

        visited[u] = True
        mst_weight += weight
        edges_used += 1

        for w, v in graph[u]:
            if not visited[v]:
                heapq.heappush(heap, (w, v))

    return mst_weight if edges_used == n else -1


# ============================================
# PATTERN 3: Min Cost to Connect All Points
# ============================================
def min_cost_connect_points(points):
    """
    Connect all points with minimum total Manhattan distance.
    """
    n = len(points)
    if n <= 1:
        return 0

    # Build edges
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((i, j, dist))

    return kruskal(n, edges)


# ============================================
# PATTERN 4: Min Cost to Connect Cities with Threshold
# ============================================
def minimum_cost(n, connections):
    """
    Minimum cost to connect all cities.
    connections[i] = [city1, city2, cost]
    """
    edges = [(u - 1, v - 1, cost) for u, v, cost in connections]  # 0-index
    return kruskal(n, edges)


# ============================================
# PATTERN 5: Optimize Water Distribution
# ============================================
def min_cost_to_supply_water(n, wells, pipes):
    """
    Each house can have a well (cost wells[i]) or pipe from another.
    pipes[i] = [house1, house2, cost]
    Minimize total cost.

    Trick: Add virtual node 0 connected to each house with well cost.
    """
    edges = []

    # Virtual node 0 with well costs
    for i, cost in enumerate(wells):
        edges.append((0, i + 1, cost))

    # Pipe costs
    for h1, h2, cost in pipes:
        edges.append((h1, h2, cost))

    return kruskal(n + 1, edges)


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 1584. Min Cost to Connect All Points
- 1135. Connecting Cities With Minimum Cost

Hard:
- 1168. Optimize Water Distribution in a Village
- 1489. Find Critical and Pseudo-Critical Edges in MST
"""
