"""
CONNECTED COMPONENTS
====================

WHEN TO USE:
- Count separate groups
- Friend circles / provinces
- Network connectivity

KEY INSIGHT: Run DFS/BFS from unvisited nodes.
Each run discovers one component.

TIME: O(V + E)  |  SPACE: O(V)
"""

from collections import defaultdict, deque

# ============================================
# PATTERN 1: Count Components (DFS)
# ============================================
def count_components(n, edges):
    """Count number of connected components."""
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in range(n):
        if node not in visited:
            dfs(node)
            count += 1

    return count


# ============================================
# PATTERN 2: Friend Circles / Provinces
# ============================================
def find_circle_num(is_connected):
    """
    Count provinces from adjacency matrix.
    is_connected[i][j] = 1 means i and j are connected.
    """
    n = len(is_connected)
    visited = [False] * n
    count = 0

    def dfs(city):
        visited[city] = True
        for other in range(n):
            if is_connected[city][other] == 1 and not visited[other]:
                dfs(other)

    for city in range(n):
        if not visited[city]:
            dfs(city)
            count += 1

    return count


# ============================================
# PATTERN 3: Graph Valid Tree
# ============================================
def valid_tree(n, edges):
    """
    Check if edges form a valid tree (connected, no cycles).
    Tree has exactly n-1 edges.
    """
    if len(edges) != n - 1:
        return False

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if neighbor in visited:  # Cycle
                return False
            if not dfs(neighbor, node):
                return False
        return True

    if not dfs(0, -1):
        return False

    return len(visited) == n  # Must be connected


# ============================================
# PATTERN 4: Accounts Merge
# ============================================
def accounts_merge(accounts):
    """Merge accounts with same email."""
    from collections import defaultdict

    # Build graph: email -> emails in same account
    email_to_name = {}
    graph = defaultdict(set)

    for account in accounts:
        name = account[0]
        first_email = account[1]

        for email in account[1:]:
            graph[first_email].add(email)
            graph[email].add(first_email)
            email_to_name[email] = name

    visited = set()
    result = []

    def dfs(email, emails):
        visited.add(email)
        emails.append(email)
        for neighbor in graph[email]:
            if neighbor not in visited:
                dfs(neighbor, emails)

    for email in graph:
        if email not in visited:
            emails = []
            dfs(email, emails)
            result.append([email_to_name[email]] + sorted(emails))

    return result


# ============================================
# PATTERN 5: Critical Connections (Bridges)
# ============================================
def critical_connections(n, connections):
    """Find edges whose removal disconnects graph."""
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    disc = [0] * n  # Discovery time
    low = [0] * n   # Lowest reachable discovery time
    visited = [False] * n
    bridges = []
    time = [0]

    def dfs(node, parent):
        visited[node] = True
        disc[node] = low[node] = time[0]
        time[0] += 1

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > disc[node]:  # Bridge
                    bridges.append([node, neighbor])
            elif neighbor != parent:
                low[node] = min(low[node], disc[neighbor])

    dfs(0, -1)
    return bridges


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 323. Number of Connected Components
- 547. Number of Provinces (Friend Circles)
- 261. Graph Valid Tree
- 721. Accounts Merge

Hard:
- 1192. Critical Connections in a Network
"""
