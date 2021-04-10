data = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".strip().splitlines()

FILE_IN = "input.txt"

with open(FILE_IN, 'r') as f: data = f.read().splitlines()

from enum import Enum

class State(Enum):
    FLOOR = "."
    EMPTY = "L"
    OCCUPIED = "#"

# process data in 2d array

table = []
for line in data:
    state_line = [State(char) for char in line]
    table.append(state_line)


class PuzzleBoi:

    directions = [
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, 1),
        # (0, 0) self
        (0, -1),
        (1, 1),
        (1, 0),
        (1, -1)
    ]

    def __init__(self, floor_plan):
        self.floor_plan = floor_plan
        self.max_x = len(self.floor_plan[0])
        self.max_y = len(self.floor_plan)

    def get_state_in_visual_direction(self, start_x, start_y, direction_x, direction_y):
        while True:
            if (start_x + direction_x) < 0 or (start_y + direction_y) < 0:
                raise IndexError()
            check = self.floor_plan[start_x + direction_x][start_y + direction_y]
            if check != State.FLOOR:
                return check
            start_x += direction_x
            start_y += direction_y


    def _execute_if_empty(self, x, y) -> State:
        for dire_x, dire_y in PuzzleBoi.directions:
            try:
                if self.get_state_in_visual_direction(x, y, dire_x, dire_y) == State.OCCUPIED:
                    return self.floor_plan[x][y]
            except IndexError:
                pass
        return State.OCCUPIED

    def _execute_if_occupied(self, x, y) -> State:
        adjacent_occupied = 0
        for dire_x, dire_y in PuzzleBoi.directions:
            try:
                if self.get_state_in_visual_direction(x, y, dire_x, dire_y) == State.OCCUPIED:
                    adjacent_occupied += 1
            except IndexError:
                pass
        if adjacent_occupied >= 5:
            return State.EMPTY
        return self.floor_plan[x][y]

    def _execute(self, x, y):
        cases = {
            State.FLOOR: lambda _, __: State.FLOOR,
            State.EMPTY: self._execute_if_empty,
            State.OCCUPIED: self._execute_if_occupied,
        }
        return cases[self.floor_plan[x][y]](x, y)

    def execute(self):
        new_plan = []

        for x in range(len(self.floor_plan)):
            new_line = []
            for y in range(len(self.floor_plan[x])):
                new_line.append(self._execute(x, y))
            new_plan.append(new_line)

        return new_plan

    def print(self):
        print("-----NEW------")
        for line in self.floor_plan:
            print("".join([c.value for c in line]))

    @property
    def occupied_seats(self):
        total = 0
        for line in self.floor_plan:
            for char in line:
                total += int(char == State.OCCUPIED)
        return total


pb = PuzzleBoi(table)
prev = 0
while True:
    pb = PuzzleBoi(pb.execute()) #: round n
    pb.print()
    if prev == pb.occupied_seats:
        break
    prev = pb.occupied_seats

print(pb.occupied_seats)