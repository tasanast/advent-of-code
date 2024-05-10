# advent of code day 03 part 1
import re

def generate_new_number():
    return {"number":'',
        "pos_x": -1,
        "pos_y":-1}
        
def is_symbol(character):
    match = re.search("[^0-9a-zA-Z.]", character)
    if match:
        return True
    else:
        return False

def get_number(row, coloumn, lines):
    # Find beginning of the number
    row_start = row
    row_end = row
    while(True):
        if lines[row_start][column].isnumeric():
            row_start = row-1
        else:
            break
    while(True):
        if lines[row_end][column].isnumeric():
            row_end = row+1
        else:
            break
    
# read input file
filename = "input.txt"
lines = None
with open(filename) as f:
    lines = f.read().splitlines() 

#  Find character with special character
#for j, line in enumerate(lines):
#    for k, character in enumerate(line):
#        if is_symbol(character):
#            print("found symbol", character, "at position", j, k)
#            # Check for numbers around special character.
#            for relative_row in range(-1,2):
#                for relative_colount in range(-1,2):
#                    other_character  = lines[j+relative_row][k+relative_colount]
#                    if other_character.isnumeric():
#                        print("found number", other_character)


# Find a number and capture it aling with its position
j=0
jmax = len(lines[0])
k=0
kmax = len(lines)
# Store number in this format
number=generate_new_number()
# Store numberes in this list
numbers=[]
        
while (k<kmax):
    line = lines[k]
    previous_char_was_number = False    # Flag to check if previous character was a number
    while (j<jmax):        
        character = line[j]
        if character.isnumeric() and not previous_char_was_number:
            number=generate_new_number()
            number["pos_x"] = j
            number["pos_y"] = k
        if character.isnumeric():
            number["number"]+=character
            previous_char_was_number = True
        else:
            if previous_char_was_number:
                numbers.append(number)
            previous_char_was_number = False
        if character.isnumeric() and j == jmax-1:
            numbers.append(number)

        j+=1
    j=0
    k+=1

# Check if each number is adjucent to a symbol
sum = 0
for number in numbers:
    # define the area to check for symbols
    area={}
    area["top_left_x"] = max(0, number["pos_x"]-1)
    area["top_left_y"] = max(0, number["pos_y"]-1)
    area["bottom_right_x"] = min(len(lines[0])-1, len(number["number"])+ number["pos_x"])
    area["bottom_right_y"] = min(len(lines)-1, number["pos_y"]+1)

    for x in range(area["top_left_x"], area["bottom_right_x"]+1):
        for y in range(area["top_left_y"], area["bottom_right_y"]+1):
            if is_symbol(lines[y][x]):
                # add to sum
                #print(number, "yes")
                number["is_part_number"] = True
                sum += int(number["number"])
print(sum)