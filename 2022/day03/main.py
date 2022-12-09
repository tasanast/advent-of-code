# adventofcode.com 2022 day 03
filename = "input.txt"
#filename = "input_test.txt"

data = []
with open(filename) as f:
    data = f.read().splitlines()
score_sum = 0
count = 0
line_num = 0
for line in data:
    found = False
    line_num +=1
    half_len = int(len(line)/2)
    compartment1 = set(line[0:half_len])
    compartment2 = set(line[half_len:])
    for character in compartment1:
        if character in compartment2:
            found = True
            count +=1
            if ord(character)>= 97:
                score = ord(character) - 96
            else:
                score = ord(character) - 64 + 26
            score_sum += score
            print(character, score)
    if found == False:
        print("line skipped: ", line_num)
    #line = [compartment1, compartment2]
print(score_sum)
print(count)
