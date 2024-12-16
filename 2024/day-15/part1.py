
UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"

DELTAS = {
  UP: (-1, 0),
  DOWN: (1, 0),
  LEFT: (0, -1),
  RIGHT: (0, 1)
}

ROBOT = "@"
BOX = "O"
WALL = "#"
EMPTY = '.'

class Warehouse:
  def __init__(self, state, robot_position):
    self.initial_state = state
    self.initial_pos = robot_position

    self.state = state
    self.pos = robot_position

  def check_box(self, position, direction):
    next_pos = (position[0] + DELTAS[direction][0], position[1] + DELTAS[direction][1])
    adj_object = self.state[next_pos[0]][next_pos[1]]

    if adj_object == WALL:
      return False
    elif adj_object == EMPTY:
      self.state[next_pos[0]][next_pos[1]] = BOX
      self.state[position[0]][position[1]] = EMPTY
      return True
    else:
      can_move = self.check_box(next_pos, direction)
      if can_move:
        self.state[next_pos[0]][next_pos[1]] = BOX
        self.state[position[0]][position[1]] = EMPTY
        return True
      else:
        return False

  def move(self, direction):
    next_pos = (self.pos[0] + DELTAS[direction][0], self.pos[1] + DELTAS[direction][1])

    adj_object = self.state[next_pos[0]][next_pos[1]]

    if adj_object == EMPTY:
      self.state[next_pos[0]][next_pos[1]] = ROBOT
      self.state[self.pos[0]][self.pos[1]] = EMPTY
      self.pos = next_pos
    elif adj_object == BOX:
      can_move = self.check_box(next_pos, direction)
      if can_move:
        self.state[next_pos[0]][next_pos[1]] = ROBOT
        self.state[self.pos[0]][self.pos[1]] = EMPTY
        self.pos = next_pos


  def disp(self):
    for row in self.state:
      print("".join(row))

  def compute_boxes_coordinates(self):
    boxes = []
    for i in range(len(self.state)):
      for j in range(len(self.state[0])):
        obj = self.state[i][j]
        if obj == BOX:
          boxes.append((i, j))

    return boxes


def main():
  pos, state, dirs= parse_input()
  WH = Warehouse(state, pos)

  for d in dirs:
    WH.move(d)

  WH.disp()

  boxes = WH.compute_boxes_coordinates()
  tot = 0
  for box in boxes:
    tot += 100 * box[0] + box[1]

  print(tot)



def parse_input():
  with open("input.txt", "r") as f:
    data = f.read()

  lines = data.split("\n\n")[0].split()
  state = []
  pos = None
  for i, line in enumerate(lines):
    s = []
    for j, c in enumerate(line.strip()):
      if c == ROBOT:
        pos = (i, j)
      s.append(c)

    state.append(s)

  directions = "".join(data.split("\n\n")[1].split())
  return pos, state, directions

if __name__ == "__main__":
  main()
