import copy
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

OPPOSITE = {
  UP: DOWN,
  DOWN: UP,
  LEFT: RIGHT,
  RIGHT: LEFT
}

ROBOT = "@"
BOX = "O"
BOX_LEFT = "["
BOX_RIGHT = "]"
WALL = "#"
EMPTY = '.'

"""
The move functionality here is really messy and could use some work.

But the basic idea works similar to the method from part 1. I kind of
cheat a little bit by using a deep copy of the state when recursing to check
the box movements up and down, but I'm too lazy to think through an
actual solve.

"""


class Warehouse:
  def __init__(self, state, robot_position):
    self.initial_state = state
    self.initial_pos = robot_position

    self.state = state
    self.pos = robot_position
    self.save_state = state

  def check_box(self, l, r, direction):
    if direction == LEFT:
      next_pos = (l[0] + DELTAS[direction][0], l[1] + DELTAS[direction][1])
      adj_object = self.state[next_pos[0]][next_pos[1]]

      if adj_object == WALL:
        return False

      elif adj_object == EMPTY:
        self.state[next_pos[0]][next_pos[1]] = BOX_LEFT
        self.state[l[0]][l[1]] = BOX_RIGHT
        self.state[r[0]][r[1]] = EMPTY
        return True

      else:
        next_l = (l[0] + 2 * DELTAS[direction][0], l[1] + 2 * DELTAS[direction][1])
        next_r = (l[0] + DELTAS[direction][0], l[1] + DELTAS[direction][1])
        can_move = self.check_box(next_l, next_r, direction)
        if can_move:
          self.state[next_pos[0]][next_pos[1]] = BOX_LEFT
          self.state[l[0]][l[1]] = BOX_RIGHT
          self.state[r[0]][r[1]] = EMPTY
          return True
        else:
          return False

    if direction == RIGHT:
      next_pos = (r[0] + DELTAS[direction][0], r[1] + DELTAS[direction][1])
      adj_object = self.state[next_pos[0]][next_pos[1]]

      if adj_object == WALL:
        return False

      elif adj_object == EMPTY:
        self.state[next_pos[0]][next_pos[1]] = BOX_RIGHT
        self.state[r[0]][r[1]] = BOX_LEFT
        self.state[l[0]][l[1]] = EMPTY
        return True

      else:
        next_r = (r[0] + 2 * DELTAS[direction][0], r[1] + 2 * DELTAS[direction][1])
        next_l = (r[0] + DELTAS[direction][0], r[1] + DELTAS[direction][1])
        can_move = self.check_box(next_l, next_r, direction)
        if can_move:
          self.state[next_pos[0]][next_pos[1]] = BOX_RIGHT
          self.state[r[0]][r[1]] = BOX_LEFT
          self.state[l[0]][l[1]] = EMPTY
          return True
        else:
          return False

    if direction == UP or direction == DOWN:
      l_next = (l[0] + DELTAS[direction][0], l[1] + DELTAS[direction][1])
      r_next = (r[0] + DELTAS[direction][0], r[1] + DELTAS[direction][1])

      l_adj = self.state[l_next[0]][l_next[1]]
      r_adj = self.state[r_next[0]][r_next[1]]

      if l_adj == WALL or r_adj == WALL:
        return False
      elif l_adj == EMPTY and r_adj == EMPTY:
        self.state[l_next[0]][l_next[1]] = BOX_LEFT
        self.state[r_next[0]][r_next[1]] = BOX_RIGHT
        self.state[l[0]][l[1]] = EMPTY
        self.state[r[0]][r[1]] = EMPTY
        return True
      else:
        if l_adj == BOX_LEFT and r_adj == BOX_RIGHT:
          can_move = self.check_box(l_next, r_next, direction)
          if can_move:
            self.state[l_next[0]][l_next[1]] = BOX_LEFT
            self.state[r_next[0]][r_next[1]] = BOX_RIGHT
            self.state[l[0]][l[1]] = EMPTY
            self.state[r[0]][r[1]] = EMPTY
            return True
          else:
            return False

        elif l_adj == BOX_RIGHT and r_adj == BOX_LEFT:
          l_next_l = (l_next[0] + DELTAS[LEFT][0], l[1] + DELTAS[LEFT][1])
          r_next_r = (r_next[0] + DELTAS[RIGHT][0], r[1] + DELTAS[RIGHT][1])

          save_state = copy.deepcopy(self.state)
          cm1 = self.check_box(l_next_l, l_next, direction)
          cm2 = self.check_box(r_next, r_next_r, direction)
          if cm1 and cm2:
            self.state[l_next[0]][l_next[1]] = BOX_LEFT
            self.state[r_next[0]][r_next[1]] = BOX_RIGHT
            self.state[l[0]][l[1]] = EMPTY
            self.state[r[0]][r[1]] = EMPTY
            return True
          else:
            self.state = save_state
            return False
        elif l_adj == BOX_RIGHT and r_adj == EMPTY:
          l_next_l = (l_next[0] + DELTAS[LEFT][0], l[1] + DELTAS[LEFT][1])
          save_state = copy.deepcopy(self.state)
          cm1 = self.check_box(l_next_l, l_next, direction)
          if cm1:
            self.state[l_next[0]][l_next[1]] = BOX_LEFT
            self.state[r_next[0]][r_next[1]] = BOX_RIGHT
            self.state[l[0]][l[1]] = EMPTY
            self.state[r[0]][r[1]] = EMPTY
            return True
          else:
            self.state = save_state
            return False
        elif r_adj == BOX_LEFT and l_adj == EMPTY:
          r_next_r = (r_next[0] + DELTAS[RIGHT][0], r[1] + DELTAS[RIGHT][1])
          save_state = copy.deepcopy(self.state)
          cm1 = self.check_box(r_next, r_next_r, direction)
          if cm1:
            self.state[l_next[0]][l_next[1]] = BOX_LEFT
            self.state[r_next[0]][r_next[1]] = BOX_RIGHT
            self.state[l[0]][l[1]] = EMPTY
            self.state[r[0]][r[1]] = EMPTY
            return True
          else:
            self.state = save_state
            return False





  def move(self, direction):
    next_pos = (self.pos[0] + DELTAS[direction][0], self.pos[1] + DELTAS[direction][1])

    adj_object = self.state[next_pos[0]][next_pos[1]]
    if adj_object == EMPTY:
      self.state[next_pos[0]][next_pos[1]] = ROBOT
      self.state[self.pos[0]][self.pos[1]] = EMPTY
      self.pos = next_pos
    elif adj_object == BOX_RIGHT and direction == LEFT:
      l = (next_pos[0] + DELTAS[direction][0], next_pos[1] + DELTAS[direction][1])
      r = next_pos
      can_move = self.check_box(l, r, direction)
      if can_move:
        self.state[next_pos[0]][next_pos[1]] = ROBOT
        self.state[self.pos[0]][self.pos[1]] = EMPTY
        self.pos = next_pos
    elif adj_object == BOX_LEFT and direction == RIGHT:
      r = (next_pos[0] + DELTAS[direction][0], next_pos[1] + DELTAS[direction][1])
      l = next_pos
      can_move = self.check_box(l, r, direction)
      if can_move:
        self.state[next_pos[0]][next_pos[1]] = ROBOT
        self.state[self.pos[0]][self.pos[1]] = EMPTY
        self.pos = next_pos
    elif direction in (UP, DOWN) and adj_object in (BOX_LEFT, BOX_RIGHT):
      if adj_object == BOX_LEFT:
        l = next_pos
        r = (next_pos[0] + DELTAS[RIGHT][0], next_pos[1] + DELTAS[RIGHT][1])
      else:
        r = next_pos
        l = (next_pos[0] + DELTAS[LEFT][0], next_pos[1] + DELTAS[LEFT][1])

      can_move = self.check_box(l, r, direction)
      if can_move:
        self.state[next_pos[0]][next_pos[1]] = ROBOT
        self.state[self.pos[0]][self.pos[1]] = EMPTY
        self.pos = next_pos


  def disp(self, state = None):
    if state != None:
      s = state
    else:
      s = self.state

    for row in s:
      print("".join(row))

    print()

  def compute_boxes_coordinates(self):
    boxes = []
    for i in range(len(self.state)):
      for j in range(len(self.state[0])):
        obj = self.state[i][j]
        if obj == BOX_LEFT:
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
        s.append(ROBOT)
        s.append(EMPTY)
      elif c == BOX:
        s.append(BOX_LEFT)
        s.append(BOX_RIGHT)
      else:
        s.append(c)
        s.append(c)

    state.append(s)

  for i in range(len(state)):
    s = []
    for j in range(len(state[0])):
      c = state[i][j]
      if c == ROBOT:
        pos = (i, j)

  directions = "".join(data.split("\n\n")[1].split())
  return pos, state, directions

if __name__ == "__main__":
  main()
