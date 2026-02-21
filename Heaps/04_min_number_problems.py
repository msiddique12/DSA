"""
MINIMUM NUMBER PROBLEMS (Heap)
==============================

WHEN TO USE:
- Minimize cost by combining elements
- Task scheduling with cooldowns
- Reorganizing strings
- Problems requiring greedy min/max selection

KEY INSIGHT: Heaps give O(log n) access to min/max.
Process greedily by always taking optimal choice.

TIME: O(n log n)  |  SPACE: O(n)
"""

import heapq
from collections import Counter

# ============================================
# PATTERN 1: Minimum Cost to Connect Sticks
# ============================================
def connect_sticks(sticks):
    """
    Connect sticks, cost = sum of lengths being connected.
    Minimize total cost.
    Greedy: always connect two smallest.
    """
    heapq.heapify(sticks)
    total_cost = 0

    while len(sticks) > 1:
        first = heapq.heappop(sticks)
        second = heapq.heappop(sticks)
        cost = first + second
        total_cost += cost
        heapq.heappush(sticks, cost)

    return total_cost


# ============================================
# PATTERN 2: Task Scheduler
# ============================================
def least_interval(tasks, n):
    """
    Schedule tasks with cooldown n between same tasks.
    Return minimum intervals needed.
    """
    count = Counter(tasks)
    # Max-heap of remaining counts
    heap = [-cnt for cnt in count.values()]
    heapq.heapify(heap)

    time = 0
    while heap:
        temp = []
        cycle = n + 1  # Process up to n+1 tasks in cycle

        for _ in range(cycle):
            if heap:
                cnt = heapq.heappop(heap)
                if cnt + 1 < 0:  # Still has remaining
                    temp.append(cnt + 1)
            time += 1

            if not heap and not temp:
                break  # All done

        for item in temp:
            heapq.heappush(heap, item)

    return time


# ============================================
# PATTERN 3: Reorganize String
# ============================================
def reorganize_string(s):
    """
    Rearrange so no two adjacent chars are same.
    Return "" if impossible.
    """
    count = Counter(s)

    # Check if possible
    max_count = max(count.values())
    if max_count > (len(s) + 1) // 2:
        return ""

    # Max-heap of (-count, char)
    heap = [(-cnt, char) for char, cnt in count.items()]
    heapq.heapify(heap)

    result = []
    while len(heap) >= 2:
        cnt1, char1 = heapq.heappop(heap)
        cnt2, char2 = heapq.heappop(heap)

        result.extend([char1, char2])

        if cnt1 + 1 < 0:
            heapq.heappush(heap, (cnt1 + 1, char1))
        if cnt2 + 1 < 0:
            heapq.heappush(heap, (cnt2 + 1, char2))

    if heap:
        result.append(heap[0][1])

    return ''.join(result)


# ============================================
# PATTERN 4: Minimum Cost to Hire K Workers
# ============================================
def mincost_to_hire_workers(quality, wage, k):
    """
    Hire k workers. Each worker has quality[i] and min wage[i].
    Total wage proportional to quality. Minimize cost.
    """
    # ratio = wage/quality, higher ratio = more expensive per quality
    workers = sorted([(w/q, q) for w, q in zip(wage, quality)])

    heap = []  # Max-heap of qualities
    quality_sum = 0
    result = float('inf')

    for ratio, q in workers:
        heapq.heappush(heap, -q)
        quality_sum += q

        if len(heap) > k:
            quality_sum += heapq.heappop(heap)  # Remove largest quality

        if len(heap) == k:
            result = min(result, ratio * quality_sum)

    return result


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 1167. Minimum Cost to Connect Sticks
- 621. Task Scheduler
- 767. Reorganize String
- 1054. Distant Barcodes

Hard:
- 857. Minimum Cost to Hire K Workers
- 358. Rearrange String k Distance Apart
"""
