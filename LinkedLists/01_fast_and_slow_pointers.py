"""
FAST AND SLOW POINTERS (Floyd's Tortoise & Hare)
================================================

WHEN TO USE:
- Cycle detection
- Finding middle of list
- Finding cycle start
- Kth element from end

KEY INSIGHT: Slow moves 1 step, fast moves 2 steps.
When fast reaches end, slow is at middle.
If they meet, there's a cycle.

TIME: O(n)  |  SPACE: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ============================================
# PATTERN 1: Cycle Detection
# ============================================
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# ============================================
# PATTERN 2: Find Middle
# ============================================
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # For even length, returns 2nd middle


# ============================================
# PATTERN 3: Find Cycle Start
# ============================================
def find_cycle_start(head):
    # Phase 1: Detect cycle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle

    # Phase 2: Find start (reset one pointer to head)
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


# ============================================
# PATTERN 4: Kth From End
# ============================================
def kth_from_end(head, k):
    slow = fast = head
    for _ in range(k):  # Move fast k steps ahead
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 141. Linked List Cycle
- 876. Middle of the Linked List

Medium:
- 142. Linked List Cycle II
- 19. Remove Nth Node From End
- 234. Palindrome Linked List (find middle + reverse)
- 143. Reorder List

Hard:
- 287. Find the Duplicate Number (treat array as linked list!)
"""
