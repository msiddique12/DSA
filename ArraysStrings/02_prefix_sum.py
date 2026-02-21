"""
PREFIX SUM
==========

WHEN TO USE:
- Range sum queries
- Subarray sum equals k
- Product except self
- Finding equilibrium index

KEY INSIGHT: prefix[i] = sum of elements from 0 to i-1.
Range sum [i,j] = prefix[j+1] - prefix[i]

TIME: O(n) build, O(1) query  |  SPACE: O(n)
"""

# ============================================
# PATTERN 1: Build Prefix Sum Array
# ============================================
def build_prefix_sum(nums):
    """prefix[i] = sum of nums[0:i]"""
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)
    return prefix

def range_sum(prefix, i, j):
    """Sum of nums[i:j+1] inclusive"""
    return prefix[j + 1] - prefix[i]


# ============================================
# PATTERN 2: Subarray Sum Equals K
# ============================================
def subarray_sum(nums, k):
    """Count subarrays with sum = k."""
    count = 0
    prefix_sum = 0
    seen = {0: 1}  # prefix_sum -> count

    for num in nums:
        prefix_sum += num
        # If (prefix_sum - k) exists, found subarray with sum k
        if prefix_sum - k in seen:
            count += seen[prefix_sum - k]
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count


# ============================================
# PATTERN 3: Product Except Self
# ============================================
def product_except_self(nums):
    """Product of all elements except self, without division."""
    n = len(nums)
    result = [1] * n

    # Left products
    left = 1
    for i in range(n):
        result[i] = left
        left *= nums[i]

    # Right products
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= nums[i]

    return result


# ============================================
# PATTERN 4: Contiguous Array (Equal 0s and 1s)
# ============================================
def find_max_length(nums):
    """Longest subarray with equal 0s and 1s."""
    # Treat 0 as -1, find longest subarray with sum 0
    max_len = 0
    prefix_sum = 0
    seen = {0: -1}  # prefix_sum -> first index

    for i, num in enumerate(nums):
        prefix_sum += 1 if num == 1 else -1

        if prefix_sum in seen:
            max_len = max(max_len, i - seen[prefix_sum])
        else:
            seen[prefix_sum] = i

    return max_len


# ============================================
# PATTERN 5: 2D Prefix Sum (Range Sum Query)
# ============================================
class NumMatrix:
    def __init__(self, matrix):
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                self.prefix[i+1][j+1] = (matrix[i][j] +
                                          self.prefix[i][j+1] +
                                          self.prefix[i+1][j] -
                                          self.prefix[i][j])

    def sumRegion(self, r1, c1, r2, c2):
        return (self.prefix[r2+1][c2+1] -
                self.prefix[r1][c2+1] -
                self.prefix[r2+1][c1] +
                self.prefix[r1][c1])


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 303. Range Sum Query - Immutable
- 724. Find Pivot Index

Medium:
- 560. Subarray Sum Equals K
- 238. Product of Array Except Self
- 525. Contiguous Array
- 304. Range Sum Query 2D - Immutable
- 974. Subarray Sums Divisible by K
"""
