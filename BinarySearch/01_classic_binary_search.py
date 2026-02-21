"""
CLASSIC BINARY SEARCH
=====================

WHEN TO USE:
- Sorted array
- Finding exact element
- O(log n) lookup needed

KEY INSIGHT: Compare with middle, eliminate half each time.
Watch out for off-by-one errors!

TIME: O(log n)  |  SPACE: O(1)
"""

# ============================================
# PATTERN 1: Basic Binary Search
# ============================================
def binary_search(nums, target):
    """Return index of target, or -1 if not found."""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ============================================
# PATTERN 2: First/Last Position (bisect_left)
# ============================================
def search_range(nums, target):
    """Find first and last position of target."""
    def find_first():
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1  # Keep searching left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    def find_last():
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result = mid
                left = mid + 1  # Keep searching right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    return [find_first(), find_last()]


# ============================================
# PATTERN 3: Insert Position
# ============================================
def search_insert(nums, target):
    """Find index to insert target to keep sorted."""
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


# ============================================
# PATTERN 4: Using Python bisect
# ============================================
import bisect

def bisect_examples(nums, target):
    """
    bisect_left: index where target would go (leftmost)
    bisect_right: index after rightmost target
    """
    left_pos = bisect.bisect_left(nums, target)   # First >= target
    right_pos = bisect.bisect_right(nums, target) # First > target

    # Count occurrences of target
    count = right_pos - left_pos

    # Check if target exists
    exists = left_pos < len(nums) and nums[left_pos] == target

    return left_pos, right_pos, count, exists


# ============================================
# PATTERN 5: Peak Index in Mountain Array
# ============================================
def peak_index_in_mountain(arr):
    """Find peak in mountain array (increasing then decreasing)."""
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1  # Peak is to the right
        else:
            right = mid     # Peak is mid or to the left

    return left


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 704. Binary Search
- 35. Search Insert Position
- 852. Peak Index in a Mountain Array

Medium:
- 34. Find First and Last Position
- 162. Find Peak Element
- 153. Find Minimum in Rotated Sorted Array
"""
