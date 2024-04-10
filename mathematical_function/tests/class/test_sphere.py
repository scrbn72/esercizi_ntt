import unittest
from math import pi
from mathematical_function.math_func.classes.sphere import Sphere

class TestSphere(unittest.TestCase):

    def test_volume(self):

        radius = 1
        expected_volume = round((4/3) * pi * radius ** 3, 2)
        sphere = Sphere(radius)
        self.assertAlmostEqual(sphere.volume(), expected_volume, places=2)

    def test_surface_area(self):

        radius = 1
        expected_surface_area = round(4 * pi * radius ** 2, 2)
        sphere = Sphere(radius)
        self.assertAlmostEqual(sphere.surface_area(), expected_surface_area, places=2)

if __name__ == '__main__':
    unittest.main()
