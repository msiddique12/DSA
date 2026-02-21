"""
MONOTONIC STACK
===============

WHEN TO USE:
- Next greater/smaller element
- Stock span problems
- Histogram problems (largest rectangle)
- Temperature problems

KEY INSIGHT: Maintain stack in increasing/decreasing order.
Pop elements that violate the monotonic property.

TIME: O(n)  |  SPACE: O(n)
"""

# ============================================
# PATTERN 1: Next Greater Element
# ============================================
def next_greater_element(nums):
    """Find next greater element for each position."""
    n = len(nums)
    result = [-1] * n
    stack = []  # Store indices

    for i in range(n):
        # Pop all elements smaller than current
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)

    return result


# ============================================
# PATTERN 2: Next Greater Element (Circular)
# ============================================
def next_greater_circular(nums):
    """Next greater in circular array."""
    n = len(nums)
    result = [-1] * n
    stack = []

    # Traverse twice for circular
    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            result[stack.pop()] = nums[i % n]
        if i < n:
            stack.append(i)

    return result


# ============================================
# PATTERN 3: Daily Temperatures
# ============================================
def daily_temperatures(temps):
    """Days to wait for warmer temperature."""
    n = len(temps)
    result = [0] * n
    stack = []

    for i in range(n):
        while stack and temps[stack[-1]] < temps[i]:
            prev = stack.pop()
            result[prev] = i - prev
        stack.append(i)

    return result


# ============================================
# PATTERN 4: Largest Rectangle in Histogram
# ============================================
def largest_rectangle_in_histogram(heights):
    """Find largest rectangle area in histogram."""
    stack = []  # (index, height)
    max_area = 0

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))

    # Process remaining in stack
    for idx, height in stack:
        max_area = max(max_area, height * (len(heights) - idx))

    return max_area


# ============================================
# PATTERN 5: Maximal Rectangle (2D)
# ============================================
def maximal_rectangle(matrix):
    """Largest rectangle of 1s in binary matrix."""
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0

        max_area = max(max_area, largest_rectangle_in_histogram(heights))

    return max_area


# ============================================
# PATTERN 6: Trapping Rain Water
# ============================================
def trap(height):
    """Calculate trapped rain water."""
    stack = []
    water = 0

    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            bottom = stack.pop()
            if stack:
                bounded_height = min(h, height[stack[-1]]) - height[bottom]
                width = i - stack[-1] - 1
                water += bounded_height * width
        stack.append(i)

    return water


# ============================================
# PATTERN 7: Stock Span
# ============================================
class StockSpanner:
    """Days since last higher price (including today)."""
    def __init__(self):
        self.stack = []  # (price, span)

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 496. Next Greater Element I

Medium:
- 739. Daily Temperatures
- 503. Next Greater Element II (circular)
- 901. Online Stock Span
- 907. Sum of Subarray Minimums

Hard:
- 84. Largest Rectangle in Histogram
- 85. Maximal Rectangle
- 42. Trapping Rain Water
"""
