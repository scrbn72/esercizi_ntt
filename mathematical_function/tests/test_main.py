import unittest
from mathematical_function.math_func.classes.sphere import Sphere


class TestSphere(unittest.TestCase):

    def test_volume(self):

        sphere = Sphere(1)

        self.assertAlmostEqual(sphere.volume(), 4.19, places=2)

    def test_surface_area(self):

        sphere = Sphere(1)

        self.assertAlmostEqual(sphere.surface_area(), 12.57, places=2)

if __name__ == '__main__':
    unittest.main()
