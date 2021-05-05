FILE_IN = "input.txt"

with open(FILE_IN, 'r') as file: data = file.read().splitlines()

now_time =int(data[0])
bus_ids = [int(id_) for id_ in data[1].split(',') if id_ != "x"]
bus_next_departures = [int(now_time / id_ + 1) * id_ for id_ in bus_ids]
next_in_time = min(bus_next_departures)
time_to_wait = next_in_time - now_time
bus_solution = bus_ids[bus_next_departures.index(next_in_time)]
print(bus_solution)
print(time_to_wait)
print(bus_solution * time_to_wait)