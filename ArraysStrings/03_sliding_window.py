"""
SLIDING WINDOW
==============

WHEN TO USE:
- Substring/subarray problems
- Maximum/minimum in window of size k
- Longest substring with condition
- Anagram finding

KEY INSIGHT: Expand right, shrink left when condition violated.
Use hashmap to track window contents.

TIME: O(n)  |  SPACE: O(k) for window contents
"""

from collections import Counter, defaultdict

# ============================================
# PATTERN 1: Fixed Window Size
# ============================================
def max_sum_subarray(nums, k):
    """Maximum sum of subarray with size k."""
    if len(nums) < k:
        return 0

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]  # Slide: add right, remove left
        max_sum = max(max_sum, window_sum)

    return max_sum


# ============================================
# PATTERN 2: Variable Window - Longest Valid
# ============================================
def length_of_longest_substring(s):
    """Longest substring without repeating characters."""
    seen = {}  # char -> last index
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1  # Shrink window
        seen[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


# ============================================
# PATTERN 3: Longest with At Most K Distinct
# ============================================
def longest_k_distinct(s, k):
    """Longest substring with at most k distinct characters."""
    char_count = defaultdict(int)
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        char_count[char] += 1

        while len(char_count) > k:  # Shrink when > k distinct
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# ============================================
# PATTERN 4: Minimum Window Substring
# ============================================
def min_window(s, t):
    """Minimum window containing all chars of t."""
    if not t or not s:
        return ""

    need = Counter(t)
    have = defaultdict(int)
    required = len(need)
    formed = 0

    left = 0
    min_len = float('inf')
    result = ""

    for right, char in enumerate(s):
        have[char] += 1
        if char in need and have[char] == need[char]:
            formed += 1

        # Shrink while valid
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right+1]

            have[s[left]] -= 1
            if s[left] in need and have[s[left]] < need[s[left]]:
                formed -= 1
            left += 1

    return result


# ============================================
# PATTERN 5: Find All Anagrams
# ============================================
def find_anagrams(s, p):
    """Find all start indices of p's anagrams in s."""
    if len(p) > len(s):
        return []

    p_count = Counter(p)
    s_count = Counter(s[:len(p)])
    result = []

    if s_count == p_count:
        result.append(0)

    for i in range(len(p), len(s)):
        # Add new char
        s_count[s[i]] += 1
        # Remove old char
        old = s[i - len(p)]
        s_count[old] -= 1
        if s_count[old] == 0:
            del s_count[old]

        if s_count == p_count:
            result.append(i - len(p) + 1)

    return result


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 643. Maximum Average Subarray I

Medium:
- 3. Longest Substring Without Repeating Characters
- 424. Longest Repeating Character Replacement
- 567. Permutation in String
- 438. Find All Anagrams in String
- 209. Minimum Size Subarray Sum
- 1004. Max Consecutive Ones III

Hard:
- 76. Minimum Window Substring
- 239. Sliding Window Maximum (use deque)
- 30. Substring with Concatenation of All Words
"""
