
def main():

  with open("input.txt", "r") as f:
    lines = f.readlines()
  # print(lines)
  # a new problem is denoted by there being a character in the operator line
  # each line is going to have the same length.
  # starting from right, move a scanning column backwards, scanning each line to build out the numbers
  # once we reach an operator column, we know the problem is complete

  operators = lines[-1].strip("\n")
  numerals = [l.strip("\n") for l in lines[:-1]]
  row_lengths = [len(operators)] + [len(n) for n in numerals]
  curr_col = max(row_lengths) - 1
  problems = []
  operator_col = False
  nums = []
  op = None
  while curr_col >= 0:
    if curr_col < len(operators) and operators[curr_col] in ["*", "+"]:
      operator_col = True
      op = operators[curr_col]

    num = ""
    for n in numerals:
      if curr_col < len(n):
        num += n[curr_col]

    nums.append(int(num))

    if operator_col:
      problems.append((op, nums))
      nums = []
      operator_col = False
      # skip over blank space col
      curr_col -= 1

    curr_col -= 1

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
