"""
WORD SEARCH
===========

WHEN TO USE:
- Finding path in grid
- Pattern matching in 2D
- DFS with backtracking on grid

KEY INSIGHT: DFS from each cell, mark visited, backtrack.
For multiple words, use Trie for efficiency.

TIME: O(m*n*4^L) where L = word length  |  SPACE: O(L)
"""

# ============================================
# PATTERN 1: Word Search (Single Word)
# ============================================
def exist(board, word):
    """Check if word exists in grid (adjacent cells)."""
    if not board:
        return False

    rows, cols = len(board), len(board[0])

    def dfs(r, c, index):
        if index == len(word):
            return True
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            board[r][c] != word[index]):
            return False

        # Mark visited
        temp = board[r][c]
        board[r][c] = '#'

        # Explore all 4 directions
        found = (dfs(r + 1, c, index + 1) or
                 dfs(r - 1, c, index + 1) or
                 dfs(r, c + 1, index + 1) or
                 dfs(r, c - 1, index + 1))

        # Backtrack
        board[r][c] = temp
        return found

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False


# ============================================
# PATTERN 2: Word Search II (Multiple Words with Trie)
# ============================================
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

def find_words(board, words):
    """Find all words from list that exist in grid."""
    # Build Trie
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

    rows, cols = len(board), len(board[0])
    result = []

    def dfs(r, c, node):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        char = board[r][c]
        if char not in node.children:
            return

        node = node.children[char]
        if node.word:
            result.append(node.word)
            node.word = None  # Avoid duplicates

        board[r][c] = '#'
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(r + dr, c + dc, node)
        board[r][c] = char

    for i in range(rows):
        for j in range(cols):
            dfs(i, j, root)

    return result


# ============================================
# PATTERN 3: Path with Maximum Gold
# ============================================
def get_maximum_gold(grid):
    """Collect maximum gold, can't visit same cell twice."""
    rows, cols = len(grid), len(grid[0])
    max_gold = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 0

        gold = grid[r][c]
        grid[r][c] = 0  # Mark visited

        max_path = 0
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            max_path = max(max_path, dfs(r + dr, c + dc))

        grid[r][c] = gold  # Backtrack
        return gold + max_path

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 0:
                max_gold = max(max_gold, dfs(i, j))

    return max_gold


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 79. Word Search
- 1219. Path with Maximum Gold

Hard:
- 212. Word Search II (Trie + backtracking)
"""
