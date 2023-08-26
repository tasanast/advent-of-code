import unittest
from pathlib import Path
import main_a

input_test_filename = "input_test.txt"
answer_a_test_filename = "answer_a_test.txt"
answer_a_test = Path(answer_a_test_filename).read_text()

class MyTests(unittest.TestCase):
    def test_main_a_test(self):
        self.assertEqual(main_a.main(input_test_filename),answer_a_test)

if __name__ == "__main__":
    unittest.main()
