# adventofcode.com 2022 day 03
filename = "input.txt"
#filename = "input_test.txt"

data = []
with open(filename) as f:
    data = f.read().splitlines()
score_sum = 0
count = 0
for i in range(0, len(data)-1,3):
    for character in set(data[i]):
        if character in data[i+1] and character in data[i+2]:
            if ord(character)>= 97:
                score = ord(character) - 96
            else:
                score = ord(character) - 64 + 26
            score_sum += score
print(score_sum)
