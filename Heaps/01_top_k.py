"""
TOP K ELEMENTS
==============

WHEN TO USE:
- Kth largest/smallest element
- K most frequent elements
- K closest points
- K largest sum combinations

KEY INSIGHT: Use min-heap of size K for "K largest" (pop smallest).
Use max-heap of size K for "K smallest" (pop largest).

TIME: O(n log k)  |  SPACE: O(k)
"""

import heapq
from collections import Counter

# ============================================
# PATTERN 1: Kth Largest Element
# ============================================
def find_kth_largest(nums, k):
    """Find kth largest element."""
    # Min-heap of size k - smallest of the k largest will be at top
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # Remove smallest

    return heap[0]  # Kth largest

# Alternative using heapq.nlargest
def find_kth_largest_alt(nums, k):
    return heapq.nlargest(k, nums)[-1]


# ============================================
# PATTERN 2: Top K Frequent Elements
# ============================================
def top_k_frequent(nums, k):
    """Return k most frequent elements."""
    count = Counter(nums)

    # Min-heap by frequency
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [item[1] for item in heap]


# ============================================
# PATTERN 3: K Closest Points to Origin
# ============================================
def k_closest(points, k):
    """Return k closest points to origin."""
    # Max-heap (negate distance) of size k
    heap = []

    for x, y in points:
        dist = -(x*x + y*y)  # Negative for max-heap behavior
        heapq.heappush(heap, (dist, x, y))
        if len(heap) > k:
            heapq.heappop(heap)

    return [[x, y] for _, x, y in heap]


# ============================================
# PATTERN 4: Sort Array by Frequency
# ============================================
def frequency_sort(s):
    """Sort string by character frequency (descending)."""
    count = Counter(s)
    # Max-heap by frequency
    heap = [(-freq, char) for char, freq in count.items()]
    heapq.heapify(heap)

    result = []
    while heap:
        freq, char = heapq.heappop(heap)
        result.append(char * (-freq))

    return ''.join(result)


# ============================================
# PATTERN 5: Find K Pairs with Smallest Sums
# ============================================
def k_smallest_pairs(nums1, nums2, k):
    """Find k pairs with smallest sums from two sorted arrays."""
    if not nums1 or not nums2:
        return []

    heap = [(nums1[0] + nums2[0], 0, 0)]
    seen = {(0, 0)}
    result = []

    while heap and len(result) < k:
        _, i, j = heapq.heappop(heap)
        result.append([nums1[i], nums2[j]])

        if i + 1 < len(nums1) and (i + 1, j) not in seen:
            heapq.heappush(heap, (nums1[i+1] + nums2[j], i + 1, j))
            seen.add((i + 1, j))

        if j + 1 < len(nums2) and (i, j + 1) not in seen:
            heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j + 1))
            seen.add((i, j + 1))

    return result


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 215. Kth Largest Element in an Array
- 347. Top K Frequent Elements
- 973. K Closest Points to Origin
- 451. Sort Characters By Frequency
- 692. Top K Frequent Words
- 378. Kth Smallest Element in Sorted Matrix
- 373. Find K Pairs with Smallest Sums

Hard:
- 295. Find Median from Data Stream (two heaps)
"""
