
DELTAS = {
  "U": (-1, 0),
  "D": (1, 0),
  "L": (0, -1),
  "R": (0, 1)
}

def main():
  M, S, E = parse_input()

  dist = {}
  cell = S
  ps = 0
  while cell != E:
    dist[cell] = {
      "ps": ps,
      "next": None
    }
    for dir in "UDLR":
      drow, dcol = DELTAS[dir]
      next_cell = (cell[0] + drow, cell[1] + dcol)
      next_space = M[next_cell[0]][next_cell[1]]
      if next_space != "#" and next_cell not in dist:
        dist[cell]["next"] = next_cell
        cell = next_cell
        ps += 1
        break
  dist[E] = {
    "ps": ps,
    "next": None
  }

  cheats = {}
  radius = 20
  for cell in dist.keys():
    for r in range(cell[0] - radius, cell[0] + radius + 1):
      for c in range(cell[1] - radius, cell[1] + radius + 1):
        cheat_cell = (r, c)
        distance = abs(r - cell[0]) + abs(c - cell[1])
        if distance <= radius:
          if cheat_cell in dist:
            savings = dist[cell]["ps"] - dist[cheat_cell]["ps"] + distance
            if savings < 0:
              cheats[(cell, cheat_cell)] = savings


  tot = 0
  for cheat, savings in cheats.items():
    if savings <= -100:
      tot += 1

  print(tot)

def parse_input():
  with open("input.txt", "r") as f:
    lines = f.readlines()

  M = []
  for row, line in enumerate(lines):
    m = []
    for col, cell in enumerate(line.strip()):
      if cell == 'S':
        S = (row, col)
      if cell == 'E':
        E = (row, col)

      m.append(cell)
    M.append(m)

  return M, S, E


if __name__ == "__main__":
  main()
