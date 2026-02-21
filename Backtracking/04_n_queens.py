"""
N-QUEENS
========

WHEN TO USE:
- Constraint satisfaction problems
- Placing items with constraints
- Sudoku-like problems

KEY INSIGHT: Place queen row by row. Track attacked columns and diagonals.
Diagonals: (row-col) for one direction, (row+col) for other.

TIME: O(n!)  |  SPACE: O(n)
"""

# ============================================
# PATTERN 1: N-Queens (Return All Solutions)
# ============================================
def solve_n_queens(n):
    """Find all valid n-queens arrangements."""
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def backtrack(row):
        if row == n:
            result.append([''.join(r) for r in board])
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # Place queen
            board[row][col] = 'Q'
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtrack(row + 1)

            # Remove queen
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return result


# ============================================
# PATTERN 2: N-Queens II (Count Solutions)
# ============================================
def total_n_queens(n):
    """Count the number of valid n-queens arrangements."""
    count = 0
    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtrack(row + 1)

            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return count


# ============================================
# PATTERN 3: Sudoku Solver
# ============================================
def solve_sudoku(board):
    """Solve sudoku in-place."""
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # Initialize sets
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                num = board[i][j]
                rows[i].add(num)
                cols[j].add(num)
                boxes[(i // 3) * 3 + j // 3].add(num)

    def backtrack(pos):
        if pos == 81:
            return True

        i, j = pos // 9, pos % 9
        if board[i][j] != '.':
            return backtrack(pos + 1)

        box_idx = (i // 3) * 3 + j // 3
        for num in '123456789':
            if num in rows[i] or num in cols[j] or num in boxes[box_idx]:
                continue

            board[i][j] = num
            rows[i].add(num)
            cols[j].add(num)
            boxes[box_idx].add(num)

            if backtrack(pos + 1):
                return True

            board[i][j] = '.'
            rows[i].remove(num)
            cols[j].remove(num)
            boxes[box_idx].remove(num)

        return False

    backtrack(0)


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Hard:
- 51. N-Queens
- 52. N-Queens II
- 37. Sudoku Solver
- 36. Valid Sudoku (validation only)
"""
