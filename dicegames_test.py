import unittest
from dicegames import *

class TestDicegames(unittest.TestCase):

    def test_roll(self):
        self.assertIs(type(roll()),list)
        self.assertIs(len(roll(4)),4)
        self.assertEqual(roll(6,seed=10),roll(6,seed=10))

    def test_dec_to_pct(self):
        self.assertIs(type(dec_to_pct(0.158324)),str)
        self.assertIs(len(dec_to_pct(0.158324)),6)
        self.assertIs(len(dec_to_pct(0.158324,4)),8)
        self.assertRaises(TypeError, dec_to_pct, "0.2342")
        
    def test_farkel_prob(self):
        self.assertIs(type(farkel_prob()),dict)
        self.assertIs(len(farkel_prob()),12)
        self.assertRaises(ValueError, farkel_prob, 8)
    
    def test_farkel_score(self):
        self.assertIs(type(farkel_score(roll(6))),dict)
        self.assertEqual(farkel_score([1,2,3,4,5,6])["score"],1500)
        self.assertEqual(farkel_score([1,2,3,1,2,3])["score"],1500)
        self.assertEqual(farkel_score([2,2,2,4,4,4])["score"],2500)
        self.assertEqual(farkel_score([6,6,6,6,6,6])["score"],3000)
        self.assertEqual(farkel_score([3,3,3,3,3,4])["score"],2000)
        self.assertEqual(farkel_score([3,3,3,3,3,5])["score"],2050)
        self.assertEqual(farkel_score([3,3,3,3,6,6])["score"],1000)
        self.assertEqual(farkel_score([3,3,3,3,1,6])["score"],1100)
        self.assertEqual(farkel_score([3,3,3,3,1,5])["score"],1150)
        self.assertEqual(farkel_score([3,3,3,2,2,4])["score"],300)
        self.assertEqual(farkel_score([4,4,4,1,2])["score"],500)
        self.assertEqual(farkel_score([4,4,4,1,5])["score"],550)
        self.assertEqual(farkel_score([4,4,4,2])["score"],400)
        self.assertEqual(farkel_score([4,2,1,5])["score"],150)
        self.assertEqual(farkel_score([3,2,3])["score"],0)
        self.assertEqual(farkel_score([1,2,3,4,5,6])["dice remaining"],6)
        self.assertEqual(farkel_score([1,2,3,1,2,3])["dice remaining"],6)
        self.assertEqual(farkel_score([2,2,2,4,4,4])["dice remaining"],6)
        self.assertEqual(farkel_score([6,6,6,6,6,6])["dice remaining"],6)
        self.assertEqual(farkel_score([3,3,3,3,3,4])["dice remaining"],1)
        self.assertEqual(farkel_score([3,3,3,3,3,5])["dice remaining"],6)
        self.assertEqual(farkel_score([3,3,3,3,6,6])["dice remaining"],2)
        self.assertEqual(farkel_score([3,3,3,3,1,6])["dice remaining"],1)
        self.assertEqual(farkel_score([3,3,3,3,1,5])["dice remaining"],6)
        self.assertEqual(farkel_score([3,3,3,2,2,4])["dice remaining"],3)
        self.assertEqual(farkel_score([4,4,4,1,2])["dice remaining"],1)
        self.assertEqual(farkel_score([4,4,4,1,5])["dice remaining"],6)
        self.assertEqual(farkel_score([4,4,4,2])["dice remaining"],1)
        self.assertEqual(farkel_score([4,2,1,5])["dice remaining"],2)
        self.assertEqual(farkel_score([3,2,3])["dice remaining"],0)
        
    def test_farkel_turn(self):
        self.assertIs(type(farkel_turn()),int)

if __name__ == '__main__':
    unittest.main()