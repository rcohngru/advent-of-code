import re

def main():
  R, U = parse_input()

  rules = {}

  for r in R:
    before, after = r[0], r[1]
    if before not in rules:
      rules[before] = {
        "before": set(),
        "after": set()
      }

    if after not in rules:
      rules[after] = {
        "before": set(),
        "after": set()
      }

    rules[before]["before"].add(after)
    rules[after]["after"].add(before)

  ordered_U = []
  for u in U:
    # iterate through every item in u
    # for each item, determine if the numbers following fit within defined rules
    # if a rule is broken, swap number in current spot with the breaking number
    # continue to validate current spot
    needs_updating = False
    u_copy = u.copy()

    for i in range(len(u) - 1):
      num_i = u_copy[i]
      j = i + 1

      while j < len(u):
        num_j = u_copy[j]

        if num_j in rules[num_i]['after']:
          needs_updating = True
          u_copy[i] = num_j
          u_copy[j] = num_i
          num_i = u_copy[i]
          j = i + 1
          continue

        j += 1


    if needs_updating:
      ordered_U.append(u_copy)

  sol = 0

  for u in ordered_U:
    med = int(len(u) / 2)
    sol += u[med]

  print(sol)

def parse_input():
  with open("input.txt", "r") as f:
    data = f.read()

  rules = [list(map(int, m.group().split('|'))) for m in re.finditer('\d+\|\d+', data)]
  updates = [list(map(int, m.group().split(','))) for m in re.finditer('\d+(,\d+)+', data)]

  return rules, updates

if __name__ == "__main__":
  main()
