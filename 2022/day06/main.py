# Advent of code 2022 day 06

# Read file
filename = 'input.txt'
#filename = 'input_test2.txt'
input_file = ""
with open(filename) as f:
    input_file = f.read()

#  Main
distinct_char_num = 14
for i in range (0, len(input_file)-distinct_char_num-1):
    flag = False
    for j in range(i,i+distinct_char_num-1):
        for k in range(j+1,i+distinct_char_num):
            if input_file[j] == input_file[k]:
                flag = True
                break

    if flag == False:
        print("Message found after character:",i+distinct_char_num)
        break
