"""
PERMUTATIONS
============

WHEN TO USE:
- Generate all orderings of elements
- Arrangement problems
- When order matters

KEY INSIGHT: At each position, try all remaining unused elements.
Backtrack by removing element from path after exploring.

TIME: O(n! * n)  |  SPACE: O(n) recursion depth
"""

# ============================================
# PATTERN 1: Basic Permutations
# ============================================
def permute(nums):
    """Generate all permutations of nums."""
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return

        for i in range(len(remaining)):
            # Choose
            path.append(remaining[i])
            # Explore (exclude chosen element)
            backtrack(path, remaining[:i] + remaining[i+1:])
            # Unchoose
            path.pop()

    backtrack([], nums)
    return result


# ============================================
# PATTERN 2: Permutations with Duplicates
# ============================================
def permute_unique(nums):
    """Permutations when nums may have duplicates."""
    result = []
    nums.sort()  # Important for duplicate handling

    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return

        for i in range(len(remaining)):
            # Skip duplicates at same level
            if i > 0 and remaining[i] == remaining[i-1]:
                continue

            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()

    backtrack([], nums)
    return result


# ============================================
# PATTERN 3: Using Visited Array
# ============================================
def permute_with_visited(nums):
    """Alternative using visited array (more efficient)."""
    result = []
    n = len(nums)
    visited = [False] * n

    def backtrack(path):
        if len(path) == n:
            result.append(path[:])
            return

        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            visited[i] = False

    backtrack([])
    return result


# ============================================
# PATTERN 4: Next Permutation
# ============================================
def next_permutation(nums):
    """
    Modify nums to next lexicographically greater permutation.
    In-place, O(1) extra space.
    """
    n = len(nums)
    i = n - 2

    # Find first decreasing element from right
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Find smallest element larger than nums[i]
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse suffix
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 46. Permutations
- 47. Permutations II (with duplicates)
- 31. Next Permutation
- 60. Permutation Sequence
- 567. Permutation in String (sliding window)
"""
