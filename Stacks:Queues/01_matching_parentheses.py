"""
MATCHING PARENTHESES
====================

WHEN TO USE:
- Validate brackets/parentheses
- Parse expressions
- HTML/XML tag matching

KEY INSIGHT: Use stack. Push opening brackets, pop and match closing.
Stack should be empty at end for valid expression.

TIME: O(n)  |  SPACE: O(n)
"""

# ============================================
# PATTERN 1: Valid Parentheses
# ============================================
def is_valid(s):
    """Check if brackets are valid: (), [], {}"""
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping:  # Closing bracket
            if not stack or stack.pop() != mapping[char]:
                return False
        else:  # Opening bracket
            stack.append(char)

    return len(stack) == 0


# ============================================
# PATTERN 2: Minimum Add to Make Valid
# ============================================
def min_add_to_make_valid(s):
    """Minimum insertions to make parentheses valid."""
    open_count = 0
    insertions = 0

    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count > 0:
                open_count -= 1
            else:
                insertions += 1

    return insertions + open_count


# ============================================
# PATTERN 3: Longest Valid Parentheses
# ============================================
def longest_valid_parentheses(s):
    """Length of longest valid parentheses substring."""
    stack = [-1]  # Base for length calculation
    max_len = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)  # New base
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len


# ============================================
# PATTERN 4: Remove Invalid Parentheses
# ============================================
def remove_invalid_parentheses(s):
    """Remove minimum parentheses to make valid. Return all results."""
    def is_valid_expr(expr):
        count = 0
        for c in expr:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    result = []
    visited = {s}
    queue = [s]

    found = False
    while queue:
        current = queue.pop(0)

        if is_valid_expr(current):
            result.append(current)
            found = True

        if found:
            continue  # Don't go deeper if found at this level

        for i in range(len(current)):
            if current[i] not in '()':
                continue
            next_str = current[:i] + current[i+1:]
            if next_str not in visited:
                visited.add(next_str)
                queue.append(next_str)

    return result


# ============================================
# PATTERN 5: Generate Parentheses
# ============================================
def generate_parentheses(n):
    """Generate all valid combinations of n pairs."""
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    backtrack('', 0, 0)
    return result


# ============================================
# PATTERN 6: Score of Parentheses
# ============================================
def score_of_parentheses(s):
    """
    () = 1
    AB = A + B
    (A) = 2 * A
    """
    stack = [0]

    for char in s:
        if char == '(':
            stack.append(0)
        else:
            inner = stack.pop()
            stack[-1] += max(2 * inner, 1)

    return stack[0]


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 20. Valid Parentheses
- 1614. Maximum Nesting Depth of the Parentheses

Medium:
- 22. Generate Parentheses
- 921. Minimum Add to Make Parentheses Valid
- 856. Score of Parentheses
- 1249. Minimum Remove to Make Valid Parentheses

Hard:
- 32. Longest Valid Parentheses
- 301. Remove Invalid Parentheses
"""
