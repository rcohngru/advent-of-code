
MIN_DIFF = 1
MAX_DIFF = 3

def main():
  # L: a list of reports, where each report is a list of integer values
  L = parse_input()

  safe_reports = 0
  for l in L:
    if (
      ((sorted(l) == l)
        or
      (sorted(l, reverse=True) == l))
      and all([MIN_DIFF <= abs(l[i] - l[i - 1]) <= MAX_DIFF for i in range(1, len(l))])
    ):
      safe_reports += 1

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
