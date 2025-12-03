with open('AC1Input.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()

START_POSITION = 50
DEBUG = False

current_position = START_POSITION
pass_counter = 0


for i in range(len(content)):
    line = content[i].strip()
    direction = line[0]
    magnitude = int(line[1:].strip())
    #now lets iterate through the dial based on magnitude & direction
    #once we reach 99 the next step we reset to 0 and increase the pass counter
    #once we reach 0 the next step we reset to 99 and increase the pass counter
    for x in range(magnitude):
        if DEBUG:
            print('Run ' + str(x) + ' Start Pass Counter: ' + str(pass_counter))
            print('Run ' + str(x) + ' Magnitude: ' + str(magnitude))
            print('Run ' + str(x) + ' Start Position: ' + str(current_position))
       #Any time we hit 0 the pass_counter needs to move up by 1
       #But that is separate from keeping us on the 'dial'

       #So first we stay on the "dial"
        if direction == 'R':
            if current_position == 99:
                x += 1  # to offset the upcoming increment
                current_position = 0
            else: #We can always add 1 if its not 99
                current_position += 1
            
        else: # direction == 'L'
            if current_position == 0:
                x += 1  # to offset the upcoming decrement
                current_position = 99
            else: #we can always subtract 1 if its not 0
                current_position -= 1

        #Then we check if we need to increase the pass counter
        if current_position == 0:
            pass_counter += 1
        
        #So we are always on the dial and any time we pass 0 we click
        #Note we are always going to complete a full direction of motion before
        #we iniiate another motion

        if DEBUG:
            print('Run ' + str(x) + ' End Pass Counter: ' + str(pass_counter))
            print('Run ' + str(x) + ' End Position: ' + str(current_position))


print(pass_counter)
            