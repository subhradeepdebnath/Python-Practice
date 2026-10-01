# # A data analyst is given an array data representing data collected over n days. They are also given k update operations.

# Each update is represented by a pair [l, r], where l and r are 1-based indices.

# For every update [l, r]:

# Negate (multiply by -1) every element of data from index l to r, inclusive.
# Apply the updates in the given order.

# After applying all k updates, return the final data array.

# Example

# Input:

# n = 4
# data = [1, -4, 5, -2]
# k = 2
# updates = [[2, 4], [1, 2]]
# Step 1 — Apply [2, 4]

# Negate elements from index 2 to 4:

# [1, -4, 5, -2]
#        ↓   ↓  ↓
# [1,  4, -5,  2]
# Step 2 — Apply [1, 2]

# Negate elements from index 1 to 2:

# [1, 4, -5, 2]
#  ↓  ↓
# [-1, -4, -5, 2]

# Wait — let's carefully apply the operations: after the first update we have [1, 4, -5, 2]; negating indices 1–2 gives:

# [-1, -4, -5, 2]

# So the correct output for the stated operations is:

# [-1, -4, -5, 2]
# Input Format
# The first line contains an integer n, the number of elements in data.
# The next n lines each contain one integer data[i].
# The next two lines contain:
# k — the number of updates.
# 2 — the number of columns in the updates array (always 2).
# The next k lines each contain two space-separated integers l and r, representing an update [l, r].
# Output Format

# Return the final data array after applying all updates in order.

# Constraints
# 1 ≤ n
# 1 ≤ k
# 1 ≤ l ≤ r ≤ n
# |data[i]| ≤ 10^9
# Each update contains exactly two integers [l, r].
# Indices are 1-based.
# Sample Input
# 4
# 1
# -4
# 5
# -2
# 2
# 2
# 2 4
# 1 2
# Sample Output
# -1 -4 -5 2



