
FILE_IN = "input.txt"

total = 0

with open(FILE_IN, 'r') as f:
    data = f.read().split("\n\n")
    
    for group in data:
        
        unique_answers_group = set(group)
        unique_answers = [set(answer_one_person) for answer_one_person in group.split('\n')]
        total += len(unique_answers_group.intersection(*unique_answers))

print(total)
