import re

# This is a system of equations problem. All we need to do is balance the equations
# and solve given the inputs:
#
# A * Xa + B * Xb = Xp
# A * Ya + B * Yb = Yp
# ...
# A = (Xp * Yb - Xb * Yp) / (Xa * Yb - Xb * Ya)
# B = (Xa * Yp - Xp * Ya) / (Xa * Yb - Xb * Ya)
#
# If both A & B are integers, then a solution is possible
#

CONST = 10000000000000

def main():
  # E: is a list of a list of tuples, where each list of tuples represents the
  # XY values for the system of equations
  E = parse_input()
  tot = 0
  for e in E:
    (Xa, Ya), (Xb, Yb), (Xp, Yp) = e

    Xp = CONST + Xp
    Yp = CONST + Yp

    A = (Xp * Yb - Xb * Yp) / (Xa * Yb - Xb * Ya)
    B = (Xa * Yp - Xp * Ya) / (Xa * Yb - Xb * Ya)

    if A.is_integer() and B.is_integer():
      tot += A * 3 + B * 1

  print(tot)


def convert_int(tup):
  return

def parse_input():
  with open("input.txt", "r") as f:
    data = f.read()

  eqs = data.split("\n\n")
  E = []
  for eq in eqs:
    e = re.findall("X.(\d+), Y.(\d+)", eq)
    E.append(list(map(lambda tup: (int(tup[0]), int(tup[1])), e)))

  return E


if __name__ == "__main__":
  main()
