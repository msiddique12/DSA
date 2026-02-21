"""
TREE BREADTH-FIRST SEARCH (BFS) / LEVEL ORDER
==============================================

WHEN TO USE:
- Level order traversal
- Finding shortest path in unweighted tree
- Level-by-level processing
- Connect nodes at same level

KEY INSIGHT: Use queue. Process level by level.

TIME: O(n)  |  SPACE: O(w) where w = max width
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================
# PATTERN 1: Basic Level Order
# ============================================
def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):  # Process current level
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result


# ============================================
# PATTERN 2: Zigzag Level Order
# ============================================
def zigzag_level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level = deque()
        for _ in range(len(queue)):
            node = queue.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(list(level))
        left_to_right = not left_to_right

    return result


# ============================================
# PATTERN 3: Right Side View
# ============================================
def right_side_view(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:  # Rightmost node
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


# ============================================
# PATTERN 4: Minimum Depth
# ============================================
def min_depth(root):
    if not root:
        return 0

    queue = deque([(root, 1)])  # (node, depth)

    while queue:
        node, depth = queue.popleft()
        if not node.left and not node.right:  # First leaf = min depth
            return depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return 0


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 111. Minimum Depth of Binary Tree

Medium:
- 102. Binary Tree Level Order Traversal
- 103. Binary Tree Zigzag Level Order
- 199. Binary Tree Right Side View
- 116. Populating Next Right Pointers
- 515. Find Largest Value in Each Row
- 513. Find Bottom Left Tree Value
- 1161. Maximum Level Sum
"""
