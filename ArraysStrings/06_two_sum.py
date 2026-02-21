"""
TWO SUM VARIANTS
================

WHEN TO USE:
- Finding pairs with target sum
- Unsorted array → use hashmap
- Sorted array → use two pointers
- Multiple solutions → track all

KEY INSIGHT: For each element x, look for (target - x) in hashmap.

TIME: O(n)  |  SPACE: O(n)
"""

from collections import defaultdict

# ============================================
# PATTERN 1: Basic Two Sum (Hashmap)
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
# PATTERN 2: Two Sum - Sorted Array
# ============================================
def two_sum_sorted(nums, target):
    """Two pointers for sorted array."""
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left + 1, right + 1]  # 1-indexed
        elif total < target:
            left += 1
        else:
            right -= 1

    return []


# ============================================
# PATTERN 3: Two Sum - Count Pairs
# ============================================
def count_pairs(nums, target):
    """Count all pairs that sum to target."""
    count = 0
    seen = defaultdict(int)

    for num in nums:
        complement = target - num
        count += seen[complement]
        seen[num] += 1

    return count


# ============================================
# PATTERN 4: Two Sum - All Unique Pairs
# ============================================
def all_unique_pairs(nums, target):
    """Find all unique pairs (values, not indices)."""
    seen = set()
    used = set()
    result = []

    for num in nums:
        complement = target - num
        if complement in seen and (min(num, complement), max(num, complement)) not in used:
            pair = (min(num, complement), max(num, complement))
            result.append(list(pair))
            used.add(pair)
        seen.add(num)

    return result


# ============================================
# PATTERN 5: Two Sum - Data Structure Design
# ============================================
class TwoSum:
    """Design a data structure for two sum queries."""
    def __init__(self):
        self.nums = defaultdict(int)

    def add(self, number):
        self.nums[number] += 1

    def find(self, value):
        for num in self.nums:
            complement = value - num
            if complement in self.nums:
                if complement != num or self.nums[num] > 1:
                    return True
        return False


# ============================================
# PATTERN 6: Four Sum Count (Two Arrays Each)
# ============================================
def four_sum_count(A, B, C, D):
    """Count tuples where A[i]+B[j]+C[k]+D[l]=0."""
    # Combine A+B sums, then look for -(C+D)
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
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 1. Two Sum
- 167. Two Sum II (sorted)
- 170. Two Sum III - Data structure design

Medium:
- 15. 3Sum (sort + two pointers)
- 18. 4Sum
- 454. 4Sum II (four arrays)
- 653. Two Sum IV - BST input

Hard:
- Related: 923. 3Sum With Multiplicity
"""
