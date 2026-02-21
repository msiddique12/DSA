"""
PATH PROBLEMS (Grid DP)
=======================

WHEN TO USE:
- Counting paths in grid
- Minimum/maximum path sum
- Can only move right/down

KEY INSIGHT: dp[i][j] depends on dp[i-1][j] and dp[i][j-1].
Can often optimize to O(n) space.

TIME: O(m*n)  |  SPACE: O(m*n) or O(n)
"""

# ============================================
# PATTERN 1: Unique Paths
# ============================================
def unique_paths(m, n):
    """Count unique paths from top-left to bottom-right."""
    dp = [1] * n  # First row is all 1s

    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]  # Current = above + left

    return dp[n-1]


# ============================================
# PATTERN 2: Unique Paths with Obstacles
# ============================================
def unique_paths_with_obstacles(grid):
    """Count paths avoiding obstacles (1 = obstacle)."""
    if not grid or grid[0][0] == 1:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [0] * n
    dp[0] = 1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j-1]

    return dp[n-1]


# ============================================
# PATTERN 3: Minimum Path Sum
# ============================================
def min_path_sum(grid):
    """Minimum sum path from top-left to bottom-right."""
    m, n = len(grid), len(grid[0])
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(m):
        dp[0] += grid[i][0]
        for j in range(1, n):
            dp[j] = min(dp[j], dp[j-1]) + grid[i][j]

    return dp[n-1]


# ============================================
# PATTERN 4: Triangle (Min Path Sum)
# ============================================
def minimum_total(triangle):
    """Minimum path sum from top to bottom of triangle."""
    n = len(triangle)
    dp = triangle[-1][:]  # Start from bottom

    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            dp[j] = triangle[i][j] + min(dp[j], dp[j+1])

    return dp[0]


# ============================================
# PATTERN 5: Maximum Path Sum in Grid (All directions)
# ============================================
def max_path_sum_any_direction(grid):
    """
    Max path sum where you can move in any direction (no revisit).
    This needs DFS with memoization, not simple DP.
    """
    # This is actually backtracking, shown for comparison
    m, n = len(grid), len(grid[0])

    def dfs(i, j, visited):
        if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited:
            return 0

        visited.add((i, j))
        max_sum = grid[i][j] + max(
            dfs(i+1, j, visited),
            dfs(i-1, j, visited),
            dfs(i, j+1, visited),
            dfs(i, j-1, visited),
            0
        )
        visited.remove((i, j))
        return max_sum

    return max(dfs(i, j, set()) for i in range(m) for j in range(n))


# ============================================
# PATTERN 6: Dungeon Game
# ============================================
def calculate_minimum_hp(dungeon):
    """Minimum initial HP to reach princess (bottom-right)."""
    m, n = len(dungeon), len(dungeon[0])
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    dp[m][n-1] = dp[m-1][n] = 1  # Need at least 1 HP at end

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            need = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
            dp[i][j] = max(1, need)  # At least 1 HP needed

    return dp[0][0]


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 62. Unique Paths
- 63. Unique Paths II
- 64. Minimum Path Sum
- 120. Triangle
- 931. Minimum Falling Path Sum

Hard:
- 174. Dungeon Game
- 741. Cherry Pickup
- 1463. Cherry Pickup II
"""
