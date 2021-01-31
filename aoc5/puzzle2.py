FILE_IN = "input.txt"

with open(FILE_IN, 'r') as f:
    data = f.read().splitlines()


def cmp_startswith_most_bs(inp):
    i = 0
    for c in inp:
        if c == "B":
            i += 1
        else:
            break
    return i

def bubble(string_input, move_low_c, move_high_c):
    total = 1 << len(string_input)
    low = 0
    high = total - 1
    for c in string_input:
        total = int(total / 2)
        if c == move_high_c:
            low += total
        elif c == move_low_c:
            high -= total
    return low


data = sorted(data, key=cmp_startswith_most_bs, reverse=True)

string = ""
string_low = ""
highest = 0
lowest = 1000

seatids = []

for s in data:
    row = bubble(s[:7], "F", "B")
    column = bubble(s[7:], "L", "R")

    seatid = row * 8 + column
    if seatid > highest:
        highest = seatid
        string = s
    elif seatid < lowest:
        lowest = seatid
        string_low = s
    seatids.append(seatid)

print("highest:%s,string:%s" % (highest, string))
print("lowest:%s,string:%s" % (lowest, string_low))

for r in range(lowest, highest):
    if r not in seatids:
        print(r)