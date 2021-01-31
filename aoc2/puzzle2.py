from collections import namedtuple
FILE_IN = "input.txt"
PasswordInfo = namedtuple("Info", ["lower_bound", "upper_bound", "letter", "password", "raw"])


data = []
with open(FILE_IN, 'r') as f:
    for line in f.read().splitlines():
        bounds, letter, password = line.split(' ')
        lower, upper = bounds.split('-')
        letter = letter[0]
        data.append(PasswordInfo(int(lower), int(upper), letter, password, line))
        # should be class next time

good = 0
for x in data:
    max_len = len(x.password)
    lower_is_true = (max_len >= x.lower_bound) and (x.password[x.lower_bound - 1] == x.letter)
    upper_is_true = (max_len >= x.upper_bound) and (x.password[x.upper_bound - 1] == x.letter)

    if lower_is_true ^ upper_is_true:  # xor because only one can be true
        good += 1
        print("valid: %s (%r, %r)" % (x.raw, lower_is_true, upper_is_true))

print("valid passwords: %s" % good)
