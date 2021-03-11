import fibonnaci
import unittest

class TestClass(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fibonnaci.fibonnaci(10), 55)

if __name__ == "__main__":
    unittest.main()

def test_fibonnaci():
    assert 55 == fibonnaci.fibonnaci(10), "test failed"
