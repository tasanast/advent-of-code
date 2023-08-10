# advent of code 2022 day02 part 1
def get_score(a, x):
    score_table = {'A X': 4, 'A Y': 8, 'A Z': 3, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6}
    return score_table[a + " " + x]
def main(filename):
    text_file = []
    with open(filename) as file:
        values = file.readline()
        while (values):
            text_file.append(values.strip().split(' '))
            values = file.readline()

    total = 0

    for line in text_file:
        total += get_score(line[0], line[1])

    return str(total)

if __name__ == '__main__':
    main()
