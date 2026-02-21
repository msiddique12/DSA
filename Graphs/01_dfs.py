"""
GRAPH DFS (Depth-First Search)
==============================

WHEN TO USE:
- Finding paths/cycles
- Connected components
- Topological sort prep
- Backtracking on graphs

KEY INSIGHT: Go deep first. Use recursion or stack.
Track visited to avoid infinite loops.

TIME: O(V + E)  |  SPACE: O(V)
"""

# ============================================
# PATTERN 1: DFS on Adjacency List
# ============================================
def dfs_recursive(graph, start, visited=None):
    """DFS traversal from start node."""
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def dfs_iterative(graph, start):
    """DFS using explicit stack."""
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            # Add neighbors (reverse for same order as recursive)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)


# ============================================
# PATTERN 2: Find All Paths
# ============================================
def find_all_paths(graph, start, end, path=None):
    """Find all paths from start to end."""
    if path is None:
        path = []

    path = path + [start]

    if start == end:
        return [path]

    paths = []
    for neighbor in graph.get(start, []):
        if neighbor not in path:  # Avoid cycles
            new_paths = find_all_paths(graph, neighbor, end, path)
            paths.extend(new_paths)

    return paths


# ============================================
# PATTERN 3: Detect Cycle in Directed Graph
# ============================================
def has_cycle_directed(graph, n):
    """
    Detect cycle in directed graph using colors.
    WHITE (0): unvisited
    GRAY (1): in current DFS path
    BLACK (2): completely processed
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    def dfs(node):
        color[node] = GRAY

        for neighbor in graph.get(node, []):
            if color[neighbor] == GRAY:  # Back edge = cycle
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True

        color[node] = BLACK
        return False

    for node in range(n):
        if color[node] == WHITE:
            if dfs(node):
                return True

    return False


# ============================================
# PATTERN 4: Detect Cycle in Undirected Graph
# ============================================
def has_cycle_undirected(graph, n):
    """Detect cycle in undirected graph."""
    visited = [False] * n

    def dfs(node, parent):
        visited[node] = True

        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:  # Back edge (not parent)
                return True

        return False

    for node in range(n):
        if not visited[node]:
            if dfs(node, -1):
                return True

    return False


# ============================================
# PATTERN 5: Clone Graph
# ============================================
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def clone_graph(node):
    """Deep copy a graph."""
    if not node:
        return None

    visited = {}  # original -> clone

    def dfs(n):
        if n in visited:
            return visited[n]

        clone = Node(n.val)
        visited[n] = clone

        for neighbor in n.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 133. Clone Graph
- 207. Course Schedule (cycle detection)
- 210. Course Schedule II
- 547. Number of Provinces
- 841. Keys and Rooms

Hard:
- 332. Reconstruct Itinerary
"""
