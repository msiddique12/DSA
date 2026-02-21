"""
MERGE K SORTED
==============

WHEN TO USE:
- Merge k sorted lists/arrays
- K-way merge
- Smallest range covering elements from k lists

KEY INSIGHT: Use min-heap to always get the smallest current element.
Push (value, list_index, element_index) tuples.

TIME: O(n log k) where n = total elements  |  SPACE: O(k)
"""

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ============================================
# PATTERN 1: Merge K Sorted Lists
# ============================================
def merge_k_lists(lists):
    """Merge k sorted linked lists into one sorted list."""
    # Handle ListNode comparison by wrapping
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))

    dummy = ListNode(0)
    curr = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


# ============================================
# PATTERN 2: Merge K Sorted Arrays
# ============================================
def merge_k_arrays(arrays):
    """Merge k sorted arrays into one sorted array."""
    heap = []
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    result = []
    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))

    return result


# ============================================
# PATTERN 3: Smallest Range Covering K Lists
# ============================================
def smallest_range(nums):
    """
    Find smallest range [a, b] such that for each list,
    at least one number is in [a, b].
    """
    # Track max in current window, use heap for min
    heap = []
    curr_max = float('-inf')

    for i, arr in enumerate(nums):
        heapq.heappush(heap, (arr[0], i, 0))
        curr_max = max(curr_max, arr[0])

    result = [float('-inf'), float('inf')]

    while heap:
        curr_min, arr_idx, elem_idx = heapq.heappop(heap)

        # Update result if smaller range
        if curr_max - curr_min < result[1] - result[0]:
            result = [curr_min, curr_max]

        # Move to next element in that array
        if elem_idx + 1 < len(nums[arr_idx]):
            next_val = nums[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))
            curr_max = max(curr_max, next_val)
        else:
            break  # Can't cover all lists anymore

    return result


# ============================================
# PATTERN 4: Kth Smallest in Sorted Matrix
# ============================================
def kth_smallest(matrix, k):
    """Find kth smallest in row/column sorted matrix."""
    n = len(matrix)
    # Start with first element of each row
    heap = [(matrix[i][0], i, 0) for i in range(min(k, n))]
    heapq.heapify(heap)

    for _ in range(k):
        val, row, col = heapq.heappop(heap)
        if col + 1 < n:
            heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))

    return val


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 378. Kth Smallest Element in a Sorted Matrix

Hard:
- 23. Merge k Sorted Lists
- 632. Smallest Range Covering Elements from K Lists
- 786. K-th Smallest Prime Fraction
"""
