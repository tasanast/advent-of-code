# advent of code day 03 part 1
import re

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
filename = "input_test.txt"
lines = None
with open(filename) as f:
    lines = f.read().splitlines() 

#  Find character with special character
for j, line in enumerate(lines):
    for k, character in enumerate(line):
        if is_symbol(character):
            print("found symbol", character, "at position", j, k)
            # Check for numbers around special character.
            for relative_row in range(-1,2):
                for relative_colount in range(-1,2):
                    other_character  = lines[j+relative_row][k+relative_colount]
                    if other_character.isnumeric():
                        print("found number", other_character)
