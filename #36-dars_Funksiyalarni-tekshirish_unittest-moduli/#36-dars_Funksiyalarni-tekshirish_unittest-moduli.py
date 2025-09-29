import unittest
from name import get_full_name
from circle import getArea,getPerimeter
from tubsonmi import tubSonmi


class NameTest(unittest.TestCase):
    def test_full_name(self):    
        name=get_full_name("ulugbek", "yuldoshev")
        self.assertEqual(name, "Ulugbek Yuldoshev")
    
    def test_toliq_ism(self):
        name = get_full_name('hasan','husanov','olimovich')
        self.assertEqual(name, "Hasan Olimovich Husanov")

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(10), 314.159) #bunda sonlar verguldan keyin 7xonagacha bir xilligini tekshiradi
        self.assertAlmostEqual(getArea(3),28.27431,3) # bunda esa verguldan keyin 3 xonagacha tekshiradi

    def test_perimetr(self):
        self.assertAlmostEqual(getPerimeter(10), 62.8318)
        self.assertAlmostEqual(getPerimeter(4), 25.13272)
        
class tubSonTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(tubSonmi(7))
        self.assertTrue(tubSonmi(193))
        self.assertTrue(tubSonmi(547))
    def test_false(self):
        self.assertFalse(tubSonmi(6))
        self.assertFalse(tubSonmi(265))
        self.assertFalse(tubSonmi(489))    


unittest.main()
