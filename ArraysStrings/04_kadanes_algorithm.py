"""
KADANE'S ALGORITHM
==================

WHEN TO USE:
- Maximum subarray sum
- Maximum product subarray
- Circular array max sum
- Buy/sell stock problems

KEY INSIGHT: At each position, decide: extend current subarray or start new.
current_max = max(nums[i], current_max + nums[i])

TIME: O(n)  |  SPACE: O(1)
"""

# ============================================
# PATTERN 1: Maximum Subarray Sum
# ============================================
def max_subarray(nums):
    """Find contiguous subarray with largest sum."""
    current_max = global_max = nums[0]

    for num in nums[1:]:
        current_max = max(num, current_max + num)  # Extend or start new
        global_max = max(global_max, current_max)

    return global_max


# ============================================
# PATTERN 2: Maximum Product Subarray
# ============================================
def max_product(nums):
    """Maximum product of contiguous subarray."""
    # Track both max and min (negative * negative = positive)
    max_prod = min_prod = result = nums[0]

    for num in nums[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod  # Swap

        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        result = max(result, max_prod)

    return result


# ============================================
# PATTERN 3: Circular Array Max Sum
# ============================================
def max_subarray_circular(nums):
    """Max subarray sum in circular array."""
    total = sum(nums)

    # Case 1: Max subarray doesn't wrap
    max_kadane = max_subarray(nums)

    # Case 2: Max subarray wraps (= total - min subarray)
    # Find min subarray using Kadane with min
    current_min = global_min = nums[0]
    for num in nums[1:]:
        current_min = min(num, current_min + num)
        global_min = min(global_min, current_min)

    # If all negative, max_kadane is the answer
    if total == global_min:
        return max_kadane

    return max(max_kadane, total - global_min)


# ============================================
# PATTERN 4: Best Time to Buy and Sell Stock
# ============================================
def max_profit(prices):
    """Maximum profit from one buy-sell transaction."""
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


# ============================================
# PATTERN 5: Get Indices of Max Subarray
# ============================================
def max_subarray_indices(nums):
    """Return (start, end, sum) of max subarray."""
    current_max = global_max = nums[0]
    start = end = temp_start = 0

    for i, num in enumerate(nums[1:], 1):
        if num > current_max + num:
            current_max = num
            temp_start = i  # Start new subarray
        else:
            current_max = current_max + num

        if current_max > global_max:
            global_max = current_max
            start = temp_start
            end = i

    return start, end, global_max


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 121. Best Time to Buy and Sell Stock

Medium:
- 53. Maximum Subarray
- 152. Maximum Product Subarray
- 918. Maximum Sum Circular Subarray
- 122. Best Time to Buy and Sell Stock II (multiple transactions)

Hard:
- 123. Best Time to Buy and Sell Stock III (at most 2 transactions)
- 188. Best Time to Buy and Sell Stock IV (at most k transactions)
"""
