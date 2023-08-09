# adventofcode.com 2022 day01 part 1

def update_top_values(new_value, top_list):
    for index, value in enumerate(top_list):
        if new_value > value:
            top_list.insert(index,new_value)
            top_list.pop()
            break
    return top_list

#file_name = "input_test.txt"
file_name = "input.txt"

text = ""

with open(file_name) as file:
    text = file.read()

lines = text.splitlines()
max_list = [0, 0, 0]
total = 0
last_line = len(lines)

for index, line in enumerate(lines):
    if not line == "":
        total += int(line)
    if line == "" or index == last_line-1:
        update_top_values(total,max_list)
        total = 0

print(max_list[0]+max_list[1]+max_list[2])
