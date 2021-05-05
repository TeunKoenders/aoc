FILE_IN = "input.txt"

with open(FILE_IN, 'r') as file: data = file.read().splitlines()

# data = ["0", "1789,37,47,1889"]

busses = [(i, int(id_)) for i, id_ in enumerate(data[1].split(",")) if id_ != "x"]
processed_busses = []

def test_previously_checked_busses_still_ok():
    for x, y in processed_busses:
        #: should be all zero
        assert ((timestamp + x) % y) == 0

timestamp = 0
step = 1

for offset, bus_id in busses:
    while (timestamp + offset) % bus_id != 0:  #: main check, definitely need this.
        timestamp += step  #: skip step amount, because we want to keep our previous discoveries as well
    step *= bus_id  #: lock previous discoveries

    processed_busses.append((offset, bus_id))
    test_previously_checked_busses_still_ok()

print(timestamp)
test_previously_checked_busses_still_ok()