# adventofcode.com 2022 day05 part 1
filename = 'input_test.txt'
data1 = []
data2 = []
flag = True
data1 = []
with open(filename) as f:
    line = f.readline() 

    while line:
        if line.strip() == "":
            flag = False
            line = f.readline()
            continue
        
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


#print(data)