"""
UNION-FIND (Disjoint Set Union)
===============================

WHEN TO USE:
- Dynamic connectivity queries
- Kruskal's MST
- Detect cycle in undirected graph
- Grouping elements

KEY INSIGHT: Use path compression + union by rank for near O(1) operations.

TIME: O(α(n)) ≈ O(1) amortized  |  SPACE: O(n)
"""

# ============================================
# PATTERN 1: Basic Union-Find
# ============================================
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # Number of components

    def find(self, x):
        """Find root with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """Union by rank. Returns True if merged."""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        # Attach smaller tree under larger
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        self.count -= 1
        return True

    def connected(self, x, y):
        """Check if x and y are in same set."""
        return self.find(x) == self.find(y)


# ============================================
# PATTERN 2: Number of Connected Components
# ============================================
def count_components(n, edges):
    """Count connected components using union-find."""
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.count


# ============================================
# PATTERN 3: Redundant Connection (Find Cycle Edge)
# ============================================
def find_redundant_connection(edges):
    """
    Find the edge that creates a cycle.
    Return last such edge if multiple.
    """
    n = len(edges)
    uf = UnionFind(n + 1)  # 1-indexed nodes

    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]

    return []


# ============================================
# PATTERN 4: Accounts Merge
# ============================================
def accounts_merge(accounts):
    """Merge accounts with common emails."""
    from collections import defaultdict

    email_to_id = {}
    email_to_name = {}
    uf = UnionFind(len(accounts) * 10)  # Max emails estimate
    email_id = 0

    for i, account in enumerate(accounts):
        name = account[0]
        for email in account[1:]:
            if email not in email_to_id:
                email_to_id[email] = email_id
                email_id += 1
            email_to_name[email] = name
            uf.union(email_to_id[account[1]], email_to_id[email])

    # Group emails by root
    groups = defaultdict(list)
    for email, idx in email_to_id.items():
        root = uf.find(idx)
        groups[root].append(email)

    return [[email_to_name[emails[0]]] + sorted(emails)
            for emails in groups.values()]


# ============================================
# PATTERN 5: Longest Consecutive Sequence
# ============================================
def longest_consecutive(nums):
    """Find length of longest consecutive sequence."""
    if not nums:
        return 0

    num_set = set(nums)
    num_to_idx = {num: i for i, num in enumerate(nums)}
    uf = UnionFind(len(nums))

    for num in nums:
        if num + 1 in num_set:
            uf.union(num_to_idx[num], num_to_idx[num + 1])

    # Count sizes of each component
    from collections import Counter
    roots = [uf.find(i) for i in range(len(nums))]
    return max(Counter(roots).values())


# ============================================
# KEY PROBLEMS (LeetCode)
# ============================================
"""
Medium:
- 323. Number of Connected Components
- 684. Redundant Connection
- 721. Accounts Merge
- 128. Longest Consecutive Sequence
- 547. Number of Provinces

Hard:
- 685. Redundant Connection II (directed)
- 305. Number of Islands II
"""
