import unittest
from vattenKubikMeter import vattenKubikMeter

class TestWaterCubic(unittest.TestCase):
    """Testfall med olika siffror som representerar terrängens markhöjd."""
    
    def test_data(self):
        obj = vattenKubikMeter([0,0,0,-1,-1,-1,-2,-3])
        a = obj.beräkna_vatten()
        self.assertEqual(a, 8)

        obj = vattenKubikMeter([-1,2,-1,-2,1,4,-1,2])
        b = obj.beräkna_vatten()
        self.assertEqual(b, 12)
    
    def test_data2(self):
        obj = vattenKubikMeter([1,2])
        c = obj.beräkna_vatten()
        self.assertFalse(c, 1)

if __name__ == '__main__':
    unittest.main()