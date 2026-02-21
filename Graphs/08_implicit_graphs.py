"""
IMPLICIT GRAPHS
===============

WHEN TO USE:
- State space search
- Puzzle solving (sliding puzzle, word ladder)
- When graph isn't given but can be derived

KEY INSIGHT: States are nodes, valid transitions are edges.
Use BFS for shortest path in state space.

TIME: O(states * transitions)  |  SPACE: O(states)
"""

from collections import deque

# ============================================
# PATTERN 1: Open the Lock
# ============================================
def open_lock(deadends, target):
    """
    Lock has 4 wheels, each 0-9. Start at "0000".
    Find minimum moves to reach target avoiding deadends.
    """
    dead = set(deadends)
    if "0000" in dead:
        return -1
    if target == "0000":
        return 0

    visited = {"0000"}
    queue = deque([("0000", 0)])

    def neighbors(code):
        for i in range(4):
            digit = int(code[i])
            for d in (-1, 1):
                new_digit = (digit + d) % 10
                yield code[:i] + str(new_digit) + code[i+1:]

    while queue:
        code, steps = queue.popleft()

        for next_code in neighbors(code):
            if next_code == target:
                return steps + 1
            if next_code not in visited and next_code not in dead:
                visited.add(next_code)
                queue.append((next_code, steps + 1))

    return -1


# ============================================
# PATTERN 2: Sliding Puzzle
# ============================================
def sliding_puzzle(board):
    """
    2x3 board, slide to reach [[1,2,3],[4,5,0]].
    Return minimum moves (-1 if impossible).
    """
    target = "123450"
    start = "".join(str(n) for row in board for n in row)

    if start == target:
        return 0

    # Neighbors of each position in flattened board
    neighbors = {
        0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
        3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
    }

    visited = {start}
    queue = deque([(start, 0)])

    while queue:
        state, moves = queue.popleft()
        zero = state.index('0')

        for neighbor in neighbors[zero]:
            new_state = list(state)
            new_state[zero], new_state[neighbor] = new_state[neighbor], new_state[zero]
            new_state = "".join(new_state)

            if new_state == target:
                return moves + 1
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, moves + 1))

    return -1


# ============================================
# PATTERN 3: Minimum Knight Moves
# ============================================
def min_knight_moves(x, y):
    """Minimum moves for knight from (0,0) to (x,y)."""
    x, y = abs(x), abs(y)  # Symmetry

    visited = {(0, 0)}
    queue = deque([(0, 0, 0)])

    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    while queue:
        cx, cy, steps = queue.popleft()

        if (cx, cy) == (x, y):
            return steps

        for dx, dy in moves:
            nx, ny = cx + dx, cy + dy
            # Limit search space (knight can't go too far negative)
            if (nx, ny) not in visited and nx >= -2 and ny >= -2:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1


# ============================================
# PATTERN 4: Water Jugs Problem
# ============================================
def can_measure_water(jug1, jug2, target):
    """
    Can we measure exactly target liters using two jugs?
    Operations: fill, empty, pour from one to other.
    """
    if target > jug1 + jug2:
        return False

    visited = set()
    stack = [(0, 0)]

    while stack:
        a, b = stack.pop()

        if a == target or b == target or a + b == target:
            return True

        if (a, b) in visited:
            continue
        visited.add((a, b))

        # All possible states
        stack.extend([
            (jug1, b),  # Fill jug1
            (a, jug2),  # Fill jug2
            (0, b),     # Empty jug1
            (a, 0),     # Empty jug2
            # Pour jug1 -> jug2
            (max(0, a - (jug2 - b)), min(jug2, a + b)),
            # Pour jug2 -> jug1
            (min(jug1, a + b), max(0, b - (jug1 - a))),
        ])

    return False


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 752. Open the Lock
- 773. Sliding Puzzle
- 1197. Minimum Knight Moves
- 365. Water and Jug Problem
- 1293. Shortest Path in a Grid with Obstacles

Hard:
- 815. Bus Routes
- 864. Shortest Path to Get All Keys
"""
