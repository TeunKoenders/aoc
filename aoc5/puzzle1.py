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
highest = 0



for s in data:
    if not s.startswith("BBB"):
        continue  #: don't bother (atleast for my list)
    row = bubble(s[:7], "F", "B")
    column = bubble(s[7:], "L", "R")

    seatid = row * 8 + column
    print("str:%s,row:%s,column:%s,seatid:%s" % (s, row, column, seatid))
    if seatid > highest:
        highest = seatid
        string = s

print("highest:%s,string:%s" % (highest, string))