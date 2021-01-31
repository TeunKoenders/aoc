import sys
FILE_IN = "input.txt"
TREE = "#"
try:
    SLOPE = sys.argv[1]
    Y_SLOPE = sys.argv[2]
except IndexError:
    SLOPE = 3
    Y_SLOPE = 1

data = []
with open(FILE_IN, 'r') as f:
    for line in f.read().splitlines():
        # e.g.: ...#...###......##.#..#.....##.
        trees = [char == TREE for char in line]
        data.append(trees)

treeline_width = len(data[0])  # modulo this 
treeline_length = len(data)

print("slope: %s, %s" % (SLOPE, Y_SLOPE))
print("width: %s" % treeline_width)
print("length: %s" % treeline_length)
curr_x = 0
curr_y = 0
total = 0

while curr_y < treeline_length:
    if data[curr_y][curr_x % treeline_width]:
        total += 1
    curr_x += SLOPE
    curr_y += Y_SLOPE 

print("total trees: %s" % total)