"""
CLONE/COPY GRAPH (BFS)
======================

WHEN TO USE:
- Deep copy of graph structure
- Copy with random pointers
- When need to preserve structure but create new nodes

KEY INSIGHT: Use hashmap to map original nodes to clones.
BFS ensures all nodes are visited level by level.

TIME: O(V + E)  |  SPACE: O(V)
"""

from collections import deque

# ============================================
# PATTERN 1: Clone Graph (BFS)
# ============================================
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def clone_graph_bfs(node):
    """Clone graph using BFS."""
    if not node:
        return None

    old_to_new = {node: Node(node.val)}
    queue = deque([node])

    while queue:
        curr = queue.popleft()

        for neighbor in curr.neighbors:
            if neighbor not in old_to_new:
                old_to_new[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            old_to_new[curr].neighbors.append(old_to_new[neighbor])

    return old_to_new[node]


# ============================================
# PATTERN 2: Copy List with Random Pointer
# ============================================
class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head):
    """Deep copy linked list with random pointers."""
    if not head:
        return None

    old_to_new = {}

    # First pass: create all nodes
    curr = head
    while curr:
        old_to_new[curr] = ListNode(curr.val)
        curr = curr.next

    # Second pass: set next and random pointers
    curr = head
    while curr:
        if curr.next:
            old_to_new[curr].next = old_to_new[curr.next]
        if curr.random:
            old_to_new[curr].random = old_to_new[curr.random]
        curr = curr.next

    return old_to_new[head]


# ============================================
# PATTERN 3: Copy List with Random (O(1) space)
# ============================================
def copy_random_list_optimized(head):
    """Copy without hashmap - interleave then separate."""
    if not head:
        return None

    # Step 1: Create interleaved list (A -> A' -> B -> B' -> ...)
    curr = head
    while curr:
        copy = ListNode(curr.val, curr.next)
        curr.next = copy
        curr = copy.next

    # Step 2: Set random pointers
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate lists
    dummy = ListNode(0)
    copy_curr = dummy
    curr = head

    while curr:
        copy_curr.next = curr.next
        copy_curr = copy_curr.next
        curr.next = curr.next.next
        curr = curr.next

    return dummy.next


# ============================================
# PATTERN 4: Clone Binary Tree with Random
# ============================================
class TreeNode:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

def clone_tree_with_random(root):
    """Clone binary tree with random pointers."""
    if not root:
        return None

    old_to_new = {}

    # First pass: clone structure
    def clone_structure(node):
        if not node:
            return None
        copy = TreeNode(node.val)
        old_to_new[node] = copy
        copy.left = clone_structure(node.left)
        copy.right = clone_structure(node.right)
        return copy

    new_root = clone_structure(root)

    # Second pass: set random pointers
    def set_random(node):
        if not node:
            return
        if node.random:
            old_to_new[node].random = old_to_new[node.random]
        set_random(node.left)
        set_random(node.right)

    set_random(root)
    return new_root


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 133. Clone Graph
- 138. Copy List with Random Pointer
- 1485. Clone Binary Tree With Random Pointer
"""
