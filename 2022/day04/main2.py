# adventofcode.com 2022 day04

filename = "input.txt"
#filename = "input_test.txt"

data = []
with open(filename) as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.rstrip('\n')
        line = line.split(',')
        a1, a2 = line[0].split('-')
        b1, b2 = line[1].split('-')
        a1 = int(a1)
        a2 = int(a2)
        b1 = int(b1)
        b2 = int(b2)
        data.append([[a1, a2], [b1,b2]])

count = 0
for line in data:
    if ((line[0][0] >= line[1][0]) and (line[0][0] <= line[1][1])) \
        or ((line[0][1] >= line[1][0]) and (line[0][1] <= line[1][1])) \
        or((line[1][0] >= line[0][0]) and (line[1][0] <= line[0][1])) \
        or ((line[1][1] >= line[0][0]) and (line[1][1] <= line[0][1])):
            count +=1
            print(line)

print(count)
