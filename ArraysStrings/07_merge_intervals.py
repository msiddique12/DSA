"""
MERGE INTERVALS
===============

WHEN TO USE:
- Overlapping interval problems
- Meeting room scheduling
- Insert/merge intervals
- Interval intersection

KEY INSIGHT: Sort by start time. Merge if current.start <= prev.end.

TIME: O(n log n) for sort  |  SPACE: O(n)
"""

# ============================================
# PATTERN 1: Merge Overlapping Intervals
# ============================================
def merge(intervals):
    """Merge all overlapping intervals."""
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= result[-1][1]:  # Overlaps
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])

    return result


# ============================================
# PATTERN 2: Insert Interval
# ============================================
def insert(intervals, new):
    """Insert new interval and merge if necessary."""
    result = []
    i = 0
    n = len(intervals)

    # Add all intervals before new
    while i < n and intervals[i][1] < new[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping with new
    while i < n and intervals[i][0] <= new[1]:
        new[0] = min(new[0], intervals[i][0])
        new[1] = max(new[1], intervals[i][1])
        i += 1
    result.append(new)

    # Add remaining
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


# ============================================
# PATTERN 3: Interval Intersection
# ============================================
def interval_intersection(A, B):
    """Find intersection of two sorted interval lists."""
    result = []
    i = j = 0

    while i < len(A) and j < len(B):
        # Find intersection
        start = max(A[i][0], B[j][0])
        end = min(A[i][1], B[j][1])

        if start <= end:
            result.append([start, end])

        # Move pointer of interval that ends first
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1

    return result


# ============================================
# PATTERN 4: Meeting Rooms (Can Attend All?)
# ============================================
def can_attend_meetings(intervals):
    """Check if person can attend all meetings."""
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True


# ============================================
# PATTERN 5: Meeting Rooms II (Min Rooms Needed)
# ============================================
def min_meeting_rooms(intervals):
    """Minimum conference rooms required."""
    if not intervals:
        return 0

    # Separate start and end times
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])

    rooms = max_rooms = 0
    s = e = 0

    while s < len(starts):
        if starts[s] < ends[e]:
            rooms += 1
            s += 1
        else:
            rooms -= 1
            e += 1
        max_rooms = max(max_rooms, rooms)

    return max_rooms


# ============================================
# PATTERN 6: Non-Overlapping Intervals (Min Removals)
# ============================================
def erase_overlap_intervals(intervals):
    """Minimum intervals to remove for non-overlapping."""
    if not intervals:
        return 0

    # Sort by end time (greedy: keep shorter intervals)
    intervals.sort(key=lambda x: x[1])
    count = 0
    prev_end = float('-inf')

    for start, end in intervals:
        if start >= prev_end:
            prev_end = end  # Keep this interval
        else:
            count += 1  # Remove this interval

    return count


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Easy:
- 252. Meeting Rooms

Medium:
- 56. Merge Intervals
- 57. Insert Interval
- 986. Interval List Intersections
- 253. Meeting Rooms II
- 435. Non-overlapping Intervals
- 452. Minimum Number of Arrows to Burst Balloons

Hard:
- 759. Employee Free Time
"""
