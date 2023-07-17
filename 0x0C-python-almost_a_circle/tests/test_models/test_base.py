#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_specified_1(self):
         test0 = Base()
         self.assertAlmostEquals(test0.id, 1)

    def test_id_specified(self):
        test1 = Base()
        test2 = Base()
        self.assertAlmostEquals(test1.id, 2)
        self.assertAlmostEquals(test2.id, 3)

    def test_id_not_specified(self):
        test3 = Base(12)
        test4 = Base()
        self.assertAlmostEquals(test3.id, 12)
        self.assertAlmostEquals(test4.id, 4)

if __name__=='__main__':
	unittest.main()
