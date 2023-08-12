import unittest
import main_a
from pathlib import Path


input_test_filename = 'input_test.txt'
answer_a_test = Path('answer_a_test.txt').read_text().strip()

input_filename = 'input.txt'
answer_a = Path('answer_a.txt').read_text().strip()

class main_a_tests(unittest.TestCase):
    def test_main_a_with_answer_test(self):
        self.assertEqual(main_a.main(input_test_filename), answer_a_test)

    def test_main_a_with_answer(self):
        self.assertEqual(main_a.main(input_filename), answer_a)

if __name__ == '__main__':
    unittest.main()
