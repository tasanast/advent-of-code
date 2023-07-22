# adventofcode.com 2022 day01 part 1

#file_name = "input_test.txt"
file_name = "input.txt"

text = ""

with open(file_name) as file:
    text = file.read()

lines = text.splitlines()
max = 0
total = 0
last_line = len(lines)
for index, line in enumerate(lines):
    if not line == "":
        total += int(line)
    if line == "" or index == last_line-1:
        if total > max:
            max = total
        total = 0

print(max)