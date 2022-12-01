def main():
  print("------------- Part 1 -------------")
  part_1()
  print("------------- Part 2 -------------")
  part_2()


def part_1():
  lines = ingest_file("input.txt")
  cards = build_cards(lines)
  sol = f"{sum([card.points for card in cards])}"
  print(f"The solution for Part 1 is: {sol}")

def part_2():
  lines = ingest_file("input.txt")
  cards = build_cards(lines)
  for card in cards:
    card_num = card.card_number
    for i in range(1, card.num_winning_numbers + 1):
      cards[card_num + i - 1].copies += card.copies

  total_copies = sum([card.copies for card in cards])

  sol = f"{total_copies}"
  print(f"The solution for Part 2 is: {sol}")

def ingest_file(file):
    f = open(file, "r")
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines

def build_cards(lines):
  cards = []
  for line in lines:
    card_number = int(line.split(":")[0].split()[1])
    winning_numbers = [l.strip() for l in line.split(":")[1].split("|")[0].strip().split()]
    numbers = [l.strip() for l in line.split(":")[1].split("|")[1].strip().split()]
    cards.append(Card(card_number, winning_numbers, numbers))

  return cards

class Card:
  def __init__(self, card_number, winning_numbers, numbers):
    self.card_number = card_number
    self.winners = set(winning_numbers)
    self.numbers = set(numbers)
    self.winning_numbers = self.winners.intersection(self.numbers)
    self.num_winning_numbers = len(self.winning_numbers)
    self.points = pow(2, self.num_winning_numbers - 1) if self.num_winning_numbers > 0 else 0
    self.copies = 1

  def __repr__(self):
    return f"Card {self.card_number}: {self.num_winning_numbers} winning numbers, {self.copies} copies"


if __name__ == "__main__":
  main()
