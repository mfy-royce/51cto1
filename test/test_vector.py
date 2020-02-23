import unittest
from ml.mathunit import Vector

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector((0,1,1))
        self.v2 = Vector((1,0,0))
    def test_norm(self):
        m = 2 ** 0.5
        r = self.v1.norm()
        self.assertEqual(m,r,'Vector.norm test fail,{0}'.format(r))
    def test_dot(self):
        d1 = self.v1.dot(self.v2)
        d2 = self.v2.dot(self.v1)

        self.assertEqual(0, d1)
        self.assertEqual(0, d2)

    def test_cosin(self):
        c1 = self.v1.cosin(self.v2)
        c2 = self.v2.cosin(self.v1)
        self.assertEqual(0,c1,'Vector.cosin test fail,{0}'.format(c1))
        self.assertEqual(0,c2,'Vector.cosin test fail,{0}'.format(c2))
if __name__ == '__main__':
    unittest.main()
