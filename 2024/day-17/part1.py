import re

class Computer:
  def __init__(self, instructions, A=0, B=0, C=0):
    self.A = A
    self.B = B
    self.C = C
    self.instructions = instructions
    self.instruction_pointer = 0
    self.output = []

  def reg(self):
    print(f"Register A: {self.A}")
    print(f"Register B: {self.B}")
    print(f"Register C: {self.C}")


  def dump(self):
    print(",".join(map(str, self.output)))

  def run(self):
    while self.instruction_pointer < len(self.instructions):
      opcode = self.instructions[self.instruction_pointer]
      operand = self.instructions[self.instruction_pointer + 1]
      self.operation(opcode, operand)

    self.reg()
    self.dump()

  def operation(self, opcode, operand):
    if opcode == 0:
      inc = self.adv(operand)
    elif opcode == 1:
      inc = self.bxl(operand)
    elif opcode == 2:
      inc = self.bst(operand)
    elif opcode == 3:
      inc = self.jnz(operand)
    elif opcode == 4:
      inc = self.bxc(operand)
    elif opcode == 5:
      inc = self.out(operand)
    elif opcode == 6:
      inc = self.bdv(operand)
    elif opcode == 7:
      inc = self.cdv(operand)

    self.instruction_pointer += inc

  def combo_operand(self, operand):
    if operand <= 3:
      return operand
    elif operand == 4:
      return self.A
    elif operand == 5:
      return self.B
    elif operand == 6:
      return self.C
    else:
      return None

  def _dvp(self, operand):
    return int(self.A / (2 ** self.combo_operand(operand)))

  def adv(self, operand):
    self.A = self._dvp(operand)
    return 2

  def bdv(self, operand):
    self.B = self._dvp(operand)
    return 2

  def cdv(self, operand):
    self.C = self._dvp(operand)
    return 2

  def bxl(self, operand):
    self.B = self.B ^ operand
    return 2

  def bst(self, operand):
    self.B = self.combo_operand(operand) % 8
    return 2

  def jnz(self, operand):
    if self.A != 0:
      self.instruction_pointer = operand
      return 0
    return 2

  def bxc(self, operand):
    self.B = self.B ^ self.C
    return 2

  def out(self, operand):
    n1 = self.combo_operand(operand)
    self.output.append(n1 % 8)
    return 2




def main():
  reg, ins = parse_input()
  C = Computer(ins, A=reg[0], B=reg[1], C=reg[2])
  C.run()

def parse_input():
  with open("input.txt", "r") as f:
    data = f.read()

  reg = list(map(int, re.findall("Register \w: (\d+)", data)))
  ins = list(map(int, re.findall("Program: (\d[,\d]+)", data)[0].split(",")))
  return reg, ins





if __name__ == "__main__":
  main()
