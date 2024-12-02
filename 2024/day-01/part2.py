
def main():
  global L, M
  # L: a list of integers appearing in the left list
  # M: a dictionary containing the number of appearances in the right list
  L, M = parse_input()

  sol = 0
  for n in L:
    sol += n * M.get(n, 0)

  print(sol)


def parse_input():
  with open("input.txt", "r") as f:
    lines = f.readlines()

  L = [] # left list
  M = {} # right list lookup

  for line in lines:
    n1, n2 = line.split()
    L.append(int(n1))
    M[int(n2)] = M.get(int(n2), 0) + 1

  return L, M

if __name__ == "__main__":
  main()
