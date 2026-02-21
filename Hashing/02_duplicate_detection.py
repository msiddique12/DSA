"""
DUPLICATE DETECTION (Hash Map)
==============================

WHEN TO USE:
- Find duplicates with specific conditions
- Count frequencies
- Track element properties (index, count)

KEY INSIGHT: Hash map stores key-value pairs.
Use to count occurrences or track additional info.

TIME: O(1) average per operation  |  SPACE: O(n)
"""

from collections import Counter, defaultdict

# ============================================
# PATTERN 1: Contains Duplicate II (Within K)
# ============================================
def contains_nearby_duplicate(nums, k):
    """Check if duplicate exists within k indices."""
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i

    return False


# ============================================
# PATTERN 2: Contains Duplicate III (Within K, Value Diff)
# ============================================
def contains_nearby_almost_duplicate(nums, index_diff, value_diff):
    """
    Check if nums[i] - nums[j] <= value_diff
    and abs(i - j) <= index_diff.
    Use bucket sort idea.
    """
    if value_diff < 0:
        return False

    buckets = {}
    w = value_diff + 1  # Bucket width

    for i, num in enumerate(nums):
        bucket_id = num // w

        if bucket_id in buckets:
            return True
        if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= value_diff:
            return True
        if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= value_diff:
            return True

        buckets[bucket_id] = num

        # Maintain sliding window
        if i >= index_diff:
            del buckets[nums[i - index_diff] // w]

    return False


# ============================================
# PATTERN 3: Find All Duplicates
# ============================================
def find_duplicates(nums):
    """Find all elements that appear twice. O(1) extra space."""
    result = []

    for num in nums:
        idx = abs(num) - 1
        if nums[idx] < 0:
            result.append(abs(num))
        else:
            nums[idx] = -nums[idx]

    return result


# ============================================
# PATTERN 4: Single Number (XOR)
# ============================================
def single_number(nums):
    """Find element appearing once (others appear twice)."""
    result = 0
    for num in nums:
        result ^= num
    return result


# ============================================
# PATTERN 5: Single Number III (Two Singles)
# ============================================
def single_number_iii(nums):
    """Find two elements appearing once (others appear twice)."""
    # XOR all = a ^ b (the two singles)
    xor_all = 0
    for num in nums:
        xor_all ^= num

    # Find rightmost set bit (where a and b differ)
    diff_bit = xor_all & (-xor_all)

    # Partition by this bit
    a = b = 0
    for num in nums:
        if num & diff_bit:
            a ^= num
        else:
            b ^= num

    return [a, b]


# ============================================
# PATTERN 6: Group Anagrams
# ============================================
def group_anagrams(strs):
    """Group strings that are anagrams of each other."""
    groups = defaultdict(list)

    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)

    return list(groups.values())


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 136. Single Number
- 242. Valid Anagram
- 383. Ransom Note

Medium:
- 219. Contains Duplicate II
- 49. Group Anagrams
- 442. Find All Duplicates in Array
- 260. Single Number III

Hard:
- 220. Contains Duplicate III
"""
