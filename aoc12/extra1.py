import random
import locale
import curses
import time
from puzzle1 import Compass, data


class Ocean:

    WAVE = "~"

    def __init__(self, width=51, length=21, waviness=20):
        self.width = width
        self.length = length
        self.waviness = waviness

        self.middle = (int(self.width/2), int(self.length/2))
        self.as_2d_array = self._init_ocean()

    def _init_ocean(self):
        lines = []
        for l in range(0, self.length):
            line = []
            for w in range(0, self.width):
                line.append(self.WAVE if random.randint(0, self.waviness) == 0 else " ")
            lines.append(line)
        return lines

    def move_ocean_west(self):
        curr_ocean = self.as_2d_array.copy()

        for line in curr_ocean:
            line.insert(0, line.pop())

        self.as_2d_array = curr_ocean

    def move_ocean_east(self):
        curr_ocean = self.as_2d_array.copy()

        for line in curr_ocean:
            line.append(line.pop(0))

        self.as_2d_array = curr_ocean

    def move_ocean_south(self):
        curr_ocean = self.as_2d_array.copy()
        curr_ocean.append(curr_ocean.pop(0))
        self.as_2d_array = curr_ocean

    def move_ocean_north(self):
        curr_ocean = self.as_2d_array.copy()
        curr_ocean.insert(0, curr_ocean.pop())
        self.as_2d_array = curr_ocean

    def draw(self, screen):
        for w in range(self.width):
            for l in range(self.length):
                screen.addch(l, w, self.as_2d_array[l][w])
        screen.addstr(self.middle[1], self.middle[0], boats[c.direction].encode('utf-8'))
        screen.addstr(1, 1, "--=%sN,%sE=--" % (c.north, c.east))
        screen.refresh()
        time.sleep(.02)

boats = {
    0: chr(0x2191),
    90: chr(0x2190),
    180: chr(0x2193),
    270: chr(0x2192),
}

c = Compass()

def curses_program(screen: curses.window):
    y, x = screen.getmaxyx()
    o = Ocean(x - 1, y - 1)
    screen.clear()
    curses.resizeterm(y, x)

    for instruct in data:
        screen.clear()
        curr_north, curr_east = c.north, c.east
        c.execute_instruction(instruct)
        new_north, new_east = c.north, c.east

        if new_north < curr_north:
            for i in range(abs(curr_north - new_north)):
                o.move_ocean_south()
                o.draw(screen)
        else:
            for i in range(abs(curr_north - new_north)):
                o.move_ocean_north()
                o.draw(screen)

        if new_east < curr_east:
            for i in range(abs(curr_east - new_east)):
                o.move_ocean_west()
                o.draw(screen)
        else:
            for i in range(abs(curr_east - new_east)):
                o.move_ocean_east()
                o.draw(screen)


locale.setlocale(locale.LC_ALL, "")
curses.wrapper(curses_program)
