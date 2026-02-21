"""
TREE DEPTH-FIRST SEARCH (DFS)
=============================

WHEN TO USE:
- Path sum problems
- Tree traversals (inorder, preorder, postorder)
- Finding paths from root to leaf
- Checking tree properties (balanced, symmetric)

KEY INSIGHT: Go deep before going wide. Use recursion or stack.

TIME: O(n)  |  SPACE: O(h) where h = height
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================
# PATTERN 1: Basic Traversals (Recursive)
# ============================================
def preorder(root):   # Root -> Left -> Right
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def inorder(root):    # Left -> Root -> Right (BST gives sorted order)
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def postorder(root):  # Left -> Right -> Root
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


# ============================================
# PATTERN 2: Path Sum
# ============================================
def has_path_sum(root, target):
    if not root:
        return False
    if not root.left and not root.right:  # Leaf
        return root.val == target
    return (has_path_sum(root.left, target - root.val) or
            has_path_sum(root.right, target - root.val))


# ============================================
# PATTERN 3: Max Depth
# ============================================
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# ============================================
# PATTERN 4: Same Tree / Symmetric
# ============================================
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and
            is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))

def is_symmetric(root):
    def mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val and
                mirror(t1.left, t2.right) and
                mirror(t1.right, t2.left))
    return mirror(root, root)


# ============================================
# PATTERN 5: Lowest Common Ancestor
# ============================================
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:  # p and q on different sides
        return root
    return left or right


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 104. Maximum Depth of Binary Tree
- 100. Same Tree
- 101. Symmetric Tree
- 112. Path Sum
- 226. Invert Binary Tree

Medium:
- 113. Path Sum II (collect all paths)
- 236. Lowest Common Ancestor
- 98. Validate Binary Search Tree
- 230. Kth Smallest Element in BST
- 105. Construct Tree from Preorder/Inorder
- 124. Binary Tree Maximum Path Sum (Hard)
"""
