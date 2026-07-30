import re

def main():
  D = 50
  CLICK_ON_0 = 0

  with open("input.txt") as f:
    lines = f.readlines()

  for line in lines:
    # if CLICK_ON_0 > 500:
      # break
    match = re.search("(\D)(\d+)", line)
    rotation, distance = match.groups()
    # left is towards lower numbers, right is towards higher numbers
    mult = 1 if rotation == "R" else -1
    distance = mult * int(distance)
    CLICK_ON_0 += len([i for i in range(D, D + distance, mult) if i % 100 == 0])

    D = (D + distance) % 100

  print(CLICK_ON_0)
if __name__ == "__main__":
  main()
