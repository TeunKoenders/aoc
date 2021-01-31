
FILE_IN = "input.txt"

total = 0

with open(FILE_IN, 'r') as f:
    data = f.read().split("\n\n")
    
    for group in data:
        total += len(set(group.replace('\n', ''))) 

print(total)