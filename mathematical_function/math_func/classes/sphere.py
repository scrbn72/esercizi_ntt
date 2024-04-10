from math import pi
from mathematical_function.math_func.classes.abstract_class import ThreeDimensionalShape


class Sphere(ThreeDimensionalShape):

    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return round((4/3) * pi * self.radius ** 3, 2)

    def surface_area(self):
        return round(4 * pi * self.radius ** 2, 2)
