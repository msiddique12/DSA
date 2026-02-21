"""
LONGEST INCREASING SUBSEQUENCE (LIS)
====================================

WHEN TO USE:
- Finding longest sorted subsequence
- Box stacking, envelope nesting
- Chain problems

KEY INSIGHT: For each element, find longest LIS ending before it.
O(n^2) DP or O(n log n) with binary search.

TIME: O(n^2) DP, O(n log n) optimal  |  SPACE: O(n)
"""

import bisect

# ============================================
# PATTERN 1: LIS (O(n^2) DP)
# ============================================
def lis_dp(nums):
    """Find length of longest increasing subsequence."""
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # dp[i] = LIS ending at i

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# ============================================
# PATTERN 2: LIS (O(n log n) with Binary Search)
# ============================================
def lis_binary_search(nums):
    """
    Maintain array of smallest tail of LIS of each length.
    Use binary search to find position.
    """
    if not nums:
        return 0

    tails = []  # tails[i] = smallest tail of LIS of length i+1

    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)


# ============================================
# PATTERN 3: LIS - Get Actual Sequence
# ============================================
def lis_sequence(nums):
    """Return one of the longest increasing subsequences."""
    if not nums:
        return []

    n = len(nums)
    dp = [1] * n
    parent = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    # Find index of max length
    max_idx = max(range(n), key=lambda x: dp[x])

    # Reconstruct
    result = []
    while max_idx != -1:
        result.append(nums[max_idx])
        max_idx = parent[max_idx]

    return result[::-1]


# ============================================
# PATTERN 4: Number of LIS
# ============================================
def find_number_of_lis(nums):
    """Count number of longest increasing subsequences."""
    if not nums:
        return 0

    n = len(nums)
    length = [1] * n   # length[i] = LIS ending at i
    count = [1] * n    # count[i] = number of LIS ending at i

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]

    max_len = max(length)
    return sum(c for l, c in zip(length, count) if l == max_len)


# ============================================
# PATTERN 5: Russian Doll Envelopes
# ============================================
def max_envelopes(envelopes):
    """
    Max envelopes you can nest (both width and height must be larger).
    Sort by width asc, then height desc, then LIS on heights.
    """
    if not envelopes:
        return 0

    # Sort: width ascending, height descending
    envelopes.sort(key=lambda x: (x[0], -x[1]))

    # LIS on heights
    heights = [e[1] for e in envelopes]
    return lis_binary_search(heights)


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 300. Longest Increasing Subsequence
- 673. Number of Longest Increasing Subsequence
- 646. Maximum Length of Pair Chain
- 1218. Longest Arithmetic Subsequence of Given Difference

Hard:
- 354. Russian Doll Envelopes
- 1691. Maximum Height by Stacking Cuboids
"""
