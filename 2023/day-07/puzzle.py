def main():
  print("------------- Part 1 -------------")
  part_1()
  print("------------- Part 2 -------------")
  part_2()


def part_1():
  lines = ingest_file("input.txt")
  hands = [(l.split()[0], int(l.split()[1])) for l in lines]
  categories = {
    "five_kind" : [],
    "four_kind" : [],
    "full_house" :[],
    "three_kind" : [],
    "two_pair" : [],
    "one_pair" : [],
    "high_card" : [],
  }

  for hand in hands:
    category = identify_hand_p1(hand[0])
    categories[category] = insert_hand_p1(categories[category], hand)

  mult = 1
  total_winnings = 0
  order = ["high_card", "one_pair", "two_pair", "three_kind", "full_house", "four_kind", "five_kind"]

  for cat in order:
    hands = categories[cat]
    for h in hands[::-1]:
      total_winnings += h[1] * mult
      mult += 1

  sol = f"{total_winnings}"
  print(f"The solution for Part 1 is: {sol}")

def identify_hand_p1(hand):
  char_counts = {}
  for c in hand:
    char_counts[c] = char_counts.get(c, 0) + 1

  char_transpose = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
  }
  for k, v in char_counts.items():
    char_transpose[v].append(k)

  if len(char_transpose[5]) == 1:
    category =  "five_kind"

  elif len(char_transpose[4]) == 1:
    category =  "four_kind"

  elif len(char_transpose[3]) == 1 and len(char_transpose[2]) == 1:
    category =  "full_house"

  elif len(char_transpose[3]) == 1 and len(char_transpose[1]) == 2:
    category =  "three_kind"

  elif len(char_transpose[2]) == 2:
    category =  "two_pair"

  elif len(char_transpose[2]) == 1 and len(char_transpose[1]) == 3:
    category =  "one_pair"

  else:
    category = "high_card"

  return category

def insert_hand_p1(l, hand):
  # hand is tuple containing hand and bet ('HAND', BET)
  # lists are ordered from highest to lowest, comparing each element in hand
  for i in range(len(l)):
    if h1_ge_h2_p1(l[i][0], hand[0]):
      continue
    else:
      l.insert(i, hand)
      return l

  l.append(hand)
  return l

def h1_ge_h2_p1(h1, h2):
  # returns true if h1 is greater than or equal to h2
  cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
  for c1, c2 in zip(h1, h2):

    if cards.index(c1) == cards.index(c2):
      continue
    elif cards.index(c1) < cards.index(c2):
      return True
    else:
      return False

  return True



def part_2():
  lines = ingest_file("input.txt")
  hands = [(l.split()[0], int(l.split()[1])) for l in lines]
  categories = {
    "five_kind" : [],
    "four_kind" : [],
    "full_house" :[],
    "three_kind" : [],
    "two_pair" : [],
    "one_pair" : [],
    "high_card" : [],
  }

  for hand in hands:
    category = identify_hand_p2(hand[0])
    categories[category] = insert_hand_p2(categories[category], hand)

  mult = 1
  total_winnings = 0
  order = ["high_card", "one_pair", "two_pair", "three_kind", "full_house", "four_kind", "five_kind"]

  for cat in order:
    hands = categories[cat]
    for h in hands[::-1]:
      total_winnings += h[1] * mult
      mult += 1

  sol = f"{total_winnings}"
  print(f"The solution for Part 2 is: {sol}")

def identify_hand_p2(hand):
  char_counts = {}
  joker_count = 0
  for c in hand:
    if c == 'J':
      joker_count += 1
    else:
      char_counts[c] = char_counts.get(c, 0) + 1

  char_transpose = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
  }

  max_dupes = 0
  for k, v in char_counts.items():
    char_transpose[v].append(k)
    if v >= max_dupes:
      max_dupes = v

  # hand with all J's
  if max_dupes == 0:
    char_transpose[5].append('J')
  else:
    wc_add = char_transpose[max_dupes].pop()
    char_transpose[max_dupes + joker_count].append(wc_add)

  if len(char_transpose[5]) == 1:
    category =  "five_kind"

  elif len(char_transpose[4]) == 1:
    category =  "four_kind"

  elif len(char_transpose[3]) == 1 and len(char_transpose[2]) == 1:
    category =  "full_house"

  elif len(char_transpose[3]) == 1 and len(char_transpose[1]) == 2:
    category =  "three_kind"

  elif len(char_transpose[2]) == 2:
    category =  "two_pair"

  elif len(char_transpose[2]) == 1 and len(char_transpose[1]) == 3:
    category =  "one_pair"

  else:
    category = "high_card"

  return category

def insert_hand_p2(l, hand):
  # hand is tuple containing hand and bet ('HAND', BET)
  # lists are ordered from highest to lowest, comparing each element in hand
  for i in range(len(l)):
    if h1_ge_h2_p2(l[i][0], hand[0]):
      continue
    else:
      l.insert(i, hand)
      return l

  l.append(hand)
  return l

def h1_ge_h2_p2(h1, h2):
  # returns true if h1 is greater than or equal to h2
  cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
  for c1, c2 in zip(h1, h2):

    if cards.index(c1) == cards.index(c2):
      continue
    elif cards.index(c1) < cards.index(c2):
      return True
    else:
      return False

  return True

def ingest_file(file):
    f = open(file, "r")
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines

if __name__ == "__main__":
  main()
