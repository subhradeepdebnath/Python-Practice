import sys


def solve():
  input_data = sys.stdin.read().splitlines()
  if not input_data:
    return

  lines = [line.strip() for line in input_data if line.strip()]
  if not lines:
    return

  idx = 0
  N = int(lines[idx])
  idx += 1

  adj = {}
  for _ in range(N):
    parts = lines[idx].split()
    idx += 1
    src = parts[0]
    if src not in adj:
      adj[src] = set()
    for dest in parts[1:]:
      adj[src].add(dest)
      if dest not in adj:
        adj[dest] = set()
      adj[dest].add(src)

  Q = int(lines[idx])
  idx += 1

  queries = []
  for _ in range(Q):
    queries.append(lines[idx])
    idx += 1

  R = int(lines[idx])
  idx += 1

  restrictions = {}
  for _ in range(R):
    parts = lines[idx].split()
    idx += 1
    src = parts[0]
    restricted_set = set(parts[1:])
    restrictions[src] = restricted_set

  def can_reach(start, dest, src_for_restriction):
    if start not in adj or dest not in adj:
      return False
    restricted = restrictions.get(src_for_restriction, set())
    if start in restricted or dest in restricted:
      return False

    visited = {start}
    queue = [start]
    head = 0

    while head < len(queue):
      curr = queue[head]
      head += 1

      if curr == dest:
        return True

      for neighbor in adj.get(curr, []):
        if neighbor not in visited and neighbor not in restricted:
          visited.add(neighbor)
          queue.append(neighbor)

    return False

  for q in queries:
    if " to " in q:
      parts = q.split(" to ")
      u = parts[0].strip()
      v = parts[1].strip()
      if can_reach(u, v, u):
        print("yes")
      else:
        print("no")
    elif " connects " in q:
      parts = q.split(" connects ")
      u = parts[0].strip()
      v = parts[1].strip()
      if u not in adj:
        adj[u] = set()
      if v not in adj:
        adj[v] = set()
      adj[u].add(v)
      adj[v].add(u)
    elif " disconnects " in q:
      parts = q.split(" disconnects ")
      u = parts[0].strip()
      v = parts[1].strip()
      if u in adj and v in adj[u]:
        adj[u].remove(v)
      if v in adj and u in adj[v]:
        adj[v].remove(u)


if __name__ == "__main__":
  solve()