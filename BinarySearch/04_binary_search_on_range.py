"""
BINARY SEARCH ON ANSWER RANGE
=============================

WHEN TO USE:
- "Minimum maximum" or "Maximum minimum" problems
- Find smallest/largest value that satisfies condition
- When answer is in a known range

KEY INSIGHT: Binary search on the answer space, not the array.
Check if a candidate answer is valid using a helper function.

TIME: O(n * log(range))  |  SPACE: O(1)
"""

# ============================================
# PATTERN 1: Capacity to Ship Packages (Min Max)
# ============================================
def ship_within_days(weights, days):
    """
    Minimum ship capacity to ship all packages within 'days' days.
    Ship must carry packages in order.
    """
    def can_ship(capacity):
        current_weight = 0
        days_needed = 1
        for w in weights:
            if current_weight + w > capacity:
                days_needed += 1
                current_weight = 0
            current_weight += w
        return days_needed <= days

    left = max(weights)      # At least max weight
    right = sum(weights)     # At most all weights

    while left < right:
        mid = left + (right - left) // 2
        if can_ship(mid):
            right = mid      # Try smaller
        else:
            left = mid + 1   # Need larger

    return left


# ============================================
# PATTERN 2: Split Array Largest Sum
# ============================================
def split_array(nums, k):
    """
    Split array into k subarrays.
    Minimize the largest sum among them.
    """
    def can_split(max_sum):
        count = 1
        current_sum = 0
        for num in nums:
            if current_sum + num > max_sum:
                count += 1
                current_sum = 0
            current_sum += num
        return count <= k

    left = max(nums)
    right = sum(nums)

    while left < right:
        mid = left + (right - left) // 2
        if can_split(mid):
            right = mid
        else:
            left = mid + 1

    return left


# ============================================
# PATTERN 3: Koko Eating Bananas
# ============================================
def min_eating_speed(piles, h):
    """
    Minimum eating speed to eat all bananas within h hours.
    Each pile takes ceil(pile/speed) hours.
    """
    import math

    def can_finish(speed):
        hours = sum(math.ceil(pile / speed) for pile in piles)
        return hours <= h

    left = 1
    right = max(piles)

    while left < right:
        mid = left + (right - left) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1

    return left


# ============================================
# PATTERN 4: Magnetic Force (Max Min)
# ============================================
def max_distance(positions, m):
    """
    Place m balls to maximize minimum distance between any two.
    """
    positions.sort()

    def can_place(min_dist):
        count = 1
        last_pos = positions[0]
        for pos in positions[1:]:
            if pos - last_pos >= min_dist:
                count += 1
                last_pos = pos
        return count >= m

    left = 1
    right = positions[-1] - positions[0]

    while left < right:
        mid = left + (right - left + 1) // 2  # Bias right for max
        if can_place(mid):
            left = mid       # Try larger
        else:
            right = mid - 1  # Too large

    return left


# ============================================
# PATTERN 5: Find Smallest Divisor
# ============================================
def smallest_divisor(nums, threshold):
    """
    Find smallest divisor such that sum of ceil(nums[i]/divisor) <= threshold.
    """
    import math

    def compute_sum(divisor):
        return sum(math.ceil(num / divisor) for num in nums)

    left = 1
    right = max(nums)

    while left < right:
        mid = left + (right - left) // 2
        if compute_sum(mid) <= threshold:
            right = mid
        else:
            left = mid + 1

    return left


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 875. Koko Eating Bananas
- 1011. Capacity To Ship Packages Within D Days
- 1283. Find the Smallest Divisor Given a Threshold
- 1482. Minimum Number of Days to Make m Bouquets
- 1552. Magnetic Force Between Two Balls

Hard:
- 410. Split Array Largest Sum
- 774. Minimize Max Distance to Gas Station
"""
