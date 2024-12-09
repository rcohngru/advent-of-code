from copy import deepcopy

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
    self.in_loop = False

  def reset(self):
    self.loc = (self.start_row, self.start_col)
    self.dir = self.start_dir

    self.visited_locations = {
      (self.start_row, self.start_col): set(self.start_dir)
    }

    self.in_bounds = True
    self.in_loop = False

  def move(self, G):
    next_loc = self.next_spot()
    if G.is_obstacle(next_loc):
      self.dir = ROT[self.dir]

    else:
      self.loc = next_loc

    if self.loc in self.visited_locations:
      if self.dir in self.visited_locations[self.loc]:
        # if the current spot and direction has already been visited
        # the the guard is in a loop
        self.in_loop = True

    if not G.in_bounds(self.loc):
      self.in_bounds = False
    else:
      self.update_visited_locations()

    return

  def next_spot(self):
    row = self.loc[0]
    col = self.loc[1]

    row_delta, col_delta = DELTAS[self.dir]

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

    self.temp_obstacle = None

  def in_bounds(self, loc):
    row = loc[0]
    col = loc[1]

    if 0 <= row <= self.rows and 0 <= col <= self.cols:
      return True
    else:
      return False

  def add_obstacle(self, loc):
    self.temp_obstacle = loc
    return

  def is_obstacle(self, loc):
    row = loc[0]
    col = loc[1]
    if not self.in_bounds(loc):
      return False

    spot = self.grid[row][col]
    if spot == OBSTACLE or loc == self.temp_obstacle:
      return True
    else:
      return False

  def __repr__(self):
    s = f"{(self.rows, self.cols)}\n"
    for i in range(self.rows):
      for j in range(self.cols + 1):
        if self.temp_obstacle and (i, j) == self.temp_obstacle:
          s+= 'O'
        else:
          s+= self.grid[i][j]
      s += "\n"

    return s

def main():
  start, M = parse_input()

  P = Person(start, UP)
  G = Grid(M)
  loops = 0
  while P.in_bounds:
    P1 = deepcopy(P)
    P1.reset()
    G1 = deepcopy(G)

    G1.add_obstacle(P.next_spot())

    l = sim_obstacle(G1, P1)
    if l == 1:
      print(P.next_spot())
      loops += 1
      print(f"found loop #{loops}, visited {len(P.visited_locations.keys())}")

    P.move(G)

  print(loops)

def sim_obstacle(G, P):
  while P.in_bounds and not P.in_loop:
    P.move(G)

  if P.in_loop:
    return 1
  else:
    return 0


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


