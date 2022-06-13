import math

f = open("/Users/kimminwook/Downloads/MP07data.utf8.txt", "r")

def xy(f, n):
    l = []
    for i in range(n):
        line = f.readline()
        line = line.strip()
        num = int(line)
        l.append(num)
    t = tuple(l)
    return t


def readData(f):
    myList = []
    s = f.readline()
    while s:
        s = s.strip()

        if s == '사각형':
            l = []
            cood = xy(f, 4)
            l.append(s)
            l.append(cood)
            myList += l
        elif s == "삼각형":
            l = []
            cood = xy(f, 6)
            l.append(s)
            l.append(cood)
            myList += l
        elif s == "원":
            l = []
            cood = xy(f, 3)
            l.append(s)
            l.append(cood)
            myList += l
        s = f.readline()
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
    c =math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
    s = (a + b + c)  / 2
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

lst = readData(f)
main(lst)