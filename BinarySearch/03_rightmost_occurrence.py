"""
RIGHTMOST/LEFTMOST OCCURRENCE
=============================

WHEN TO USE:
- Finding boundaries in sorted arrays
- Floor/ceiling of a number
- Count occurrences

KEY INSIGHT: Don't stop when found, keep searching.
For rightmost: keep left = mid + 1 when equal
For leftmost: keep right = mid - 1 when equal

TIME: O(log n)  |  SPACE: O(1)
"""

# ============================================
# PATTERN 1: Leftmost (First) Occurrence
# ============================================
def leftmost(nums, target):
    """Find first occurrence of target."""
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


# ============================================
# PATTERN 2: Rightmost (Last) Occurrence
# ============================================
def rightmost(nums, target):
    """Find last occurrence of target."""
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


# ============================================
# PATTERN 3: Floor (Largest <= target)
# ============================================
def floor(nums, target):
    """Find largest element <= target."""
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] <= target:
            result = mid
            left = mid + 1  # Try to find larger
        else:
            right = mid - 1

    return result


# ============================================
# PATTERN 4: Ceiling (Smallest >= target)
# ============================================
def ceiling(nums, target):
    """Find smallest element >= target."""
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            result = mid
            right = mid - 1  # Try to find smaller
        else:
            left = mid + 1

    return result


# ============================================
# PATTERN 5: Count Occurrences
# ============================================
def count_occurrences(nums, target):
    """Count how many times target appears."""
    first = leftmost(nums, target)
    if first == -1:
        return 0
    last = rightmost(nums, target)
    return last - first + 1


# ============================================
# PATTERN 6: Single Element in Sorted Array
# ============================================
def single_non_duplicate(nums):
    """
    Array has pairs except one single element.
    Find the single one.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Ensure mid is even for pair comparison
        if mid % 2 == 1:
            mid -= 1

        if nums[mid] == nums[mid + 1]:
            left = mid + 2  # Single is to the right
        else:
            right = mid     # Single is mid or to the left

    return nums[left]


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 278. First Bad Version

Medium:
- 34. Find First and Last Position
- 540. Single Element in a Sorted Array
- 275. H-Index II
"""
