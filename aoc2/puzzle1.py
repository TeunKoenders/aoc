from collections import namedtuple
FILE_IN = "input.txt"
PasswordInfo = namedtuple("Info", ["lower_bound", "upper_bound", "letter", "password", "raw"])


data = []
with open(FILE_IN, 'r') as f:
    for line in f.read().splitlines():
        bounds, letter, password = line.split(' ')  # split from ' ' so we get [bounds, letter, password]
        lower, upper = bounds.split('-')  # split [0] with on '-' sow we get [lower, upper]
        letter = letter[0]
        data.append(PasswordInfo(int(lower), int(upper), letter, password, line))  
        # probably should be a class next time we encounter such a puzzle

good = 0
for x in data:
    amount = x.password.count(x.letter)
    if x.upper_bound >= amount >= x.lower_bound:  # just do a compare, but probably should be in class next time :)
        good += 1
        print("valid: %s" % x.raw)

print("valid passwords: %s" % good)