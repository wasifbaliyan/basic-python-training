# OOP/Classes
# Class: is a blueprint for creating new objects
# Objects: are intance of a class
# every function inside the class must have atleast one parameter which is self


class Point:
    # constructor function/magic function
    default_color = "green"

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x} {self.y})")

# Class attributes vs instance attributes
        # will be shared across all the instances
# Class vs instance methods
        # factory method (class method) use decorator @classmethod, pass first argument cls


point = Point(2, 3)
point.draw()
another = Point.zero()
another.draw()
