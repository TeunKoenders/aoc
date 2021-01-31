import sys

total = 1
for a in sys.argv:
    if a.isdigit():
        total *= int(a)
print("total: %s" % total)