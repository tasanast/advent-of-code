import unittest
import main_a
import main_b

answer_a_filename = "answer_a.txt"
answer_a = ""
with open(answer_a_filename) as file:
    answer_a = file.read().strip()

answer_b_filename = "answer_b.txt"
answer_b = ""
with open(answer_b_filename) as file:
    answer_b = file.read().strip()

input_filename = "input.txt"


class MyTests(unittest.TestCase):
    def test_main_a(self):
        self.assertEqual(main_a.main(input_filename), answer_a)

    def test_get_score(self):
        self.assertEqual(main_a.get_score("A", "X"), 4)


    def test_get_score2(self):
        self.assertEqual(main_a.get_score("C", "Y"), 2)

    def test_main_b(self):
        self.assertEqual(main_b.main(input_filename), answer_b)

if __name__ == '__main__':
    unittest.main()

