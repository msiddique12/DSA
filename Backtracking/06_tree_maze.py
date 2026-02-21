"""
TREE/MAZE BACKTRACKING
======================

WHEN TO USE:
- Path finding in trees/graphs
- All paths to target
- Decision trees
- Maze solving

KEY INSIGHT: Explore all paths, backtrack when stuck.
Track path and visited to avoid cycles.

TIME: O(2^n) worst case  |  SPACE: O(n) path length
"""

# ============================================
# PATTERN 1: All Paths from Root to Leaf
# ============================================
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def all_paths(root):
    """Find all root-to-leaf paths."""
    result = []

    def dfs(node, path):
        if not node:
            return

        path.append(node.val)

        if not node.left and not node.right:
            result.append(path[:])
        else:
            dfs(node.left, path)
            dfs(node.right, path)

        path.pop()  # Backtrack

    dfs(root, [])
    return result


# ============================================
# PATTERN 2: Path Sum II (Paths with Target Sum)
# ============================================
def path_sum(root, target):
    """Find all root-to-leaf paths with given sum."""
    result = []

    def dfs(node, path, remaining):
        if not node:
            return

        path.append(node.val)

        if not node.left and not node.right and remaining == node.val:
            result.append(path[:])
        else:
            dfs(node.left, path, remaining - node.val)
            dfs(node.right, path, remaining - node.val)

        path.pop()

    dfs(root, [], target)
    return result


# ============================================
# PATTERN 3: Maze - All Paths to Destination
# ============================================
def all_paths_maze(graph):
    """
    Find all paths from node 0 to node n-1 in DAG.
    graph[i] = list of nodes reachable from i.
    """
    result = []
    n = len(graph)

    def dfs(node, path):
        path.append(node)

        if node == n - 1:
            result.append(path[:])
        else:
            for neighbor in graph[node]:
                dfs(neighbor, path)

        path.pop()

    dfs(0, [])
    return result


# ============================================
# PATTERN 4: Maze with Obstacles
# ============================================
def unique_paths_with_obstacles(grid):
    """Count unique paths in grid with obstacles (DP better, but backtrack works)."""
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
        return 0

    count = 0

    def dfs(r, c):
        nonlocal count
        if r == rows - 1 and c == cols - 1:
            count += 1
            return

        grid[r][c] = 1  # Mark visited

        # Only move right or down
        if r + 1 < rows and grid[r + 1][c] != 1:
            dfs(r + 1, c)
        if c + 1 < cols and grid[r][c + 1] != 1:
            dfs(r, c + 1)

        grid[r][c] = 0  # Backtrack

    dfs(0, 0)
    return count


# ============================================
# PATTERN 5: Generate Parentheses
# ============================================
def generate_parenthesis(n):
    """Generate all valid combinations of n pairs of parentheses."""
    result = []

    def backtrack(path, open_count, close_count):
        if len(path) == 2 * n:
            result.append(''.join(path))
            return

        if open_count < n:
            path.append('(')
            backtrack(path, open_count + 1, close_count)
            path.pop()

        if close_count < open_count:
            path.append(')')
            backtrack(path, open_count, close_count + 1)
            path.pop()

    backtrack([], 0, 0)
    return result


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 113. Path Sum II
- 797. All Paths From Source to Target
- 22. Generate Parentheses
- 93. Restore IP Addresses
- 131. Palindrome Partitioning

Hard:
- 301. Remove Invalid Parentheses
- 1240. Tiling a Rectangle with Fewest Squares
"""
