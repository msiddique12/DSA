"""
TREE DFS - ITERATIVE (Using Stack)
==================================

WHEN TO USE:
- When recursion depth might cause stack overflow
- When you need more control over traversal
- Morris traversal for O(1) space

KEY INSIGHT: Stack mimics call stack. Push right first (LIFO).

TIME: O(n)  |  SPACE: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================
# PATTERN 1: Preorder Iterative
# ============================================
def preorder_iterative(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)
        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


# ============================================
# PATTERN 2: Inorder Iterative
# ============================================
def inorder_iterative(root):
    result = []
    stack = []
    curr = root

    while curr or stack:
        # Go all the way left
        while curr:
            stack.append(curr)
            curr = curr.left
        # Process node
        curr = stack.pop()
        result.append(curr.val)
        # Go right
        curr = curr.right

    return result


# ============================================
# PATTERN 3: Postorder Iterative
# ============================================
def postorder_iterative(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)
        # Push left first so right is processed first
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return result[::-1]  # Reverse at end


# ============================================
# PATTERN 4: BST Iterator (Controlled Inorder)
# ============================================
class BSTIterator:
    """
    Useful when you need to traverse BST on-demand.
    next() returns next smallest, hasNext() checks if more.
    """
    def __init__(self, root):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        top = self.stack.pop()
        if top.right:
            self._leftmost_inorder(top.right)
        return top.val

    def hasNext(self):
        return len(self.stack) > 0


# ============================================
# PATTERN 5: Morris Inorder (O(1) Space)
# ============================================
def morris_inorder(root):
    """
    O(1) space by threading tree (temporarily modify structure).
    """
    result = []
    curr = root

    while curr:
        if not curr.left:
            result.append(curr.val)
            curr = curr.right
        else:
            # Find inorder predecessor
            pred = curr.left
            while pred.right and pred.right != curr:
                pred = pred.right

            if not pred.right:
                # Thread it
                pred.right = curr
                curr = curr.left
            else:
                # Revert thread
                pred.right = None
                result.append(curr.val)
                curr = curr.right

    return result


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 144. Binary Tree Preorder Traversal
- 94. Binary Tree Inorder Traversal
- 145. Binary Tree Postorder Traversal

Medium:
- 173. Binary Search Tree Iterator
- 230. Kth Smallest Element in BST
- 98. Validate BST (iterative inorder)
- 99. Recover BST (Morris traversal)
"""
