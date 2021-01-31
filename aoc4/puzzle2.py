import re

FILE_IN = "input.txt"

class Passport:

    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None, hcl=None, ecl=None, pid=None, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    @property
    def is_valid(self):
        def cmp_yr_wrapper(l, min, max):
            def wrapper(val):
                if val is None:
                    return False
                if len(val) != l:
                    return False
                integer = int(val)
                return integer >= min and integer <= max
            return wrapper

        def cmp_height(val):
            if val is None:
                return False
            actual = val[:-2]
            if "cm" in val:
                if actual.isdigit() and int(actual) >= 150 and int(actual) <=193:
                    return True
            if "in" in val:
                if actual.isdigit() and int(actual) >= 59 and int(actual) <= 76:
                    return True
            return False

        def cmp_hair_color(val):
            if val is None or val[0] != "#" or len(val) != 7: return False
            if not re.match('^[0-9a-f]+$', val[1:]):
                return False
            return True

        def cmp_eye_color(val):
            if val is None:
                return False
            return val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        def cmp_pid(val):
            if val is None:
                return False
            return len(val) == 9 and val.isdigit()

        for key, cmp_f in [
            (self.byr, cmp_yr_wrapper(4, 1920, 2002)),
            (self.iyr, cmp_yr_wrapper(4, 2010, 2020)),
            (self.eyr, cmp_yr_wrapper(4, 2020, 2030)),
            (self.hgt, cmp_height),
            (self.hcl, cmp_hair_color),
            (self.ecl, cmp_eye_color),
            (self.pid, cmp_pid)
        ]:
            if cmp_f(key) is not True:
                return False
        return True


valid = 0
data = []
with open(FILE_IN, 'r') as f:
    for passport in f.read().split('\n\n'):
        passport = passport.replace("\n", " ")
        kw = {p[:p.find(":")]:p[p.find(":") + 1:] for p in passport.split(" ")}
        pp = Passport(**kw)
        data.append(pp)
        valid += 1 if pp.is_valid else 0
        print("%s:%s" % (passport, pp.is_valid))

print("total:%s" % valid)