def main():
  print("------------- Part 1 -------------")
  part_1()
  print("------------- Part 2 -------------")
  part_2()


def part_1():
  lines = ingest_file("input.txt")
  symbols, numbers = parse_lines(lines)

  valid_numbers = []
  symbol_locations = set([symbol.location for symbol in symbols])
  for number in numbers:
    if len(number.adjacent_spots.intersection(symbol_locations)) > 0:
      valid_numbers.append(number.number)

  sol = f"{sum(valid_numbers)}"
  print(f"The solution for Part 1 is: {sol}")

def part_2():
  lines = ingest_file("input.txt")
  symbols, numbers = parse_lines(lines)

  gear_ratio_sum = 0
  for symbol in symbols:
    if symbol.symbol != "*":
      continue

    possible_gears = []
    for number in numbers:
      if symbol.location in number.adjacent_spots:
        possible_gears.append(number.number)

    if len(possible_gears) == 2:
      gear_ratio_sum += possible_gears[0] * possible_gears[1]

  sol = f"{gear_ratio_sum}"
  print(f"The solution for Part 2 is: {sol}")

class Symbol:
  def __init__(self, symbol, row, col):
    self.symbol = symbol
    self.row = row
    self.col = col
    self.location = (row, col)

  def __repr__(self):
    return f"{self.symbol}: ({self.row}, {self.col})"

class Number:
  def __init__(self, number, row, start_col, end_col):
    self.number = number
    self.row = row
    self.start_col = start_col
    self.end_col = end_col

    self.adjacent_spots = set()
    for i in range(start_col - 1, end_col + 2):
      self.adjacent_spots.add((row - 1, i))
      self.adjacent_spots.add((row, i))
      self.adjacent_spots.add((row + 1, i))

  def location_is_adjacent(self, loc):
    return loc in self.adjacent_spots

  def __repr__(self):
    return f"{self.number}: ({self.row}, {self.start_col}-{self.end_col})"

def ingest_file(file):
    f = open(file, "r")
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines

def parse_lines(lines):
  symbols = []
  numbers = []
  for row, line in enumerate(lines):
    in_num = False
    building_num = ""
    num_start = 0

    for col, c in enumerate(line):
      if c.isdigit() and not in_num:
        in_num = True
        num_start = col
        building_num += c
        continue

      if c.isdigit() and in_num:
        building_num += c
        continue

      if not c.isdigit() and in_num:
        numbers.append(Number(
          number=int(building_num),
          row=row,
          start_col=num_start,
          end_col=col-1
        ))
        in_num = False
        num_start = 0
        building_num = ""

      if c != ".":
        symbols.append(Symbol(
          symbol=c,
          row=row,
          col=col
        ))

    if in_num:
      numbers.append(Number(
          number=int(building_num),
          row=row,
          start_col=num_start,
          end_col=col
        ))
  return symbols, numbers

if __name__ == "__main__":
  main()
