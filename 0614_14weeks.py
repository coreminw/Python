class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

r1 = Rectangle(10, 50)
r2 = Rectangle(20, 30)

print(r1.getArea())
print(r2.getArea())

r1.setWidth(20)
print(r1.getArea())
print(r1.getWidth())