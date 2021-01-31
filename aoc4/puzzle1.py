FILE_IN = "input.txt"

class Passport:

    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None, hcl=None, ecl=None, pid=None, cid=None):
        self.byr = byr
        self.iry = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    @property
    def is_valid(self):
        return (self.byr and self.iry and self.eyr and self.hgt and self.hcl and self.ecl and self.pid) != None


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