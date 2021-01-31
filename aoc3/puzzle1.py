FILE_IN = "input.txt"
TREE = "#"
SLOPE = 3

data = []
with open(FILE_IN, 'r') as f:
    for line in f.read().splitlines():
        # e.g.: ...#...###......##.#..#.....##.
        trees = [char == TREE for char in line]
        data.append(trees)

treeline_width = len(data[0])  # modulo this 
print("width: %s" % treeline_width)
curr_x = 0

total = 0
for treeline in data:
    if treeline[curr_x % treeline_width]:
        total += 1
    curr_x += SLOPE

print("total trees: %s" % total)