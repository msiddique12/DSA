"""
PAIR SUM PROBLEMS
=================

WHEN TO USE:
- Finding pairs that sum to target
- Two sum and variations
- Subarray sum problems

KEY INSIGHT: For target sum, store complement in hash map.
complement = target - current

TIME: O(n)  |  SPACE: O(n)
"""

from collections import defaultdict, Counter

# ============================================
# PATTERN 1: Two Sum
# ============================================
def two_sum(nums, target):
    """Return indices of two numbers that sum to target."""
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []


# ============================================
# PATTERN 2: Two Sum - Count Pairs
# ============================================
def count_pairs(nums, target):
    """Count pairs that sum to target."""
    seen = defaultdict(int)
    count = 0

    for num in nums:
        complement = target - num
        count += seen[complement]
        seen[num] += 1

    return count


# ============================================
# PATTERN 3: Subarray Sum Equals K
# ============================================
def subarray_sum(nums, k):
    """Count subarrays with sum = k."""
    count = 0
    prefix_sum = 0
    seen = {0: 1}  # prefix_sum -> frequency

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in seen:
            count += seen[prefix_sum - k]
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count


# ============================================
# PATTERN 4: Continuous Subarray Sum (Multiple of K)
# ============================================
def check_subarray_sum(nums, k):
    """
    Check if subarray of size >= 2 sums to multiple of k.
    If prefix_sum[i] % k == prefix_sum[j] % k, then
    subarray (i, j] sums to multiple of k.
    """
    seen = {0: -1}  # remainder -> index
    prefix_sum = 0

    for i, num in enumerate(nums):
        prefix_sum += num
        remainder = prefix_sum % k if k != 0 else prefix_sum

        if remainder in seen:
            if i - seen[remainder] >= 2:
                return True
        else:
            seen[remainder] = i

    return False


# ============================================
# PATTERN 5: Four Sum Count
# ============================================
def four_sum_count(A, B, C, D):
    """Count tuples where A[i]+B[j]+C[k]+D[l]=0."""
    ab_sum = defaultdict(int)

    for a in A:
        for b in B:
            ab_sum[a + b] += 1

    count = 0
    for c in C:
        for d in D:
            count += ab_sum[-(c + d)]

    return count


# ============================================
# PATTERN 6: Number of Good Pairs
# ============================================
def num_identical_pairs(nums):
    """Count pairs (i, j) where nums[i] == nums[j] and i < j."""
    count = Counter(nums)
    result = 0

    for c in count.values():
        result += c * (c - 1) // 2  # nC2

    return result


# ============================================
# PATTERN 7: Find Pairs with Given Difference
# ============================================
def find_pairs(nums, k):
    """Count unique pairs with difference k."""
    if k < 0:
        return 0

    count = Counter(nums)

    if k == 0:
        return sum(1 for c in count.values() if c > 1)

    result = 0
    for num in count:
        if num + k in count:
            result += 1

    return result


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 1. Two Sum
- 1512. Number of Good Pairs
- 532. K-diff Pairs in an Array

Medium:
- 560. Subarray Sum Equals K
- 523. Continuous Subarray Sum
- 454. 4Sum II
- 974. Subarray Sums Divisible by K

Hard:
- 149. Max Points on a Line
"""
