
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

square = Square(3, 3)
cube = Cube(3, 3, 3)

# print(square.area())
# print(cube.volume())

from time import time

limit = int(10e7)
lst = [_ for _ in range(1, limit)]


start = time()
# add to end of list
lst.append(0)
print(f"Appending to end of a {limit} element list: {time() - start} secs")

start = time()
# add to beginning of list
lst.insert(0, 0)
print(f"Inserting to beginning of a {limit} element list: {time() - start} secs")

start = time()
# remove from end of list
lst.pop()
print(f"Poping from end of a {limit} element list: {time() - start} secs")

start = time()
# remove from beginning of list
lst.remove(0)
print(f"Removing from beginning of a {limit} element list: {time() - start} secs")
