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

  valid_updates = []
  for u in U:
    valid_update = True
    for i in range(len(u) - 1):
      # iterate through numbers in u
      # find all numbers preceding and compare against rules[u]['after']
      # find all numbers succeeding and compare against rules[u]['before']

      num = u[i]
      num_before = set(u[:i])
      num_after = set(u[i + 1:])

      if num in rules:
        before_rules = rules[num]['before']
        after_rules = rules[num]['after']
      else:
        before_rules = set()
        after_rules = set()

      if len(num_before.intersection(before_rules)) > 0 :
        valid_update = False
        break

      if len(num_after.intersection(after_rules)) > 0:
        valid_update = False
        break

    if valid_update:
      valid_updates.append(u)

  sol = 0
  for u in valid_updates:
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
