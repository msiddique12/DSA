"""
SUBSETS (Power Set)
==================

WHEN TO USE:
- Generate all subsets/combinations
- Include/exclude decisions
- Power set problems

KEY INSIGHT: For each element, choose to include or not include.
OR: At each step, try adding each remaining element.

TIME: O(2^n * n)  |  SPACE: O(n) recursion depth
"""

# ============================================
# PATTERN 1: Subsets (Include/Exclude)
# ============================================
def subsets_v1(nums):
    """Generate all subsets using include/exclude."""
    result = []

    def backtrack(index, path):
        if index == len(nums):
            result.append(path[:])
            return

        # Exclude nums[index]
        backtrack(index + 1, path)

        # Include nums[index]
        path.append(nums[index])
        backtrack(index + 1, path)
        path.pop()

    backtrack(0, [])
    return result


# ============================================
# PATTERN 2: Subsets (Iterative)
# ============================================
def subsets_v2(nums):
    """Generate all subsets iteratively."""
    result = [[]]

    for num in nums:
        # Add num to all existing subsets
        result += [subset + [num] for subset in result]

    return result


# ============================================
# PATTERN 3: Subsets (Cascading with loop)
# ============================================
def subsets_v3(nums):
    """Backtracking with loop - good for subsets of specific size."""
    result = []

    def backtrack(start, path):
        result.append(path[:])  # Add every path (not just leaves)

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)  # i+1, not start+1!
            path.pop()

    backtrack(0, [])
    return result


# ============================================
# PATTERN 4: Subsets with Duplicates
# ============================================
def subsets_with_dup(nums):
    """Subsets when nums may have duplicates."""
    result = []
    nums.sort()  # Important!

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            # Skip duplicates at same level
            if i > start and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


# ============================================
# PATTERN 5: Subsets of Size K
# ============================================
def subsets_of_size_k(nums, k):
    """Generate all subsets of exactly size k."""
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return

        # Optimization: can't reach size k
        if len(path) + (len(nums) - start) < k:
            return

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 78. Subsets
- 90. Subsets II (with duplicates)
- 77. Combinations (subsets of size k)
- 784. Letter Case Permutation
- 1239. Maximum Length of Concatenated String
"""
