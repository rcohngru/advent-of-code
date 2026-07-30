import re

def main():
  DIAL_NUMBER = 50
  DIAL_ON_0 = 0

  with open("input.txt") as f:
    lines = f.readlines()

  for line in lines:
    match = re.search("(\D)(\d+)", line)
    rotation, distance = match.groups()
    # left is towards lower numbers, right is towards higher numbers
    mult = 1 if rotation == "R" else -1
    DIAL_NUMBER += mult * (int(distance) % 100) # its possible for a full dial spin (or multiple)
    if DIAL_NUMBER < 0:
      DIAL_NUMBER = 100 + DIAL_NUMBER
    elif DIAL_NUMBER > 99:
      DIAL_NUMBER = DIAL_NUMBER - 100

    if DIAL_NUMBER == 0:
      DIAL_ON_0 += 1

  print(DIAL_ON_0)
if __name__ == "__main__":
  main()
