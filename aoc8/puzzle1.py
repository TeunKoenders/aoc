FILE_IN = "input.txt"


data = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip().splitlines()

with open(FILE_IN, 'r') as f: data = f.read().splitlines()

no_dupe = True
index = 0
accumulator = 0
indexes_used = set()

while no_dupe:

    def nop(nr):
        global index
        index += 1

    def acc(nr):
        global index
        global accumulator
        accumulator += nr
        index += 1

    def jmp(nr):
        global index
        index += nr

    actions = {
        "nop": nop,
        "acc": acc,
        "jmp": jmp
    }

    action, change = data[index].split(" ")
    print("%s:%s" % (action, change))

    actions[action](int(change))

    if index not in indexes_used:
        indexes_used.add(index)
    else:
        no_dupe = False

print("acc:%s" % accumulator)