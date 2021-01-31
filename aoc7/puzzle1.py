import re

FILE_IN = "input.txt"


data = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
""".strip().splitlines()

with open(FILE_IN, 'r') as f: data = f.read().splitlines()


table = {}


for line in data:
    bag_color, bag_contents = line.split(" bags contain ")
    contents = [s.replace("bag", "") for s in re.findall("\d \w+ \w+ bag", bag_contents)]

    tmp = []
    for content in contents:
        if "shiny gold" in content:
            tmp.append(True)
        else:
            splitted = content.split(" ")
            amount = splitted[0].strip()
            color = " ".join(splitted[1:]).strip()
            tmp.append((int(amount), color))

    table[bag_color] = tmp

total = 0

def has_shiny_bag(color):
    try:
        contents = table[color]
    except KeyError:
        return False  #: shouldn't happen?

    if True in contents:
        return True  #: direct

    for content in contents:  #: indirect
        _, content_color = content
        if has_shiny_bag(content_color) is True:
            return True
    return False


for color, contents in table.items():
    if has_shiny_bag(color):
        total += 1

print(total)
