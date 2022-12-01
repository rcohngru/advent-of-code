import re

def main():
  # M : a list of tokens from the input that match the pattern: mul(X,Y)
  M = parse_input()
  total = 0
  for m in M:
    x, y = re.findall('\d{1,3}', m)

    total += int(x) * int(y)

  print(total)

def parse_input():
  with open("input.txt", "r") as f:
    input = f.read()

  # split the input data on one of "do()" or "don't()"
  # this will create a list that looks like so:
  # [s0, None, "don't()", s1, "do()", None, ...]
  # we know that initially the data starts out as "do"
  # so s0 can be parsed for matches. From there, we can
  # iterate through list three steps at a time to determine
  # if sN is valid for matches, based on whether the preceding
  # spots are None for the DO section or the DON'T section
  data = re.split("(do\(\))|(don't\(\))", input)

  mul_tok = "mul\(\d{1,3},\d{1,3}\)"

  matches = re.findall(mul_tok, data[0])
  for i in range(1, len(data), 3):
    do = data[i]
    dont = data[i + 1]
    s = data[i + 2]
    if do:
      m = re.findall(mul_tok, s)
      matches.extend(m)

  return matches

if __name__ == "__main__":
  main()
