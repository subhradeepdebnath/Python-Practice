import heapq
import re
import sys


def solve():
  input_data = sys.stdin.read().splitlines()
  if not input_data:
    return

  lines = [line.strip() for line in input_data if line.strip()]
  if not lines:
    return

  N = int(lines[0])
  grid = []

  for i in range(1, N + 1):
    if i >= len(lines):
      break
    line = lines[i]
    tokens = re.findall(r"(\d+)([RGSD])", line)
    row = []
    for count_str, char in tokens:
      count = int(count_str)
      row.extend([char] * count)
    grid.append(row)

  sources = []
  destinations = set()

  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] == "S":
        sources.append((r, c))
      elif grid[r][c] == "D":
        destinations.add((r, c))

  pq = []
  dist = {}

  for r, c in sources:
    dist[(r, c)] = 0
    heapq.heappush(pq, (0, r, c))

  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  min_cost = float("inf")

  while pq:
    cost, r, c = heapq.heappop(pq)

    if (r, c) in destinations:
      min_cost = cost
      break

    if cost > dist.get((r, c), float("inf")):
      continue

    for dr, dc in directions:
      nr, nc = r + dr, c + dc
      if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
        cell_type = grid[nr][nc]
        if cell_type == "R":
          continue

        weight = 1 if cell_type == "G" else 0
        new_cost = cost + weight

        if new_cost < dist.get((nr, nc), float("inf")):
          dist[(nr, nc)] = new_cost
          heapq.heappush(pq, (new_cost, nr, nc))

  # sys.stdout.write ka use karne se koi bhi extra newline ya formatting error nahi aayega
  sys.stdout.write(str(min_cost))


if __name__ == "__main__":
  solve()