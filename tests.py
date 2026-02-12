import unittest
from waterCubic import waterCubic

class TestWaterCubic(unittest.TestCase):
    
    def test_data(self):
        obj = waterCubic([0,0,0,-1,-1,-1,-2,-3])
        a = obj.measure_water()
        self.assertEqual(a, 8)

if __name__ == '__main__':
    unittest.main()