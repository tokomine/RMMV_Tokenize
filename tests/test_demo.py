import unittest

class DemoTestCase(unittest.TestCase):
    def test_demo(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()
