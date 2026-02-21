"""
DUMMY NODES
===========

WHEN TO USE:
- Head might change (deletion, insertion at front)
- Merging lists
- Partitioning lists
- Any time you need a "before head" reference

KEY INSIGHT: Create fake node before head. Return dummy.next at end.
Avoids special-casing head operations.

TIME: O(n)  |  SPACE: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ============================================
# PATTERN 1: Remove Elements
# ============================================
def remove_elements(head, val):
    dummy = ListNode(0, head)
    curr = dummy

    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next  # Skip the node
        else:
            curr = curr.next

    return dummy.next


# ============================================
# PATTERN 2: Merge Two Sorted Lists
# ============================================
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 or l2  # Attach remaining
    return dummy.next


# ============================================
# PATTERN 3: Partition List
# ============================================
def partition(head, x):
    # Two dummy heads: one for < x, one for >= x
    before = before_head = ListNode(0)
    after = after_head = ListNode(0)

    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next

    after.next = None           # Important! Avoid cycle
    before.next = after_head.next  # Connect the two lists

    return before_head.next


# ============================================
# PATTERN 4: Add Two Numbers
# ============================================
def add_two_numbers(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 21. Merge Two Sorted Lists
- 203. Remove Linked List Elements
- 83. Remove Duplicates from Sorted List

Medium:
- 2. Add Two Numbers
- 86. Partition List
- 82. Remove Duplicates from Sorted List II
- 19. Remove Nth Node From End (dummy helps with edge case)
- 148. Sort List (merge sort with dummy)

Hard:
- 23. Merge k Sorted Lists
"""
