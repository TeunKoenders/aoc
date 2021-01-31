FILE_IN = "input.txt"
SUM = 2020
MIDDLE = SUM/3

with open(FILE_IN, 'r') as f:
    data = [int(x) for x in f.read().splitlines()]

def cmp(x):
    x = MIDDLE - x
    x = x * (-1 if x < 0 else 1)
    return x

data = sorted(data, key=cmp)
print(data)

maximum = 0
combination = (0,0)

for x in data:
    for y in data:
        for z in data:
            if (x+y+z) == SUM:
                if (x*y*z) > maximum:
                    combination = x, y, z
                    maximum = (x*y*z)
                    print("max: %s (%s * %s * %s)" % (maximum, *combination))


print("max: %s (%s * %s * %s)" % (maximum, *combination))