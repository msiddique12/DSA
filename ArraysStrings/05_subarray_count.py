"""
SUBARRAY COUNT
==============

WHEN TO USE:
- Count subarrays with specific property
- Count subarrays with sum/product condition
- At most K vs exactly K technique

KEY INSIGHT: exactly(K) = atMost(K) - atMost(K-1)
Use sliding window + prefix sum + hashmap combinations.

TIME: O(n)  |  SPACE: O(n) or O(1)
"""

from collections import defaultdict

# ============================================
# PATTERN 1: Count Subarrays with Sum = K
# ============================================
def subarray_sum_equals_k(nums, k):
    """Count subarrays with sum exactly k."""
    count = 0
    prefix_sum = 0
    seen = {0: 1}  # prefix_sum -> frequency

    for num in nums:
        prefix_sum += num
        # If prefix_sum - k seen before, found subarray
        count += seen.get(prefix_sum - k, 0)
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count


# ============================================
# PATTERN 2: At Most K (Sliding Window)
# ============================================
def subarrays_at_most_k_distinct(nums, k):
    """Count subarrays with at most k distinct elements."""
    if k == 0:
        return 0

    count = defaultdict(int)
    left = 0
    result = 0

    for right in range(len(nums)):
        count[nums[right]] += 1

        while len(count) > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1

        # All subarrays ending at right with start in [left, right]
        result += right - left + 1

    return result


# ============================================
# PATTERN 3: Exactly K = AtMost(K) - AtMost(K-1)
# ============================================
def subarrays_exactly_k_distinct(nums, k):
    """Count subarrays with exactly k distinct elements."""
    return (subarrays_at_most_k_distinct(nums, k) -
            subarrays_at_most_k_distinct(nums, k - 1))


# ============================================
# PATTERN 4: Count Subarrays with Product < K
# ============================================
def num_subarray_product_less_than_k(nums, k):
    """Count subarrays where product < k."""
    if k <= 1:
        return 0

    product = 1
    left = 0
    count = 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product //= nums[left]
            left += 1

        # Subarrays ending at right: [left,right], [left+1,right], ...
        count += right - left + 1

    return count


# ============================================
# PATTERN 5: Count Nice Subarrays (Odd Numbers)
# ============================================
def number_of_subarrays(nums, k):
    """Count subarrays with exactly k odd numbers."""
    # Transform: odd->1, even->0, then find subarrays with sum k
    def at_most(k):
        if k < 0:
            return 0
        count = 0
        left = 0
        odd_count = 0

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd_count += 1

            while odd_count > k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1

            count += right - left + 1

        return count

    return at_most(k) - at_most(k - 1)


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 560. Subarray Sum Equals K
- 713. Subarray Product Less Than K
- 992. Subarrays with K Different Integers
- 1248. Count Number of Nice Subarrays
- 930. Binary Subarrays With Sum
- 1074. Number of Submatrices That Sum to Target
"""
