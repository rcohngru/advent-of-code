
MIN_DIFF = 1
MAX_DIFF = 3

def main():
  # L: a list of reports, where each report is a list of integer values
  L = parse_input()

  safe_reports = 0
  for l in L:
    for i in range(len(l)):
      l_copy = l.copy()
      l_copy.pop(i)
      if (
        ((sorted(l_copy) == l_copy)
          or
        (sorted(l_copy, reverse=True) == l_copy))
        and all([MIN_DIFF <= abs(l_copy[j] - l_copy[j -1]) <= MAX_DIFF for j in range(1, len(l_copy))])
      ):
        safe_reports += 1
        break

  print(safe_reports)


def parse_input():
  with open("input.txt", "r") as f:
    lines = f.readlines()

  L = []
  for line in lines:
    L.append([int(l) for l in line.split()])

  return L


if __name__ == "__main__":
  main()
