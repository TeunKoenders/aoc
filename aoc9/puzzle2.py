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

target_nr = 1398413738
i_of_nr = data.index(target_nr)

contiguous_amount = 2

solve_min = 0
solve_max = 0

for _ in range(len(data)):
    for i in range(len(data)):
        spread = data[i:i+contiguous_amount]
        if sum(spread) == target_nr:
            solve_max = max(spread)
            solve_min = min(spread)
            print("between %s nrs ranging from min:%s to max:%s" % (contiguous_amount, min(spread), max(spread)))
            # u can exit here actually
    contiguous_amount += 1

print("solve:%s" % (solve_min + solve_max))