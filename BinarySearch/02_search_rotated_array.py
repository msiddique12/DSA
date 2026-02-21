"""
SEARCH IN ROTATED SORTED ARRAY
==============================

WHEN TO USE:
- Rotated sorted array
- Find element or minimum
- Still maintain O(log n)

KEY INSIGHT: One half is always sorted.
Determine which half is sorted, check if target is there.

TIME: O(log n)  |  SPACE: O(1)
"""

# ============================================
# PATTERN 1: Search in Rotated Array
# ============================================
def search(nums, target):
    """Search in rotated sorted array (no duplicates)."""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# ============================================
# PATTERN 2: Search with Duplicates
# ============================================
def search_with_duplicates(nums, target):
    """Search in rotated array with duplicates."""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return True

        # Handle duplicates: can't determine sorted side
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        # Left half is sorted
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return False


# ============================================
# PATTERN 3: Find Minimum
# ============================================
def find_min(nums):
    """Find minimum in rotated sorted array."""
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        # If mid > right, minimum is in right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


# ============================================
# PATTERN 4: Find Minimum with Duplicates
# ============================================
def find_min_with_duplicates(nums):
    """Find minimum with duplicates."""
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right -= 1  # Can't determine, shrink

    return nums[left]


# ============================================
# PATTERN 5: Find Rotation Count
# ============================================
def find_rotation_count(nums):
    """Find how many times array was rotated."""
    # Rotation count = index of minimum element
    return find_min_index(nums)

def find_min_index(nums):
    """Return index of minimum element."""
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return left


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 33. Search in Rotated Sorted Array
- 81. Search in Rotated Sorted Array II (duplicates)
- 153. Find Minimum in Rotated Sorted Array

Hard:
- 154. Find Minimum in Rotated Sorted Array II
"""
