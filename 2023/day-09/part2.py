import re

def main():
  L = parse_input()

  tot = 0
  for l in L:
    inc = find_history(l)
    tot += l[0] - inc

  print(tot)


def find_history(seq):
  diff = [seq[i] - seq[i-1] for i in range(1, len(seq))]
  if all(d == 0 for d in diff):
    return diff[0]
  else:
    return diff[0] - find_history(diff)

def parse_input():
  with open("input.txt", "r") as f:
    lines = f.readlines()

  L = [list(map(int, re.findall("-?\d+", l))) for l in lines]
  return L

if __name__ == "__main__":
  main()
