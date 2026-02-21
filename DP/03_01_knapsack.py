"""
0/1 KNAPSACK
============

WHEN TO USE:
- Select items with weight/value (can't repeat)
- Subset sum problems
- Partition problems

KEY INSIGHT: For each item, either include (if fits) or exclude.
dp[i][w] = max value using first i items with capacity w.

TIME: O(n*W)  |  SPACE: O(n*W) or O(W) optimized
"""

# ============================================
# PATTERN 1: Classic 0/1 Knapsack
# ============================================
def knapsack(weights, values, capacity):
    """Maximum value achievable with given capacity."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i
            dp[i][w] = dp[i-1][w]
            # Take item i (if it fits)
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])

    return dp[n][capacity]


# ============================================
# PATTERN 2: Subset Sum (Can we reach target?)
# ============================================
def can_partition(nums, target):
    """Check if subset sums to target."""
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        # Traverse backwards to avoid reusing same item
        for t in range(target, num - 1, -1):
            dp[t] = dp[t] or dp[t - num]

    return dp[target]


# ============================================
# PATTERN 3: Partition Equal Subset Sum
# ============================================
def can_partition_equal(nums):
    """Can array be partitioned into two equal sum subsets?"""
    total = sum(nums)
    if total % 2 != 0:
        return False

    return can_partition(nums, total // 2)


# ============================================
# PATTERN 4: Target Sum (+ or - each number)
# ============================================
def find_target_sum_ways(nums, target):
    """
    Count ways to assign + or - to each number to reach target.
    Transform: sum(P) - sum(N) = target, sum(P) + sum(N) = total
    So: sum(P) = (target + total) / 2
    """
    total = sum(nums)
    if (target + total) % 2 != 0 or abs(target) > total:
        return 0

    subset_sum = (target + total) // 2

    dp = [0] * (subset_sum + 1)
    dp[0] = 1

    for num in nums:
        for s in range(subset_sum, num - 1, -1):
            dp[s] += dp[s - num]

    return dp[subset_sum]


# ============================================
# PATTERN 5: Last Stone Weight II
# ============================================
def last_stone_weight_ii(stones):
    """
    Smash stones, return smallest possible weight.
    Equivalent to partitioning into two groups with min diff.
    """
    total = sum(stones)
    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for stone in stones:
        for t in range(target, stone - 1, -1):
            dp[t] = dp[t] or dp[t - stone]

    # Find largest achievable sum <= target
    for t in range(target, -1, -1):
        if dp[t]:
            return total - 2 * t

    return total


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 416. Partition Equal Subset Sum
- 494. Target Sum
- 1049. Last Stone Weight II
- 474. Ones and Zeroes (2D knapsack)
- 879. Profitable Schemes

Hard:
- 805. Split Array With Same Average
"""
