import re

FILE_IN = "input.txt"


data = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
""".strip().splitlines()

with open(FILE_IN, 'r') as f: data = f.read().splitlines()


table = {}


for line in data:
    bag_color, bag_contents = line.split(" bags contain ")
    contents = [s.replace("bag", "") for s in re.findall("\d \w+ \w+ bag", bag_contents)]

    tmp = []
    for content in contents:
        splitted = content.split(" ")
        amount = splitted[0].strip()
        color = " ".join(splitted[1:]).strip()
        tmp.append((int(amount), color))

    table[bag_color] = tmp


def count_bags_in_bag(color):
    try:
        contents = table[color]
    except KeyError:
        return 0  #: shouldn't happen?

    tmp = 0
    for content in contents:  #: indirect
        count, content_color = content
        tmp += count
        tmp += count * count_bags_in_bag(content_color)
    return tmp

total = count_bags_in_bag("shiny gold")
print(total)
