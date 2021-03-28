data = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
""".strip().splitlines()

# data = """
# 16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4
# """.strip().splitlines()

FILE_IN = "input.txt"

with open(FILE_IN, 'r') as f: data = f.read().splitlines()

# input
data = [0] + [int(d) for d in data]
data.sort()
data = set(data)

# processed data
current_jolts = 0
adapters_available = True
jolts_usage = {
    1: 0,
    2: 0,
    3: 0,
}

def check_and_add_jolt_counter(jolts):
    global current_jolts
    global jolts_usage

    if (current_jolts + jolts) in data:
        current_jolts += jolts
        jolts_usage[jolts] += 1
        return True
    return False

# algorithm
while adapters_available:

    if check_and_add_jolt_counter(1):
        pass
    elif check_and_add_jolt_counter(2):
        pass
    elif check_and_add_jolt_counter(3):
        pass
    else:
        # count device 3 jolt diff
        current_jolts += 3
        jolts_usage[3] += 1
        adapters_available = False

# output
print("total:%d - one:%d - two:%d - three:%d" % (current_jolts, jolts_usage[1], jolts_usage[2], jolts_usage[3]))
print("mult(1*3):%d" % (jolts_usage[1] * jolts_usage[3],))
print(data)
