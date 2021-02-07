FILE_IN = "input.txt"


data = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""".strip().splitlines()

with open(FILE_IN, 'r') as f: data = f.read().splitlines()

data = [int(d) for d in data]

preamble_groups = []
PREAMBLE_LENGTH = 25


for i in range(len(data) - PREAMBLE_LENGTH + 1):
    group = data[i:i+PREAMBLE_LENGTH]
    tmp = set()
    for x in range(PREAMBLE_LENGTH):
        for x_ex_x in range(PREAMBLE_LENGTH):
            if x == x_ex_x:
                continue
            tmp.add(group[x] + group[x_ex_x])
    preamble_groups.append(tmp)


for i in range(len(data) - PREAMBLE_LENGTH):
    nr = data[i + PREAMBLE_LENGTH]
    group = preamble_groups[i]
    if nr not in preamble_groups[i]:
        print("%s" % nr)  #: 1398413738
