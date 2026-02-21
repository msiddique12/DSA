"""
TWO HEAPS
=========

WHEN TO USE:
- Finding median in stream
- Sliding window median
- IPO problem (maximize capital)
- Problems needing both min and max access

KEY INSIGHT: Use max-heap for smaller half, min-heap for larger half.
Median is at the top of one or both heaps.

TIME: O(log n) insert  |  SPACE: O(n)
"""

import heapq

# ============================================
# PATTERN 1: Find Median from Data Stream
# ============================================
class MedianFinder:
    """
    Two heaps:
    - max_heap (small): stores smaller half (negate for max behavior)
    - min_heap (large): stores larger half

    Invariant: len(small) == len(large) or len(small) == len(large) + 1
    """
    def __init__(self):
        self.small = []  # Max-heap (negated)
        self.large = []  # Min-heap

    def addNum(self, num):
        # Add to max-heap first
        heapq.heappush(self.small, -num)

        # Balance: move largest from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Ensure small has >= elements
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2


# ============================================
# PATTERN 2: Sliding Window Median
# ============================================
def median_sliding_window(nums, k):
    """
    Find median of each window of size k.
    Uses lazy deletion (mark as deleted, remove when at top).
    """
    from sortedcontainers import SortedList

    # Easier with SortedList for sliding window
    window = SortedList()
    result = []

    for i, num in enumerate(nums):
        window.add(num)

        # Remove leftmost element outside window
        if i >= k:
            window.remove(nums[i - k])

        # Add median when window is full
        if i >= k - 1:
            if k % 2 == 1:
                result.append(window[k // 2])
            else:
                result.append((window[k // 2 - 1] + window[k // 2]) / 2)

    return result


# ============================================
# PATTERN 3: IPO (Maximize Capital)
# ============================================
def find_maximized_capital(k, w, profits, capital):
    """
    Start with capital w, pick at most k projects.
    Each project i needs capital[i] to start, gives profits[i].
    Maximize total capital.
    """
    # Min-heap of (capital_needed, profit) for projects we can't afford
    unavailable = [(c, p) for c, p in zip(capital, profits)]
    heapq.heapify(unavailable)

    # Max-heap of profits for projects we can afford
    available = []

    for _ in range(k):
        # Move all affordable projects to available
        while unavailable and unavailable[0][0] <= w:
            c, p = heapq.heappop(unavailable)
            heapq.heappush(available, -p)

        if not available:
            break

        # Pick most profitable available project
        w += -heapq.heappop(available)

    return w


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Hard:
- 295. Find Median from Data Stream
- 480. Sliding Window Median
- 502. IPO
- 4. Median of Two Sorted Arrays (binary search approach better)
"""
