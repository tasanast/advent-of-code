# advent of code 2024 day04 part 1

file_name = 'input.txt'
#file_name = 'input_test.txt'
keyword = 'XMAS'

data = []
with open(file_name) as f:
    data = [line.strip() for line in f]

# find first letter of key word
count = 0
for row in range(0, len(data)):
    for column in range(0, len(data[0])):

        if data[row][column] == keyword[0]:
            # We will use the directions of a compass to name the directions to check
            # Get East
            if column <= len(data[0])- len(keyword) + 1: # confirm that there are enough letters to complete the keyword
                #word = data[row][column:(column+len(keyword)-1)]
                word = data[row][column:column+len(keyword)]
                if word == keyword:
                    count += 1
                    print(row, column, 'East')

            # Get South-East
            if ((column+len(keyword)-1 < len(data[0])) and
                (row+len(keyword)-1 < len(data))):
                word = ''
                for letter_x in range(0, len(keyword)):
                    word += data[row+letter_x][column+letter_x]
                if word == keyword:
                    count += 1
                    print(row, column, 'South-East')

            # Get South
            if (row+len(keyword)-1 < len(data)):
                word = ''
                for letter_x in range(0, len(keyword)):
                    word += data[row+letter_x][column]
                if word == keyword:
                    count += 1
                    print(row, column, 'South')

            # Get South-West 
            if ((column >= len(keyword)-1) and
                (row+len(keyword)-1 < len(data))):
                word = ''
                for letter_x in range(0, len(keyword)):
                    word += data[row+letter_x][column-letter_x]
                if word == keyword:
                    count += 1
                    print(row, column, 'South-West')

            # Get West 
            if (column >= len(keyword)-1):      
                word = ''
                for letter_x in range(0, len(keyword)):
                    word += data[row][column-letter_x]
                if word == keyword:
                    count += 1
                    print(row, column, 'West')

            # Get North-West
            if ((column >= len(keyword)-1) and
                (row >= len(keyword)-1)):
                word = ''
                for letter_x in range(0, len(keyword)):
                    word += data[row-letter_x][column-letter_x]
                if word == keyword:
                    count += 1
                    print(row, column, 'North-West')

            # Get North
            if (row >= len(keyword)-1):
                word = ''
                for letter_x in range(0, len(keyword)):
                    word += data[row-letter_x][column]
                if word == keyword:
                    count += 1
                    print(row,column,'North')

            # Get North-East
            if ((row >= len(keyword)-1)
                and (column+len(keyword)-1 < len(data[0]))):
                word = ''
                for letter_x in range(0, len(keyword)):
                    word += data[row-letter_x][column+letter_x]
                if word == keyword:
                    count += 1
                    print(row,column,'North')

print(count)
            # check if word 
            #negative_match = False 
            #if row+1 >= len(keyword):   # Check if there are enough letters above:
            #    letter_x = 0
            #    for letter_y in range(1, len(keyword)):
            #        if data[row-letter_x][column-letter_y] != keyword[letter_y]:
            #            print(data[row-letter_x][column-letter_y]), '!=' keyword[]
            #            negative_match = True
            #            break
            #    if not negative_match:
            #        print('found at', row,column)
            #        count += 1


