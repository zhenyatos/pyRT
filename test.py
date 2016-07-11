import unittest

from pyrt.math import *


class Vec3Test(unittest.TestCase):
    def testStandardConstructor(self):
        s = Vec3(1, 2, 3)
        self.assertEqual(s.x, 1.0)
        self.assertEqual(s.y, 2.0)
        self.assertEqual(s.z, 3.0)

    def testTupleConstructor(self):
        s = Vec3((1,2,3))
        self.assertEqual(s.x, 1.0)
        self.assertEqual(s.y, 2.0)
        self.assertEqual(s.z, 3.0)

    def testListConstructor(self):
        s = Vec3([1, 2, 3])
        self.assertEqual(s.x, 1.0)
        self.assertEqual(s.y, 2.0)
        self.assertEqual(s.z, 3.0)

    def testNamedConstructor(self):
        s = Vec3(x=1)
        self.assertEqual(s.x, 1.0)
        self.assertEqual(s.y, 0.0)
        self.assertEqual(s.z, 0.0)

        s = Vec3(y=1)
        self.assertEqual(s.x, 0.0)
        self.assertEqual(s.y, 1.0)
        self.assertEqual(s.z, 0.0)

        s = Vec3(z=1)
        self.assertEqual(s.x, 0.0)
        self.assertEqual(s.y, 0.0)
        self.assertEqual(s.z, 1.0)

        s = Vec3(x=1, y=2, z=3)
        self.assertEqual(s.x, 1.0)
        self.assertEqual(s.y, 2.0)
        self.assertEqual(s.z, 3.0)

    def testAccess(self):
        a = Vec3(5,6,7)
        self.assertEqual(a.x, 5.0)
        self.assertEqual(a.y, 6.0)
        self.assertEqual(a.z, 7.0)

        self.assertEqual(a[0], 5.0)
        self.assertEqual(a[1], 6.0)
        self.assertEqual(a[2], 7.0)

        a[0] = 10
        a[1] = 11
        a[2] = 12
        self.assertEqual(a[0], 10.0)
        self.assertEqual(a[1], 11.0)
        self.assertEqual(a[2], 12.0)


    def testWrongConstructor(self):
        self.assertRaises(ValueError, Vec3, 1,2,3,x=5)


    def testEqual(self):
        a = Vec3(4.5, 5.5, 6.5)
        b = Vec3(4.5, 5.5, 6.5)
        c = Vec3(5,4,3)

        self.assertEqual(a,b)
        self.assertEqual(a, (4.5, 5.5, 6.5))
        self.assertEqual(a, [4.5, 5.5, 6.5])
        self.assertNotEqual(a,c)

    def testMultiplication(self):
        a = Vec3(1,2,3)
        b = Vec3(2,3,4)
        c = a * b
        d = 3 * b
        e = b * 3
        x = Vec3(2,2,2)
        self.assertEqual(c, (2,6,12))
        self.assertEqual(d, (6,9,12))
        self.assertEqual(a*b*x, (4,12,24))
        self.assertEqual(d,e)

    def testFunctions(self):
        v1 = Vec3(1, 2, 3)
        v2 = Vec3(3, 4, 5)
        v3 = cross(v1,v2)

        self.assertEqual(v3, (-2.0, 4.0, -2.0))

        s = normalize(v1)

        self.assertEqual(s, (0.2672612419124244, 0.5345224838248488, 0.8017837257372732))

"""
from pyrt.math import *
from pyrt.geometry import Triangle
from pyrt.camera import PerspectiveCamera
#from pyrt.renderer import SimpleRT

print("Hello World!")

v = Vec3(1.0, 2.0, 3.0)

cam = PerspectiveCamera()
"""



if __name__ == '__main__':
    unittest.main()