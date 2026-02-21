"""
TOPOLOGICAL SORTING
===================

WHEN TO USE:
- Task scheduling with dependencies
- Course prerequisites
- Build order
- DAG (Directed Acyclic Graph) only

KEY INSIGHT: Process nodes with no incoming edges first (Kahn's).
Or use DFS post-order (reversed).

TIME: O(V + E)  |  SPACE: O(V)
"""

from collections import deque, defaultdict

# ============================================
# PATTERN 1: Kahn's Algorithm (BFS)
# ============================================
def topological_sort_kahn(n, edges):
    """
    Return topological order using Kahn's algorithm.
    edges = [(u, v), ...] meaning u must come before v.
    """
    graph = defaultdict(list)
    in_degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Start with nodes having no prerequisites
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If order doesn't include all nodes, there's a cycle
    return order if len(order) == n else []


# ============================================
# PATTERN 2: DFS-based Topological Sort
# ============================================
def topological_sort_dfs(n, edges):
    """Return topological order using DFS."""
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    order = []
    has_cycle = [False]

    def dfs(node):
        if has_cycle[0]:
            return
        color[node] = GRAY

        for neighbor in graph[node]:
            if color[neighbor] == GRAY:  # Back edge = cycle
                has_cycle[0] = True
                return
            if color[neighbor] == WHITE:
                dfs(neighbor)

        color[node] = BLACK
        order.append(node)  # Add in post-order

    for node in range(n):
        if color[node] == WHITE:
            dfs(node)

    return order[::-1] if not has_cycle[0] else []


# ============================================
# PATTERN 3: Course Schedule II
# ============================================
def find_order(num_courses, prerequisites):
    """Return order to take courses."""
    # prerequisites[i] = [a, b] means b before a
    return topological_sort_kahn(
        num_courses,
        [(b, a) for a, b in prerequisites]
    )


# ============================================
# PATTERN 4: Alien Dictionary
# ============================================
def alien_order(words):
    """
    Given sorted alien dictionary, find character order.
    Return "" if invalid.
    """
    # Build graph from adjacent word pairs
    graph = defaultdict(set)
    in_degree = {c: 0 for word in words for c in word}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))

        # Check for invalid case: prefix comes after
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""

        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break

    # Kahn's algorithm
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    result = []

    while queue:
        char = queue.popleft()
        result.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return "".join(result) if len(result) == len(in_degree) else ""


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 207. Course Schedule (detect cycle)
- 210. Course Schedule II
- 802. Find Eventual Safe States

Hard:
- 269. Alien Dictionary
- 329. Longest Increasing Path in a Matrix
"""
