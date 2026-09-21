import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  idx = 0
  N = int(input_data[idx])
  M = int(input_data[idx + 1])
  idx += 2

  adj = {i: [] for i in range(1, N + 1)}
  for _ in range(M):
    u = int(input_data[idx])
    v = int(input_data[idx + 1])
    adj[u].append(v)
    adj[v].append(u)
    idx += 2

  start1 = int(input_data[idx])
  start2 = int(input_data[idx + 1])
  outpost = int(input_data[idx + 2])

  def get_all_paths(curr, dest, visited, path):
    if curr == dest:
      return [list(path)]

    paths = []
    for neighbor in adj[curr]:
      if neighbor not in visited:
        visited.add(neighbor)
        path.append(neighbor)
        paths.extend(get_all_paths(neighbor, dest, visited, path))
        path.pop()
        visited.remove(neighbor)
    return paths

  paths1 = get_all_paths(start1, outpost, {start1}, [start1])
  paths2 = get_all_paths(start2, outpost, {start2}, [start2])

  min_total_towns = float("inf")

  for p1 in paths1:
    set1 = set(p1)
    for p2 in paths2:
      set2 = set(p2)

      intersection = set1.intersection(set2)
      if intersection == {outpost}:
        total_towns = len(set1.union(set2))
        if total_towns < min_total_towns:
          min_total_towns = total_towns

  if min_total_towns == float("inf"):
    sys.stdout.write("Impossible")
  else:
    sys.stdout.write(str(min_total_towns))


if __name__ == "__main__":
  solve()