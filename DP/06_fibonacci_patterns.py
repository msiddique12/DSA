"""
FIBONACCI PATTERNS
==================

WHEN TO USE:
- Current state depends on previous 1-2 states
- Climbing stairs variants
- House robber variants
- Decode ways

KEY INSIGHT: dp[i] = f(dp[i-1], dp[i-2], ...)
Often optimizable to O(1) space.

TIME: O(n)  |  SPACE: O(1)
"""

# ============================================
# PATTERN 1: Fibonacci Number
# ============================================
def fib(n):
    """Nth fibonacci number."""
    if n <= 1:
        return n

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1


# ============================================
# PATTERN 2: Climbing Stairs
# ============================================
def climb_stairs(n):
    """Ways to climb n stairs (1 or 2 steps at a time)."""
    if n <= 2:
        return n

    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1


# ============================================
# PATTERN 3: House Robber
# ============================================
def rob(nums):
    """Max money robbing non-adjacent houses."""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2, prev1 = 0, 0
    for num in nums:
        curr = max(prev1, prev2 + num)  # Skip or rob current
        prev2, prev1 = prev1, curr

    return prev1


# ============================================
# PATTERN 4: House Robber II (Circular)
# ============================================
def rob_circular(nums):
    """Max money robbing circular houses (first and last are adjacent)."""
    if len(nums) == 1:
        return nums[0]

    def rob_linear(houses):
        prev2, prev1 = 0, 0
        for num in houses:
            curr = max(prev1, prev2 + num)
            prev2, prev1 = prev1, curr
        return prev1

    # Either skip first house or skip last house
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# ============================================
# PATTERN 5: Decode Ways
# ============================================
def num_decodings(s):
    """Count ways to decode string (A=1, B=2, ..., Z=26)."""
    if not s or s[0] == '0':
        return 0

    n = len(s)
    prev2, prev1 = 1, 1  # dp[0], dp[1]

    for i in range(1, n):
        curr = 0

        # Single digit
        if s[i] != '0':
            curr += prev1

        # Two digits (10-26)
        two_digit = int(s[i-1:i+1])
        if 10 <= two_digit <= 26:
            curr += prev2

        prev2, prev1 = prev1, curr

    return prev1


# ============================================
# PATTERN 6: Min Cost Climbing Stairs
# ============================================
def min_cost_climbing_stairs(cost):
    """Minimum cost to reach top (1 or 2 steps)."""
    prev2, prev1 = 0, 0

    for c in cost:
        curr = c + min(prev1, prev2)
        prev2, prev1 = prev1, curr

    return min(prev1, prev2)


# ============================================
# PATTERN 7: Delete and Earn
# ============================================
def delete_and_earn(nums):
    """
    Delete num to earn num points, but must delete all num-1 and num+1.
    Transform to house robber: can't pick adjacent values.
    """
    if not nums:
        return 0

    max_num = max(nums)
    points = [0] * (max_num + 1)
    for num in nums:
        points[num] += num

    # House robber on points array
    prev2, prev1 = 0, 0
    for point in points:
        curr = max(prev1, prev2 + point)
        prev2, prev1 = prev1, curr

    return prev1


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 509. Fibonacci Number
- 70. Climbing Stairs
- 746. Min Cost Climbing Stairs

Medium:
- 198. House Robber
- 213. House Robber II
- 91. Decode Ways
- 740. Delete and Earn
- 801. Minimum Swaps To Make Sequences Increasing
"""
