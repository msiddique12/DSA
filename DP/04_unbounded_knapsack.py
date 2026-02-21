"""
UNBOUNDED KNAPSACK
==================

WHEN TO USE:
- Can use items unlimited times
- Coin change problems
- Rod cutting
- Ribbon cutting

KEY INSIGHT: Unlike 0/1, can reuse items.
Iterate capacity forward (not backward).

TIME: O(n*W)  |  SPACE: O(W)
"""

# ============================================
# PATTERN 1: Coin Change (Min Coins)
# ============================================
def coin_change(coins, amount):
    """Minimum coins to make amount. Return -1 if impossible."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


# ============================================
# PATTERN 2: Coin Change II (Count Ways)
# ============================================
def coin_change_ways(coins, amount):
    """Number of combinations to make amount."""
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]

    return dp[amount]


# ============================================
# PATTERN 3: Rod Cutting (Max Value)
# ============================================
def rod_cutting(prices, n):
    """Maximum value from cutting rod of length n. prices[i] = price of length i+1."""
    dp = [0] * (n + 1)

    for length in range(1, n + 1):
        for cut in range(1, length + 1):
            dp[length] = max(dp[length], prices[cut - 1] + dp[length - cut])

    return dp[n]


# ============================================
# PATTERN 4: Perfect Squares
# ============================================
def num_squares(n):
    """Minimum perfect squares that sum to n."""
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    # Generate squares up to n
    squares = []
    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1

    for square in squares:
        for num in range(square, n + 1):
            dp[num] = min(dp[num], dp[num - square] + 1)

    return dp[n]


# ============================================
# PATTERN 5: Combination Sum IV (Order Matters)
# ============================================
def combination_sum_iv(nums, target):
    """
    Count permutations that sum to target.
    Note: Different order = different combination.
    """
    dp = [0] * (target + 1)
    dp[0] = 1

    for t in range(1, target + 1):
        for num in nums:
            if num <= t:
                dp[t] += dp[t - num]

    return dp[target]


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 322. Coin Change
- 518. Coin Change 2
- 279. Perfect Squares
- 377. Combination Sum IV
- 983. Minimum Cost For Tickets

Hard:
- (Rod cutting not on LeetCode)
"""
