import sys


def solve():
  input_data = sys.stdin.read().splitlines()
  if not input_data:
    return

  lines = [line.strip() for line in input_data if line.strip()]
  if not lines:
    return

  idx = 0
  parts = lines[idx].split()
  N = int(parts[0])
  M = int(parts[1])
  idx += 1

  grid = []
  for _ in range(N):
    grid.append(lines[idx].split())
    idx += 1

  T = int(lines[idx])
  idx += 1
  I = int(lines[idx])
  idx += 1

  excluded = {t: [] for t in range(1, T + 1)}

  for _ in range(I):
    t = int(lines[idx])
    idx += 1
    coords = list(map(int, lines[idx].split()))
    idx += 1
    x1, y1, x2, y2 = coords
    excluded[t].append((x1, y1, x2, y2))

  allowed_cells_at_t = []
  for t in range(1, T + 1):
    valid_set = set()
    for r in range(1, N + 1):
      for c in range(1, M + 1):
        is_excluded = False
        for x1, y1, x2, y2 in excluded[t]:
          if x1 <= r <= x2 and y1 <= c <= y2:
            is_excluded = True
            break
        if not is_excluded:
          valid_set.add((r - 1, c - 1))
    allowed_cells_at_t.append(valid_set)

  valid_paths = []

  def dfs(t, r, c, path, visited):
    if t == T:
      valid_paths.append(list(path))
      return

    next_t = t + 1
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nr, nc = r + dr, c + dc
      if 0 <= nr < N and 0 <= nc < M:
        if (nr, nc) not in visited:
          if (nr, nc) in allowed_cells_at_t[next_t]:
            visited.add((nr, nc))
            path.append((nr, nc))
            dfs(next_t, nr, nc, path, visited)
            path.pop()
            visited.remove((nr, nc))

  for r, c in allowed_cells_at_t[0]:
    dfs(0, r, c, [(r, c)], {(r, c)})

  if not valid_paths:
    sys.stdout.write("Not enough clues")
    return

  keys = set()
  for path in valid_paths:
    key_chars = [grid[r][c] for r, c in path]
    keys.add("".join(key_chars))

  if len(keys) == 1:
    sys.stdout.write(list(keys)[0])
  else:
    sys.stdout.write("Not enough clues")


if __name__ == "__main__":
  solve()