import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  colors = input_data[:24]

  corners = [
      (2, 4, 17),
      (3, 5, 20),
      (6, 8, 19),
      (7, 9, 23),
      (0, 12, 16),
      (1, 13, 21),
      (10, 14, 18),
      (11, 15, 22),
  ]

  def apply_move(st, move):
    res = list(st)
    if move == "U":
      res[0], res[1], res[2], res[3] = res[2], res[0], res[3], res[1]
      l1, l2 = res[16], res[17]
      res[16], res[17] = res[12], res[13]
      res[12], res[13] = res[20], res[21]
      res[20], res[21] = res[4], res[5]
      res[4], res[5] = l1, l2
    elif move == "U2":
      res = apply_move(res, "U")
      res = apply_move(res, "U")
    elif move == "U'":
      res = apply_move(res, "U2")
      res = apply_move(res, "U")
    elif move == "F":
      res[4], res[5], res[6], res[7] = res[6], res[4], res[7], res[5]
      t2, t3 = res[2], res[3]
      res[2], res[3] = res[19], res[17]
      res[19], res[17] = res[9], res[8]
      res[9], res[8] = res[20], res[22]
      res[20], res[22] = t2, t3
    elif move == "F2":
      res = apply_move(res, "F")
      res = apply_move(res, "F")
    elif move == "F'":
      res = apply_move(res, "F2")
      res = apply_move(res, "F")
    elif move == "R":
      res[20], res[21], res[22], res[23] = (
          res[22],
          res[20],
          res[23],
          res[21],
      )
      t1, t3 = res[1], res[3]
      res[1], res[3] = res[5], res[7]
      res[5], res[7] = res[9], res[11]
      res[9], res[11] = res[13], res[15]
      res[13], res[15] = t1, t3
    elif move == "R2":
      res = apply_move(res, "R")
      res = apply_move(res, "R")
    elif move == "R'":
      res = apply_move(res, "R2")
      res = apply_move(res, "R")
    return tuple(res)

  moves = ["U", "U2", "U'", "F", "F2", "F'", "R", "R2", "R'"]

  def is_solved(st):
    for i in range(0, 24, 4):
      if len(set(st[i : i + 4])) > 1:
        return False
    return True

  def can_solve(st):
    visited = {st}
    queue = [(st, 0)]
    head = 0
    while head < len(queue):
      curr, d = queue[head]
      head += 1
      if is_solved(curr):
        return True
      if d == 4:
        continue
      for m in moves:
        nxt = apply_move(curr, m)
        if nxt not in visited:
          visited.add(nxt)
          queue.append((nxt, d + 1))
    return False

  for c in corners:
    i1, i2, i3 = c
    orig = tuple(colors)

    for direction in (1, 2):
      modified = list(orig)
      if direction == 1:
        modified[i1], modified[i2], modified[i3] = (
            orig[i3],
            orig[i1],
            orig[i2],
        )
      else:
        modified[i1], modified[i2], modified[i3] = (
            orig[i2],
            orig[i3],
            orig[i1],
        )

      if can_solve(tuple(modified)):
        corner_colors = [orig[i1], orig[i2], orig[i3]]
        corner_colors.sort()
        sys.stdout.write("".join(corner_colors))
        return


if __name__ == "__main__":
  solve()