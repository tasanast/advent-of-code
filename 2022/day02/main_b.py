# advent of code 2022 day02 part 2
def get_score(a, x):
    score_table = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}
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
