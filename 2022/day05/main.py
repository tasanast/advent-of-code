# adventofcode.com 2022 day05 part 1
#
# This code is split into two parts:
# * 1st part has the stacks of boxes
# * 2nd part has the steps for restacking the boxes
#filename = 'input_test.txt'
filename = 'input.txt'
data1 = []
steps = []
flag = True
data1 = []
with open(filename) as f:
    line = f.readline() 


    while line:
        # Check if 1st part has finished
        if line.strip() == "":
            flag = False
            line = f.readline()
            continue
        
        # 1st part of input file 
        if flag:
            if line[1] == "1":
                line = f.readline()
                continue
            row = []
            for i in range(1,len(line), 4):
                #DEBUG#print(line[i], end='|')
                row.append(line[i])
            #DEBUG#print("")
            data1.append(row)

        # second part of input file. Moving boxes around 
        if not flag:
            temp_split = line.split()
            step = {'move': int(temp_split[1]), 'from': int(temp_split[3]), 'to': int(temp_split[5])}
            steps.append(step)


        line = f.readline()



stacks = []
for i in range(0, len(data1[0])):
    column = []
    for j in range(len(data1)-1, -1, -1):
        if data1[j][i] != ' ':
            column.append(data1[j][i])
    stacks.append(column)

#DEBUG#print(stacks)



#print(data1)
#DEBUG#print(steps)

# Move boxes around and find final positions
for i, step in enumerate(steps):
    #DEBUG#print('step: ', i)
    # number of boxes to move from a stack
    for i in range(0, step['move']):
        # get the top box of a stack and move it to the top of another stack
        box = stacks[step['from']-1].pop()
        #DEBUG#print(box)
        stacks[step['to']-1].append(box)

#DEBUG#print(stacks)

# print top boxes
for stack in stacks:
    print(stack[-1], end="")
print('')



#print(data)