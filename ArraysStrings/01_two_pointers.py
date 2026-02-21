"""
TWO POINTERS
============

WHEN TO USE:
- Sorted array problems
- Pair/triplet with target sum
- Removing duplicates in-place
- Reversing, palindrome checking
- Merging sorted arrays

KEY INSIGHT: Two pointers moving toward each other or same direction.

TIME: O(n)  |  SPACE: O(1)
"""

# ============================================
# PATTERN 1: Opposite Ends (Target Sum)
# ============================================
def two_sum_sorted(nums, target):
    """For SORTED array. Use hashmap for unsorted."""
    left, right = 0, len(nums) - 1

    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return []


# ============================================
# PATTERN 2: Three Sum
# ============================================
def three_sum(nums):
    """Find all unique triplets that sum to zero."""
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:  # Skip duplicates
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1  # Skip duplicates
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# ============================================
# PATTERN 3: Remove Duplicates In-Place
# ============================================
def remove_duplicates(nums):
    """Remove duplicates from sorted array, return new length."""
    if not nums:
        return 0

    write = 1  # Position to write next unique element
    for read in range(1, len(nums)):
        if nums[read] != nums[read-1]:
            nums[write] = nums[read]
            write += 1

    return write


# ============================================
# PATTERN 4: Container With Most Water
# ============================================
def max_area(heights):
    """Maximize area between two lines."""
    left, right = 0, len(heights) - 1
    max_water = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        max_water = max(max_water, width * height)

        # Move the shorter line (might find taller)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water


# ============================================
# PATTERN 5: Is Palindrome
# ============================================
def is_palindrome(s):
    """Check if string is palindrome (alphanumeric only)."""
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 167. Two Sum II (sorted)
- 26. Remove Duplicates from Sorted Array
- 125. Valid Palindrome
- 283. Move Zeroes
- 88. Merge Sorted Array

Medium:
- 15. 3Sum
- 11. Container With Most Water
- 16. 3Sum Closest
- 75. Sort Colors (Dutch flag)
- 18. 4Sum
"""
