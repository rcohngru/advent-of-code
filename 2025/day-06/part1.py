
def main():

  with open("input.txt", "r") as f:
    lines = f.readlines()

  operators = lines[-1].split()
  numerals = [l.split() for l in lines[:-1]]
  numeral_lines = len(numerals)
  problems = []
  for i in range(0, len(operators)):
    nums = []
    op = operators[i]
    for j in range(0, numeral_lines):
      nums.append(int(numerals[j][i]))

    problems.append((op, nums))

  tot = 0
  for op, nums in problems:
    if op == "*":
      ans = 1
    elif op == "+":
      ans = 0

    for n in nums:
      if op == "*":
        ans *= n
      elif op == "+":
        ans += n

    tot += ans
  print(tot)


if __name__ == "__main__":
  main()
