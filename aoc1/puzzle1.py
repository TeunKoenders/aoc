FILE_IN = "input.txt"
SUM = 2020
MIDDLE = SUM/2

with open(FILE_IN, 'r') as f:
    data = [int(x) for x in f.read().splitlines()]

# I read some math article that the highest multiplication is given when 
# you divide into equal numbers so for 2020 and with two numbers you get 
# 1010 * 1010
# my approach is similar. first sort the list so that the first numbers
# are closest to 1010 -> this way we get to those numbers the fastest. 
# I kept the complete loop so that we can see that only the first match is printed out
# inside out (start with 2020/2 * 2020/2 and move out)

def cmp(x):
    # -20 = 1010 - 1030
    x = MIDDLE - x
    # 
    x = x * (-1 if x < 0 else 1)
    return x

data = sorted(data, key=cmp)
print(data)

maximum = 0
combination = (0,0)

for x in data:
    for y in data:
        if (x+y) == SUM:  # should be 2020 combined
            if (x*y) > maximum:  # save the highest possible (will only print one max because we did the sort)
                combination = x, y 
                maximum = (x*y)
                print("max: %s (%s * %s)" % (maximum, *combination))


print("max: %s (%s * %s)" % (maximum, *combination))