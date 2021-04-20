FILE_IN = "input.txt"

with open(FILE_IN, 'r') as file: data = file.read().splitlines()

class Compass:

    def __init__(self):
        self.north = 0
        self.east = 0
        self._direction = 270

    def execute_instruction(self, instruction):
        action = instruction[0]
        amount = int(instruction[1:])

        actions = {
            "N": lambda n: self.add_north(n),
            "S": lambda s: self.add_north(s * -1),
            "E": lambda e: self.add_east(e),
            "W": lambda w: self.add_east(w * -1),
            "L": lambda l: self.turn(l),
            "R": lambda r: self.turn(r * -1),
            "F": lambda f: self.go_forward(f)
        }
        actions[action](amount)

    def add_north(self, north):
        self.north += north

    def add_east(self, east):
        self.east += east

    def turn(self, left):
        self._direction += left

    def go_forward(self, forward):
        directions = {
            0: lambda n: self.add_north(n),
            90: lambda w: self.add_east(w * -1),
            180: lambda s: self.add_north(s * -1),
            270: lambda e: self.add_east(e),
        }
        directions[self.direction](forward)

    @property
    def direction(self):
        return self._direction % 360

    @property
    def manhattan_distance(self):
        return abs(self.north) + abs(self.east)


c = Compass()
for instruct in data:
    c.execute_instruction(instruct)

print(c.manhattan_distance)
