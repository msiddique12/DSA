"""
BINARY SEARCH ON 2D ARRAYS
==========================

WHEN TO USE:
- Sorted 2D matrix
- Row-wise and/or column-wise sorted
- Finding element in matrix

KEY INSIGHT: Treat as 1D array OR use row/column sorted property.

TIME: O(log(m*n)) or O(m + n)  |  SPACE: O(1)
"""

# ============================================
# PATTERN 1: Search in 2D Matrix I
# (Each row sorted, first element > last of prev row)
# ============================================
def search_matrix_1(matrix, target):
    """Treat as sorted 1D array."""
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = left + (right - left) // 2
        val = matrix[mid // cols][mid % cols]

        if val == target:
            return True
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# ============================================
# PATTERN 2: Search in 2D Matrix II
# (Rows sorted, columns sorted, but not globally)
# ============================================
def search_matrix_2(matrix, target):
    """Start from top-right corner."""
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1    # Need larger, go down
        else:
            col -= 1    # Need smaller, go left

    return False


# ============================================
# PATTERN 3: Kth Smallest in Sorted Matrix
# ============================================
def kth_smallest(matrix, k):
    """Find kth smallest element in row/col sorted matrix."""
    n = len(matrix)

    def count_less_equal(mid):
        """Count elements <= mid using staircase search."""
        count = 0
        row, col = n - 1, 0  # Start bottom-left

        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1

        return count

    left, right = matrix[0][0], matrix[n-1][n-1]

    while left < right:
        mid = left + (right - left) // 2
        if count_less_equal(mid) < k:
            left = mid + 1
        else:
            right = mid

    return left


# ============================================
# PATTERN 4: Find Peak Element in 2D
# ============================================
def find_peak_grid(mat):
    """Find any peak element (greater than 4 neighbors)."""
    rows, cols = len(mat), len(mat[0])

    left, right = 0, cols - 1

    while left <= right:
        mid_col = left + (right - left) // 2

        # Find max in this column
        max_row = 0
        for r in range(rows):
            if mat[r][mid_col] > mat[max_row][mid_col]:
                max_row = r

        # Check if it's a peak
        left_val = mat[max_row][mid_col - 1] if mid_col > 0 else -1
        right_val = mat[max_row][mid_col + 1] if mid_col < cols - 1 else -1

        if mat[max_row][mid_col] > left_val and mat[max_row][mid_col] > right_val:
            return [max_row, mid_col]
        elif left_val > mat[max_row][mid_col]:
            right = mid_col - 1
        else:
            left = mid_col + 1

    return [-1, -1]


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 74. Search a 2D Matrix
- 240. Search a 2D Matrix II
- 378. Kth Smallest Element in a Sorted Matrix
- 1901. Find a Peak Element II
"""
