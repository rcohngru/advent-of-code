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

  matches = re.findall("mul\(\d{1,3},\d{1,3}\)", input)
  return matches

if __name__ == "__main__":
  main()
