"""
IN-PLACE LINKED LIST REVERSAL
=============================

WHEN TO USE:
- Reverse entire list
- Reverse portion (m to n)
- Reverse in k-groups
- Palindrome check

KEY INSIGHT: Track prev, curr, next. Reverse pointer direction.

TIME: O(n)  |  SPACE: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ============================================
# PATTERN 1: Reverse Entire List
# ============================================
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # Save next
        curr.next = prev       # Reverse link
        prev = curr            # Move prev forward
        curr = next_node       # Move curr forward
    return prev  # New head


# ============================================
# PATTERN 2: Reverse Between m and n
# ============================================
def reverse_between(head, left, right):
    if not head or left == right:
        return head

    dummy = ListNode(0, head)
    conn = dummy  # Node before reversal starts

    for _ in range(left - 1):
        conn = conn.next

    # Reverse from left to right
    tail = conn.next  # Will be tail after reversal
    prev = None
    curr = conn.next

    for _ in range(right - left + 1):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # Reconnect
    conn.next = prev   # Connect to reversed head
    tail.next = curr   # Connect tail to rest

    return dummy.next


# ============================================
# PATTERN 3: Reverse in K-Groups
# ============================================
def reverse_k_group(head, k):
    # Check if k nodes exist
    node = head
    for _ in range(k):
        if not node:
            return head  # Less than k, don't reverse
        node = node.next

    # Reverse k nodes
    prev = None
    curr = head
    for _ in range(k):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # Recursively process rest
    head.next = reverse_k_group(curr, k)
    return prev


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 206. Reverse Linked List

Medium:
- 92. Reverse Linked List II
- 24. Swap Nodes in Pairs
- 61. Rotate List
- 328. Odd Even Linked List

Hard:
- 25. Reverse Nodes in k-Group
"""
