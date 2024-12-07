import re

from typing import List
from itertools import product

class Equation:
  def __init__(self, value: int, numbers: List[int]):
    self.value = value
    self.numbers = numbers

    num_operators = len(numbers) - 1
    # using 'C' to represent '||' as a single character -- C means concatenation
    # this results in 3^N combinations (yikes) but i dont want to optimize
    self.operators = list(product('*+C', repeat = num_operators))

    self.valid_operators = []
    self.balanceable = False
    for ops in self.operators:
      val = self.evaluate_operators(ops)
      if val == self.value:
        self.valid_operators.append(ops)
        self.balanceable = True


  def __repr__(self):
    return f'{self.value}: {self.numbers}'

  def evaluate_operators(self, operators: List[str]):
    if len(operators) != len(self.numbers) - 1:
      raise Exception("Incorrect number of operators for numbers")

    n1 = self.numbers[0]
    for i in range(len(operators)):
      n2 = self.numbers[i + 1]
      op = operators[i]

      if op == "*":
        n1 *= n2
      if op == "+":
        n1 += n2
      if op == 'C':
        n1 = int(str(n1) + str(n2))

    return n1


def main():
  eqs = parse_input()

  tot = 0
  for eq in eqs:
    if eq.balanceable:
      tot += eq.value

  print(tot)


def parse_input():
  with open("input.txt", "r") as f:
    lines = f.readlines()

  eqs = []
  for line in lines:
    val = int(line.split(":")[0])
    nums = list(map(int, re.findall('\d+', line.split(":")[1])))
    eqs.append(Equation(val, nums))

  return eqs

if __name__ == "__main__":
  main()

