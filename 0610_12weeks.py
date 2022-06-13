import math

# def shape(shape,n):
#     l = []
#     for i in range(n):
#         n = int(input("정수를 입력하세요: "))
#         l.append(n)
#     t = tuple(l)
#     l2 = []
#     l2.append(shape)
#     l2.append(t)
#     return l2
#
#
# def shapeCircle():
#     x = int(input("x 좌표를 입력하세요: "))
#     y = int(input("y 좌표를 입력하세요: "))
#     r = int(input("반지름을 입력하세요: "))
#     area = 3.14 * x * y
#     # t = (x, y, r)
#     # l = []
#     # l.append(shape)
#     # l.append(t)
#     return area

# def shapeTriangle():
#     x1 = int(input("x1 좌표를 입력하세요: "))
#     y1 = int(input("y1 좌표를 입력하세요: "))
#     x2 = int(input("x2 좌표를 입력하세요: "))
#     y2 = int(input("y2 좌표를 입력하세요: "))
#     x3 = int(input("x3 좌표를 입력하세요: "))
#     y3 = int(input("y3 좌표를 입력하세요: "))
#     if x1 > x2:
#         area = ((x1 - x2) * (y3 - y1)) / 2
#     elif x2 > x1:
#         area = ((x2 - x1) * (y3 - y2)) / 2
#     # t = (x1, y1, x2, y2, x3, y3)
#     # l = []
#     # l.append(shape)
#     # l.append(t)
#     print(type(area))
#     return area



# def shapeRectangle():
#     x1 = int(input("x1 좌표를 입력하세요: "))
#     y1 = int(input("y1 좌표를 입력하세요: "))
#     x2 = int(input("x2 좌표를 입력하세요: "))
#     y2 = int(input("y2 좌표를 입력하세요: "))
#     area = (x1 - x2) * (y1 - y2)
#     # t = (x1, y1, x2, y2)
#     # l = []
#     # l.append(shape)
#     # l.append(t)
#     print("면적: ", area)
#
# def readData(n):
#     # dataList = []
#     for i in range(n):
#         answer = input("도형을 입력하세요: ")
#         if answer == '원':
#             sc = shapeCircle()
#             print(sc)
#             # dataList += sc
#         elif answer == '사각형':
#             sc = shapeRectangle()
#             print(sc)
#             # dataList += sc
#         elif answer == '삼각형':
#             sc = shapeTriangle()
#             print(sc)
#             # dataList += sc
#
#
# print(readData(5))


# f = open("/Users/kimminwook/Downloads/MP07data.utf8.txt", "r")
#
# def readData2():
#     for i in range(5):
#         whatSahpe = f.readline()
#         print("도형을 입력하세요: ", whatSahpe)
#         if whatSahpe == '사각형':
#             x1 = f.readline()
#             y1 = f.readline()
#             x2 = f.readline()
#             y2 = f.readline()
#         elif whatSahpe == '삼각형':
#             x1 = f.readline()
#             y1 = f.readline()
#             x2 = f.readline()
#             y2 = f.readline()
#             x3 = f.readline()
#             y3 = f.readline()
#         elif whatSahpe == '원':
#             x = f.readline()
#             y = f.readline()
#             r = f.readline()


def xy():
    x = int(input("x 좌표를 입력하시오: "))
    y = int(input("y 좌표를 입력하시오: "))
    return (x,y)

def readingData():
    myList = []
    for i in range(5):
        whatShape = input("도형의 종류를 입력하시오: ")
        if whatShape == "사각형":
            x1, y1 = xy()
            x2, y2 = xy()
            t = (x1, y1, x2, y2)
            myList.append(whatShape)
            myList.append(t)
        elif whatShape == "삼각형":
            x1, y1 = xy()
            x2, y2 = xy()
            x3, y3 = xy()
            t = (x1, y1, x2, y2, x3, y3)
            myList.append(whatShape)
            myList.append(t)
        elif whatShape == "원":
            x1, y1 = xy()
            r = int(input("반지름을 입력하시오: "))
            t = (x1, y1, r)
            myList.append(whatShape)
            myList.append(t)
    return myList

def circle_Area(t):
    area = math.pi * t[2] * t[2]
    return area

def rectangle_Area(t):
    w = t[0] - t[2]
    h = t[1] - t[3]
    if w < 0:
        w *= -1
    if h < 0:
        h *= -1
    area = w * h
    return area

def triangle_Area(t):
    x1 = t[0]
    y1 = t[1]
    x2 = t[2]
    y2 = t[3]
    x3 = t[4]
    y3 = t[5]
    a = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    b = math.sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1))
    c = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) + (s - b) * (s - c))

def main(myList):
    for i in range(0, len(myList), 2):
        shapeName = myList[i]
        shapeArea = myList[i+1]
        if shapeName == "원":
            area = circle_Area(shapeArea)
        elif shapeName == "사각형":
            area = rectangle_Area(shapeArea)
        elif shapeName == "삼각형":
            area = triangle_Area(shapeArea)
        print("도형: ", shapeName)
        print("면적: ", area)

lst = readingData()
main(lst)
