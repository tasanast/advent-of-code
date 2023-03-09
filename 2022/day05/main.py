# adventofcode.com 2022 day05 part 1
#
# This code is split into two parts:
# * 1st part has the stacks of boxes
# * 2nd part has the steps for restacking the boxes
filename = 'input_test.txt'
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
                print(line[i], end='|')
                row.append(line[i])
            print("")
            data1.append(row)

        # second part of input file. Moving boxes around 
        if not flag:
            step = {'move': line[5], 'from': line[12], 'to': line[17]}
            steps.append(step)


        line = f.readline()
data_temp = []
for i in range(0, len(data1[0])):
    column = []
    for j in range(len(data1)-1, -1, -1):
        if data1[j][i] != ' ':
            column.append(data1[j][i])
    data_temp.append(column)

print(data_temp)



print(data1)
print(steps)


#print(data)