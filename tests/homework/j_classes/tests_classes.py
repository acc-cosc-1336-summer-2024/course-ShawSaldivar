import unittest

from src.homework.j_classes.class_a import die

class Test_Config(unittest.TestCase):

    

    def test_rolls(self):
        d = die()
        d.roll()
        self.assertTrue(1 <= d.get_roll_value() <= 6 )

        d.roll()
        self.assertTrue(1 <= d.get_roll_value() <= 6 )

        d.roll()
        self.assertTrue(1 <= d.get_roll_value() <= 6 )



