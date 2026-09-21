import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  N = int(input_data[0])
  idx = 1
  commands = []

  for _ in range(N):
    ex = int(input_data[idx])
    new_c = int(input_data[idx + 1])
    direction = input_data[idx + 2].lower()
    commands.append((ex, new_c, direction))
    idx += 3

  target_cube = int(input_data[idx])

  commands.sort(key=lambda x: (x[0], x[1]))

  cube_to_pos = {}
  pos_to_cube = {}

  cube_to_pos[1] = (0, 0)
  pos_to_cube[(0, 0)] = 1

  for ex, new_c, direction in commands:
    if ex not in cube_to_pos:
      continue

    r, c = cube_to_pos[ex]

    if direction in ("top", "up"):
      nr, nc = r - 1, c
    elif direction == "down":
      nr, nc = r + 1, c
    elif direction == "left":
      nr, nc = r, c - 1
    elif direction == "right":
      nr, nc = r, c + 1
    else:
      continue

    if (nr, nc) in pos_to_cube:
      old_cube = pos_to_cube[(nr, nc)]
      if old_cube in cube_to_pos:
        del cube_to_pos[old_cube]

    pos_to_cube[(nr, nc)] = new_c
    cube_to_pos[new_c] = (nr, nc)

  if target_cube not in cube_to_pos:
    sys.stdout.write("-1 -1 -1 -1")
    return

  r, c = cube_to_pos[target_cube]

  up_cube = pos_to_cube.get((r - 1, c), -1)
  down_cube = pos_to_cube.get((r + 1, c), -1)
  left_cube = pos_to_cube.get((r, c - 1), -1)
  right_cube = pos_to_cube.get((r, c + 1), -1)
  sys.stdout.write(
      f"{up_cube} {down_cube} {left_cube} {right_cube}".strip()
  )


if __name__ == "__main__":
  solve()