
"""pipes for adjacent spots can be determined like so:

                            (Y-1, X)
                        ['|', '7', 'F']
                               v
  (Y, X-1)['-', 'L', 'F'] > (X, Y) < ['-', 'J', '7'](Y, X+1)
                               ^
                        ['|', 'J', 'L']
                            (Y+1, X)
"""

VALID_PIPES = {
  (0,-1): ['-', 'L', 'F'],
  (0,1): ['-', 'J', '7'],
  (-1,0): ['|', '7', 'F'],
  (1,0): ['|', 'J', 'L']
}

PIPE_ADJ = {
  "-": [(0,-1), (0,1)],
  "|": [(-1,0), (1,0)],
  "L": [(0,-1), (1,0)],
  "J": [(0,1), (1,0)],
  "7": [(0,1), (-1,0)],
  "F": [(0,-1), (-1,0)]
}

def main():
  # (0, 0) is northwestern most corner of map
  S, M = parse_input()
  print(S)
  print_map(M)

  print(spot_connects(S, (1, 2), M))
  # print(next_spot(S, (1, 2), M))
  print(next_spot((1, 2), (1, 3), M))
  # print(next_spot((1, 3), (2, 3), M))
  # print(next_spot((2, 3), (3, 3), M))
  # print(next_spot((3, 3), (3, 2), M))
  # print(next_spot((3, 2), (3, 1), M))
  # print(next_spot((3, 1), (2, 1), M))



def print_map(M):
  for m in M:
    print(m)

def next_spot(prior_spot, curr_spot, M):
  """given a prior spot and the the current spot, identifies
  the next spot of the loop"""

  (y0, x0) = prior_spot
  (y1, x1) = curr_spot

  Y = y0 - y1
  X = x0 - x1

  pipe = M[y1][x1]
  possible_moves = PIPE_ADJ[pipe]

  print(curr_spot, prior_spot)
  print(Y, X)
  print(pipe)
  print(possible_moves)

  if possible_moves[0] == (Y, X):
    y_delta = possible_moves[1][0]
    x_delta = possible_moves[1][1]
  else:
    y_delta = possible_moves[0][0]
    x_delta = possible_moves[0][1]

  return (y1 + y_delta, x1 + x_delta)

def spot_connects(spot, adj, M):
  """returns true if the pipe in adj connects to spot"""

  (y0, x0) = spot
  (y1, x1) = adj

  pipe = M[y1][x1]

  if pipe in VALID_PIPES[(y1-y0,x1-x0)]:
    return True
  else:
    return False





def parse_input():
  with open("input.txt", "r") as f:
    lines = f.readlines()

  M = []
  for i, line in enumerate(lines):
    row = []
    for j, c in enumerate(line.strip()):
      if c == 'S':
        S = (i, j)
      row.append(c)
    M.append(row)

  return S, M

if __name__ == "__main__":
  main()
