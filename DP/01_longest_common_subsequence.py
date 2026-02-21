"""
LONGEST COMMON SUBSEQUENCE (LCS)
================================

WHEN TO USE:
- Comparing two sequences
- Edit distance problems
- Diff algorithms
- DNA sequence matching

KEY INSIGHT: If chars match, 1 + LCS(remaining). Else max of skip either char.

TIME: O(m*n)  |  SPACE: O(m*n) or O(min(m,n)) optimized
"""

# ============================================
# PATTERN 1: LCS Length
# ============================================
def lcs_length(text1, text2):
    """Find length of longest common subsequence."""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]


# ============================================
# PATTERN 2: LCS String (Reconstruct)
# ============================================
def lcs_string(text1, text2):
    """Reconstruct the actual LCS string."""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Backtrack to find the string
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            result.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(result))


# ============================================
# PATTERN 3: Edit Distance (Levenshtein)
# ============================================
def min_distance(word1, word2):
    """Minimum operations (insert, delete, replace) to convert word1 to word2."""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],      # Delete
                    dp[i][j-1],      # Insert
                    dp[i-1][j-1]     # Replace
                )

    return dp[m][n]


# ============================================
# PATTERN 4: Longest Palindromic Subsequence
# ============================================
def longest_palindrome_subseq(s):
    """LPS = LCS(s, reverse(s))"""
    return lcs_length(s, s[::-1])


# ============================================
# PATTERN 5: Space Optimized LCS
# ============================================
def lcs_optimized(text1, text2):
    """O(min(m,n)) space."""
    if len(text1) < len(text2):
        text1, text2 = text2, text1

    prev = [0] * (len(text2) + 1)
    curr = [0] * (len(text2) + 1)

    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i-1] == text2[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev, curr = curr, [0] * (len(text2) + 1)

    return prev[len(text2)]


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 1143. Longest Common Subsequence
- 72. Edit Distance
- 583. Delete Operation for Two Strings
- 712. Minimum ASCII Delete Sum

Hard:
- 516. Longest Palindromic Subsequence
- 1312. Minimum Insertion Steps to Make String Palindrome
"""
