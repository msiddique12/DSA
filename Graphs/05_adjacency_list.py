"""
ADJACENCY LIST BFS/DFS
======================

WHEN TO USE:
- Graph represented as adjacency list
- Sparse graphs (E << V^2)
- Most graph problems

KEY INSIGHT: graph[u] = list of nodes connected to u.
For weighted: graph[u] = [(v, weight), ...]

TIME: O(V + E)  |  SPACE: O(V + E)
"""

from collections import defaultdict, deque

# ============================================
# PATTERN 1: Build Adjacency List
# ============================================
def build_graph(n, edges, directed=False):
    """Build adjacency list from edge list."""
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)

    return graph


def build_weighted_graph(n, edges, directed=False):
    """Build weighted adjacency list."""
    graph = defaultdict(list)

    for u, v, weight in edges:
        graph[u].append((v, weight))
        if not directed:
            graph[v].append((u, weight))

    return graph


# ============================================
# PATTERN 2: Course Schedule (Can Finish?)
# ============================================
def can_finish(num_courses, prerequisites):
    """
    Check if all courses can be finished.
    prereq[i] = [a, b] means must take b before a.
    """
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # 0: unvisited, 1: visiting, 2: visited
    state = [0] * num_courses

    def has_cycle(node):
        if state[node] == 1:  # Currently visiting = cycle
            return True
        if state[node] == 2:  # Already done
            return False

        state[node] = 1
        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True
        state[node] = 2
        return False

    for course in range(num_courses):
        if has_cycle(course):
            return False

    return True


# ============================================
# PATTERN 3: Course Schedule II (Order)
# ============================================
def find_order(num_courses, prerequisites):
    """Return order to take courses (topological sort)."""
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # BFS (Kahn's algorithm)
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == num_courses else []


# ============================================
# PATTERN 4: All Paths Source to Target
# ============================================
def all_paths_source_target(graph):
    """Find all paths from 0 to n-1 in DAG."""
    n = len(graph)
    result = []

    def dfs(node, path):
        if node == n - 1:
            result.append(path[:])
            return

        for neighbor in graph[node]:
            path.append(neighbor)
            dfs(neighbor, path)
            path.pop()

    dfs(0, [0])
    return result


# ============================================
# PATTERN 5: Keys and Rooms
# ============================================
def can_visit_all_rooms(rooms):
    """
    Room i has keys rooms[i]. Start in room 0.
    Can we visit all rooms?
    """
    visited = {0}
    stack = [0]

    while stack:
        room = stack.pop()
        for key in rooms[room]:
            if key not in visited:
                visited.add(key)
                stack.append(key)

    return len(visited) == len(rooms)


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 207. Course Schedule
- 210. Course Schedule II
- 797. All Paths From Source to Target
- 841. Keys and Rooms
- 1462. Course Schedule IV

Hard:
- 269. Alien Dictionary
"""
