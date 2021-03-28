from collections import defaultdict

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
data = [int(d) for d in data]
data.sort()

total_branches = defaultdict(int)
total_branches[0] = 1  # always start with one branch


def get_number_of_branches_at_outlet_value(outlet_value):
    if outlet_value in total_branches:
        return total_branches[outlet_value]
    return 0

for outlet_value in data:
    total_branches[outlet_value] += get_number_of_branches_at_outlet_value(outlet_value - 1)
    total_branches[outlet_value] += get_number_of_branches_at_outlet_value(outlet_value - 2)
    total_branches[outlet_value] += get_number_of_branches_at_outlet_value(outlet_value - 3)

print(total_branches[max(data)]) # pffft, finally