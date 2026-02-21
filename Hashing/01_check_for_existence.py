"""
CHECK FOR EXISTENCE (Hash Set)
==============================

WHEN TO USE:
- O(1) lookup needed
- Check if element exists
- Track seen elements
- Remove duplicates

KEY INSIGHT: Hash set provides O(1) add/remove/lookup average.
Use when you only need to know "exists or not".

TIME: O(1) average  |  SPACE: O(n)
"""

# ============================================
# PATTERN 1: Contains Duplicate
# ============================================
def contains_duplicate(nums):
    """Check if any value appears at least twice."""
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# ============================================
# PATTERN 2: Missing Number
# ============================================
def missing_number(nums):
    """Find missing number in [0, n]."""
    num_set = set(nums)
    n = len(nums)
    for i in range(n + 1):
        if i not in num_set:
            return i
    return -1

# Alternative: Math approach
def missing_number_math(nums):
    n = len(nums)
    expected = n * (n + 1) // 2
    return expected - sum(nums)


# ============================================
# PATTERN 3: Intersection of Two Arrays
# ============================================
def intersection(nums1, nums2):
    """Return unique elements in both arrays."""
    return list(set(nums1) & set(nums2))


# ============================================
# PATTERN 4: Happy Number
# ============================================
def is_happy(n):
    """
    Check if number is happy (sum of squares of digits eventually = 1).
    Use set to detect cycles.
    """
    def get_next(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1


# ============================================
# PATTERN 5: First Missing Positive
# ============================================
def first_missing_positive(nums):
    """
    Find smallest missing positive integer.
    O(n) time, O(1) space using array as hash set.
    """
    n = len(nums)

    # Place each number in its correct position
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    # Find first position where nums[i] != i + 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


# ============================================
# PATTERN 6: Longest Consecutive Sequence
# ============================================
def longest_consecutive(nums):
    """Find length of longest consecutive sequence."""
    num_set = set(nums)
    max_length = 0

    for num in num_set:
        # Only start counting from sequence start
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            max_length = max(max_length, length)

    return max_length


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 217. Contains Duplicate
- 268. Missing Number
- 349. Intersection of Two Arrays
- 202. Happy Number
- 705. Design HashSet

Medium:
- 128. Longest Consecutive Sequence
- 287. Find the Duplicate Number

Hard:
- 41. First Missing Positive
"""
