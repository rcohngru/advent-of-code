import numpy as np

def main():
  V = set() # visited locations ((loc), (dir))
  M = parse_input()
  M_copy = M.copy()

  dir = (-1, 0)
  loc = np.where(M == '^')
  loc = (int(loc[0][0]), int(loc[1][0]))


  while not off_map(loc, M):
    V.add((loc, dir))
    # fuck it brute force

    obs_works = check_loop(loc, dir, M, V)
    if obs_works:
      M_copy[loc[0] + dir[0], loc[1] + dir[1]] = 'O'

    M[loc[0], loc[1]] = 'X'
    loc, dir = move(loc, dir, M)


  print(M_copy)
  print(np.count_nonzero(M_copy == 'O'))

def check_loop(loc, dir, M, V):
  # given a location and a direction, place an obstruction immediately in front
  # of guard and evaluate until either the guard exits the map (not a loop) or
  # the guard arrives at a location with a direction that it has already visited

  if dir == (-1, 0):
    obs = (loc[0] - 1, loc[1])

  if dir == (0, 1):
    obs = (loc[0], loc[1] + 1)

  if dir == (1, 0):
    obs = (loc[0] + 1, loc[1])

  if dir ==(0, -1):
    obs = (loc[0], loc[1] - 1)

  if off_map(obs, M):
    return False

  # bad
  while not off_map(loc, M):
    V.add((loc, dir))
    loc, dir = move(loc, dir, M)

    if (loc, dir) in V:
      return True

  return False

def move(loc, dir, M):

  # bad
  while True:
    next_loc = (loc[0] + dir[0], loc[1] + dir[1])
    if moveable_spot(next_loc, M):
      break
    else:
      dir = rot90(dir)

  return next_loc, dir

def off_map(loc, M):
  mins = (0, 0)
  maxes = M.shape

  if mins[0] <= loc[0] < maxes[0] and mins[1] <= loc[1] < maxes[1]:
    return False
  else:
    return True

def moveable_spot(loc, M):
  if off_map(loc, M):
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
