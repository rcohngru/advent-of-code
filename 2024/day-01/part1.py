from bisect import insort

def main():
  l1, l2 = parse_input()

  sol = 0
  for n1, n2 in zip(l1, l2):
    sol += abs(n1 - n2)

  print(sol)

def parse_input():
  with open("input.txt", "r") as f:
    lines = f.readlines()

  l1, l2 = [], []
  for line in lines:
    n1, n2 = line.split()
    insort(l1, int(n1))
    insort(l2, int(n2))

  return l1, l2

if __name__ == "__main__":
  main()
