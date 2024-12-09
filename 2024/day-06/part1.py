OBSTACLE = '#'
UP = '^'
DOWN = 'V'
LEFT = '<'
RIGHT = '>'

DELTAS = {
  UP: (-1, 0),
  DOWN: (1, 0),
  RIGHT: (0, 1),
  LEFT: (0, -1),
}

ROT = {
  UP: RIGHT,
  RIGHT: DOWN,
  DOWN: LEFT,
  LEFT: UP,
}

class Person:
  def __init__(self, start, dir):
    # possible dirs: '^', '>', 'V', '<'
    self.start_row = start[0]
    self.start_col = start[1]
    self.start_dir = dir

    self.loc = start
    self.dir = dir

    self.visited_locations = {
      (self.start_row, self.start_col): set(self.start_dir)
    }

    self.in_bounds = True

  def move(self, G):
    next_loc = self.next_spot(self.loc, self.dir)
    if G.is_obstacle(next_loc):
      self.dir = ROT[self.dir]

    else:
      self.loc = next_loc

    if not G.in_bounds(self.loc):
      self.in_bounds = False
    else:
      self.update_visited_locations()

    return

  def next_spot(self, loc, dir):
    row = loc[0]
    col = loc[1]

    row_delta, col_delta = DELTAS[dir]

    return (row + row_delta, col + col_delta)

  def update_visited_locations(self):
    if self.loc not in self.visited_locations:
      self.visited_locations[self.loc] = set(self.dir)
    else:
      self.visited_locations[self.loc].add(self.dir)

  def __repr__(self):
    s = ""
    s += f"Current Loc: {self.loc}, {self.dir}"
    return s


class Grid:
  def __init__(self, M):
    self.rows = len(M) - 1
    self.cols = len(M[0]) - 1
    self.grid = M.copy()

  def in_bounds(self, loc):
    row = loc[0]
    col = loc[1]

    if 0 <= row <= self.rows and 0 <= col <= self.cols:
      return True
    else:
      return False

  def is_obstacle(self, loc):
    row = loc[0]
    col = loc[1]
    if not self.in_bounds(loc):
      return False

    spot = self.grid[row][col]
    if spot == OBSTACLE:
      return True
    else:
      return False

  def __repr__(self):
    s = f"{(self.rows, self.cols)}\n"
    for i in range(self.rows):
      s+= "".join(self.grid[i]) + "\n"

    return s

def main():
  start, M = parse_input()

  P = Person(start, UP)
  G = Grid(M)
  print(G)

  while P.in_bounds:
    P.move(G)

  print(len(P.visited_locations.keys()))


def parse_input():
  with open("input.txt", "r") as f:
    lines = f.readlines()

  M = []
  start = None
  for i in range(len(lines)):
    m = []
    for j in range(len(lines)):
      spot = lines[i][j]
      if spot == '^':
        start = (i, j)
      m.append(spot)
    M.append(m)

  return start, M

if __name__ == "__main__":
  main()


