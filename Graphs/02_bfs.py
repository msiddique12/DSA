"""
GRAPH BFS (Breadth-First Search)
================================

WHEN TO USE:
- Shortest path in unweighted graph
- Level-by-level traversal
- Minimum steps to reach target

KEY INSIGHT: Use queue. First time you reach a node = shortest path.

TIME: O(V + E)  |  SPACE: O(V)
"""

from collections import deque

# ============================================
# PATTERN 1: Basic BFS
# ============================================
def bfs(graph, start):
    """BFS traversal from start."""
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# ============================================
# PATTERN 2: Shortest Path (Unweighted)
# ============================================
def shortest_path(graph, start, end):
    """Find shortest path from start to end."""
    if start == end:
        return [start]

    visited = {start}
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []  # No path


# ============================================
# PATTERN 3: Shortest Distance (Return Length)
# ============================================
def shortest_distance(graph, start, end):
    """Return length of shortest path (-1 if none)."""
    if start == end:
        return 0

    visited = {start}
    queue = deque([(start, 0)])

    while queue:
        node, dist = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor == end:
                return dist + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1


# ============================================
# PATTERN 4: Multi-Source BFS
# ============================================
def multi_source_bfs(grid, sources):
    """
    BFS from multiple starting points simultaneously.
    Example: Distance from each cell to nearest source.
    """
    rows, cols = len(grid), len(grid[0])
    dist = [[float('inf')] * cols for _ in range(rows)]

    queue = deque()
    for r, c in sources:
        dist[r][c] = 0
        queue.append((r, c))

    while queue:
        r, c = queue.popleft()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

    return dist


# ============================================
# PATTERN 5: Word Ladder (Transform word)
# ============================================
def ladder_length(begin_word, end_word, word_list):
    """
    Transform begin_word to end_word, changing one letter at a time.
    Each intermediate word must be in word_list.
    """
    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    queue = deque([(begin_word, 1)])
    visited = {begin_word}

    while queue:
        word, steps = queue.popleft()

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word == end_word:
                    return steps + 1
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1))

    return 0


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 127. Word Ladder
- 994. Rotting Oranges (multi-source)
- 286. Walls and Gates
- 1091. Shortest Path in Binary Matrix

Hard:
- 126. Word Ladder II (all shortest paths)
- 815. Bus Routes
"""
