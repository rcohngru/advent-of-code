def main():
  print("------------- Part 1 -------------")
  part_1()
  print("------------- Part 2 -------------")
  part_2()


def part_1():
  lines = ingest_file("input.txt")
  constraints = {
    "red": 12,
    "green": 13,
    "blue": 14
  }
  possible_game_sum = 0
  for line in lines:
    game = Game(input=line)
    if game.is_possible_game(constraints):
      possible_game_sum += game.game_id

  sol = f"{possible_game_sum}"
  print(f"The solution for Part 1 is: {sol}")

def part_2():
  lines = ingest_file("input.txt")
  power_sum = 0
  for line in lines:
    game = Game(input=line)
    min_cubes = game.min_cubes_required()
    power = 1
    for k, v in min_cubes.items():
      power *= v

    power_sum += power

  sol = f"{power_sum}"
  print(f"The solution for Part 2 is: {sol}")

def ingest_file(file):
    f = open(file, "r")
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines

class Game:
  def __init__(self, input):
    self.game_id = int(input.split(":")[0].split(" ")[-1])
    self.rounds = []
    rounds = input.split(":")[1].split(";")
    for round in rounds:
      sets = round.split(",")
      round_set = {}
      for s in sets:
        num = s.strip().split(" ")[0].strip()
        color = s.strip().split(" ")[1].strip()
        round_set[color] = int(num)
      self.rounds.append(round_set)

  def metadata(self):
    print(f"Game {self.game_id}: {len(self.rounds)}")
    print(f"Rounds: {self.rounds}")

  def is_possible_game(self, constraints):
    for round in self.rounds:
      if not self.is_possible_round(round, constraints):
        return False

    return True

  def is_possible_round(self, round, constraints):
    for k in round.keys():
      if constraints[k] < round[k]:
        return False

    return True

  def min_cubes_required(self):
    min_set = {}
    for round in self.rounds:
      for k in round.keys():
        if round[k] > min_set.get(k, 0):
          min_set[k] = round[k]

    return min_set

if __name__ == "__main__":
  main()
