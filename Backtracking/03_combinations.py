"""
COMBINATIONS
============

WHEN TO USE:
- Choosing k elements from n elements
- Order doesn't matter (unlike permutations)
- Combination sum problems

KEY INSIGHT: Use start index to avoid duplicates.
For combination sum, can reuse element (i) or not (i+1).

TIME: O(C(n,k) * k)  |  SPACE: O(k) recursion depth
"""

# ============================================
# PATTERN 1: Basic Combinations (n choose k)
# ============================================
def combine(n, k):
    """Generate all combinations of k numbers from [1, n]."""
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return

        # Optimization: need k-len(path) more elements
        for i in range(start, n - (k - len(path)) + 2):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return result


# ============================================
# PATTERN 2: Combination Sum (reuse allowed)
# ============================================
def combination_sum(candidates, target):
    """Find combinations that sum to target. Can reuse elements."""
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])  # i, not i+1 (reuse)
            path.pop()

    backtrack(0, [], target)
    return result


# ============================================
# PATTERN 3: Combination Sum II (no reuse, has duplicates)
# ============================================
def combination_sum2(candidates, target):
    """Each number used once. Candidates may have duplicates."""
    result = []
    candidates.sort()

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            # Skip duplicates at same level
            if i > start and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            backtrack(i + 1, path, remaining - candidates[i])
            path.pop()

    backtrack(0, [], target)
    return result


# ============================================
# PATTERN 4: Combination Sum III (k numbers, sum n)
# ============================================
def combination_sum3(k, n):
    """Find k numbers (1-9) that sum to n. Each used once."""
    result = []

    def backtrack(start, path, remaining):
        if len(path) == k:
            if remaining == 0:
                result.append(path[:])
            return

        for i in range(start, 10):
            if i > remaining:  # Optimization
                break
            path.append(i)
            backtrack(i + 1, path, remaining - i)
            path.pop()

    backtrack(1, [], n)
    return result


# ============================================
# PATTERN 5: Letter Combinations of Phone Number
# ============================================
def letter_combinations(digits):
    """Generate all letter combinations from phone digits."""
    if not digits:
        return []

    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = []

    def backtrack(index, path):
        if index == len(digits):
            result.append(''.join(path))
            return

        for char in mapping[digits[index]]:
            path.append(char)
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return result


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 77. Combinations
- 39. Combination Sum (reuse allowed)
- 40. Combination Sum II (no reuse, duplicates)
- 216. Combination Sum III (k numbers 1-9)
- 17. Letter Combinations of a Phone Number
- 377. Combination Sum IV (DP, count ways)
"""
