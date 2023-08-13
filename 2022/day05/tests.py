import unittest
import main_a, main_b
from pathlib import Path


input_test_filename = 'input_test.txt'
answer_a_test = Path('answer_a_test.txt').read_text().strip()

input_filename = 'input.txt'
answer_a = Path('answer_a.txt').read_text().strip()
answer_b = Path('answer_b.txt').read_text().strip()

answer_b_test = Path('answer_b_test.txt').read_text().strip()

class main_a_tests(unittest.TestCase):
    def test_main_a_with_answer_test(self):
        self.assertEqual(main_a.main(input_test_filename), answer_a_test)

    def test_main_a_with_answer(self):
        self.assertEqual(main_a.main(input_filename), answer_a)

class main_b_tests(unittest.TestCase):
    def test_main_b_with_answer_test(self):
        self.assertEqual(main_b.main(input_test_filename), answer_b_test)

    def test_main_b_with_answer(self):
        self.assertEqual(main_b.main(input_filename), answer_b)
if __name__ == '__main__':
    unittest.main()

