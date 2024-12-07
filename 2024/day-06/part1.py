import numpy as np

def main():
  global M
  M = parse_input()

  dir = (-1, 0)
  loc = np.where(M == '^')
  loc = (int(loc[0][0]), int(loc[1][0]))

  while not off_map(loc):
    M[loc[0], loc[1]] = 'X'
    loc, dir = move(loc, dir)

  print(np.count_nonzero(M == 'X'))

def move(loc, dir):

  # bad
  while True:
    next_loc = (loc[0] + dir[0], loc[1] + dir[1])
    if moveable_spot(next_loc):
      break
    else:
      dir = rot90(dir)

  return next_loc, dir

def off_map(loc):
  mins = (0, 0)
  maxes = M.shape

  if mins[0] <= loc[0] < maxes[0] and mins[1] <= loc[1] < maxes[1]:
    return False
  else:
    return True

def moveable_spot(loc):
  if off_map(loc):
    return True

  if M[loc[0], loc[1]] == '#':
    return False
  else:
    return True

def rot90(dir):
  if dir == (-1, 0):
    return (0, 1)
  if dir == (0, 1):
    return (1, 0)
  if dir == (1, 0):
    return (0, -1)
  if dir ==(0, -1):
    return (-1, 0)

def parse_input():
  with open("input.txt", "r") as f:
    lines = f.readlines()

  M = []
  for line in lines:
    M.append([c for c in line.strip()])

  return np.array(M)

if __name__ == "__main__":
  main()
