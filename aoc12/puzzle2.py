FILE_IN = "input.txt"

with open(FILE_IN, 'r') as file: data = file.read().splitlines()

class Compass:

    def __init__(self):
        self.north = 0
        self.east = 0
        self.waypoint_north = 1
        self.waypoint_east = 10

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
        self.waypoint_north += north

    def add_east(self, east):
        self.waypoint_east += east

    def turn(self, left):
        directions = {
            90: lambda n, e: (e, n * -1),
            -270: lambda n, e: (e, n * -1),
            180: lambda n, e: (n * -1, e * -1),
            -180: lambda n, e: (n * -1, e * -1),
            270: lambda n, e: (e * - 1, n),
            -90: lambda n, e: (e * - 1, n),
        }
        self.waypoint_north, self.waypoint_east = directions[left](self.waypoint_north, self.waypoint_east)

    def go_forward(self, forward):
        self.north += self.waypoint_north * forward
        self.east += self.waypoint_east * forward

    @property
    def manhattan_distance(self):
        return abs(self.north) + abs(self.east)


c = Compass()
for instruct in data:
    c.execute_instruction(instruct)

print(c.manhattan_distance)
