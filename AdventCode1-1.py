with open('AC1Input.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()

current_position = 50
pass_counter = 0

for i in range(len(content)):
    line = content[i].strip()
    direction = line[0]
    magnitude = int(line[1:].strip())
    current_position += magnitude if direction == 'R' else -magnitude
    if(current_position % 100 == 0):
        pass_counter += 1
        
print(pass_counter)