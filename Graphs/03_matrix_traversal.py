"""
MATRIX/GRID TRAVERSAL
=====================

WHEN TO USE:
- Island counting
- Flood fill
- Connected regions
- Grid path problems

KEY INSIGHT: Treat each cell as a node, adjacent cells as edges.
4-directional (up/down/left/right) or 8-directional.

TIME: O(m*n)  |  SPACE: O(m*n)
"""

from collections import deque

# ============================================
# PATTERN 1: Number of Islands (DFS)
# ============================================
def num_islands(grid):
    """Count number of islands (connected 1s)."""
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'  # Mark visited
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count


# ============================================
# PATTERN 2: Flood Fill
# ============================================
def flood_fill(image, sr, sc, new_color):
    """Fill connected cells with new color."""
    rows, cols = len(image), len(image[0])
    original = image[sr][sc]

    if original == new_color:
        return image

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != original:
            return
        image[r][c] = new_color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image


# ============================================
# PATTERN 3: Max Area of Island
# ============================================
def max_area_of_island(grid):
    """Find area of largest island."""
    rows, cols = len(grid), len(grid[0])
    max_area = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
            return 0
        grid[r][c] = 0
        return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))

    return max_area


# ============================================
# PATTERN 4: Surrounded Regions
# ============================================
def solve(board):
    """Capture surrounded 'O's (not connected to border)."""
    if not board:
        return

    rows, cols = len(board), len(board[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return
        board[r][c] = 'T'  # Temporarily mark as safe
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Mark all O's connected to border
    for i in range(rows):
        dfs(i, 0)
        dfs(i, cols - 1)
    for j in range(cols):
        dfs(0, j)
        dfs(rows - 1, j)

    # Flip: surrounded O -> X, safe T -> O
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'T':
                board[i][j] = 'O'


# ============================================
# PATTERN 5: Rotting Oranges (BFS)
# ============================================
def oranges_rotting(grid):
    """Minutes until all oranges rot (-1 if impossible)."""
    rows, cols = len(grid), len(grid[0])
    fresh = 0
    queue = deque()

    # Find initial rotten oranges and count fresh
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    max_time = 0
    while queue:
        r, c, time = queue.popleft()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                max_time = time + 1
                queue.append((nr, nc, time + 1))

    return max_time if fresh == 0 else -1


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 733. Flood Fill

Medium:
- 200. Number of Islands
- 695. Max Area of Island
- 130. Surrounded Regions
- 994. Rotting Oranges
- 417. Pacific Atlantic Water Flow
- 1254. Number of Closed Islands
"""
