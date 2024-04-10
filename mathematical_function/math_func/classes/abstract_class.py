from abc import ABC, abstractmethod

class ThreeDimensionalShape(ABC):

    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def surface_area(self):
        pass
