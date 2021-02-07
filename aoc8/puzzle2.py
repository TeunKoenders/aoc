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

class PuzzleBoi:

    def __init__(self, script):
        self.index = 0
        self.accumulator = 0
        self.indexes_used = set()
        self.changed_line = None
        self.script = script

    def execute(self):

        while self.index < len(self.script):
            def nop(nr):
                self.index += 1

            def acc(nr):
                self.accumulator += nr
                self.index += 1

            def jmp(nr):
                self.index += nr

            actions = {
                "nop": nop,
                "acc": acc,
                "jmp": jmp
            }

            action, change = self.script[self.index].split(" ")

            actions[action](int(change))

            if self.index not in self.indexes_used:
                self.indexes_used.add(self.index)
            else:
                return False
        return True


for i in range(len(data)):
    if data[i].startswith("nop") or data[i].startswith("jmp"):
        op, nr = data[i].split(" ")
        #: modify the program with replacing everytime one jmp/nop with another
        op = "nop" if op == "jmp" else "nop"
        pb = PuzzleBoi(data[:i] + ["%s %s" % (op, nr)] + data[i+1:])
        if pb.execute():
            print("solved: %s" % pb.accumulator)
            exit(0)