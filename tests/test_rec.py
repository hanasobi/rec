import unittest

from rec import RecValue


class TestRecValue(unittest.TestCase):
    def test_none_arg(self):
        with self.assertRaises(TypeError):
            RecValue(1, None)


    def test_dict_arg(self):
        with self.assertRaises(TypeError):
            RecValue(1, {})


if __name__ == "__main__":
    unittest.main()

