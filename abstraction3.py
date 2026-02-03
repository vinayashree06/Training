from abc import ABC, abstractmethod
class Shape(ABC):
    
    def __init__(self,c):
        self.color=c
    def get_color(self):
        return self.color
    @abstractmethod
    def get_area(self):
        pass
    def get_perimeter(self):
        pass
class Square(Shape):
    def __init__(self,c,side):
        super().__init__(c)
        self.side=side
    def get_area(self):
        return self.side*self.side
    def get_perimeter(self):
        return self.side*4
sq=Square("red",5.0)
print(sq.get_color(),sq.get_area(),sq.get_perimeter())
        