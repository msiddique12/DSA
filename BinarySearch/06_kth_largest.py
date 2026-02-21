"""
KTH LARGEST/SMALLEST ELEMENT
============================

WHEN TO USE:
- Finding kth order statistic
- When full sorting is overkill
- Stream of elements

KEY INSIGHT: Multiple approaches:
- Heap: O(n log k)
- QuickSelect: O(n) average
- Binary Search (on value range): O(n log range)

TIME: varies  |  SPACE: O(k) for heap, O(1) for quickselect
"""

import heapq
import random

# ============================================
# PATTERN 1: Using Heap
# ============================================
def find_kth_largest_heap(nums, k):
    """Use min-heap of size k."""
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


# ============================================
# PATTERN 2: QuickSelect
# ============================================
def find_kth_largest_quickselect(nums, k):
    """
    QuickSelect - average O(n), worst O(n^2).
    Find kth largest = (n-k)th smallest (0-indexed).
    """
    k = len(nums) - k  # Convert to index

    def partition(left, right, pivot_idx):
        pivot = nums[pivot_idx]
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

        store_idx = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[store_idx] = nums[store_idx], nums[i]
                store_idx += 1

        nums[store_idx], nums[right] = nums[right], nums[store_idx]
        return store_idx

    def quickselect(left, right):
        if left == right:
            return nums[left]

        pivot_idx = random.randint(left, right)
        pivot_idx = partition(left, right, pivot_idx)

        if k == pivot_idx:
            return nums[k]
        elif k < pivot_idx:
            return quickselect(left, pivot_idx - 1)
        else:
            return quickselect(pivot_idx + 1, right)

    return quickselect(0, len(nums) - 1)


# ============================================
# PATTERN 3: Kth Largest in Stream
# ============================================
class KthLargest:
    """Maintain kth largest in stream of numbers."""
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# ============================================
# PATTERN 4: Kth Smallest Pair Distance
# ============================================
def smallest_distance_pair(nums, k):
    """
    Find kth smallest distance among all pairs.
    Binary search on distance value.
    """
    nums.sort()
    n = len(nums)

    def count_pairs(max_dist):
        """Count pairs with distance <= max_dist."""
        count = 0
        left = 0
        for right in range(n):
            while nums[right] - nums[left] > max_dist:
                left += 1
            count += right - left
        return count

    left, right = 0, nums[-1] - nums[0]

    while left < right:
        mid = left + (right - left) // 2
        if count_pairs(mid) < k:
            left = mid + 1
        else:
            right = mid

    return left


# ============================================
# PATTERN 5: Find Kth Missing Positive
# ============================================
def find_kth_positive(arr, k):
    """Find kth missing positive integer."""
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2
        # Number of missing positives before index mid
        missing = arr[mid] - (mid + 1)
        if missing < k:
            left = mid + 1
        else:
            right = mid

    # Answer: if no array existed, kth positive is k
    # We need to add back positions where array elements exist
    return left + k


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 703. Kth Largest Element in a Stream
- 1539. Kth Missing Positive Number

Medium:
- 215. Kth Largest Element in an Array

Hard:
- 719. Find K-th Smallest Pair Distance
- 786. K-th Smallest Prime Fraction
"""
