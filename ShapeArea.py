import math

rectStrLst = [ "x1 좌표를 입력하시오: ", "y1 좌표를 입력하시오: ", "x2 좌표를 입력하시오: ", "y2 좌표를 입력하시오: " ]
circleStrLst = [ "x 좌표를 입력하시오: ", "y 좌표를 입력하시오: ", "반지름 r값을 입력하시오: " ]
triangleStrLst = [ "x1 좌표를 입력하시오: ", "y1 좌표를 입력하시오: ", "x2 좌표를 입력하시오: ", "y2 좌표를 입력하시오: ", "x3 좌표를 입력하시오: ", "y3 좌표를 입력하시오: " ]

def readShape(shape, n, strLst):
    l = []
    for i in range(n):
        n = int(input(strLst[i]))
        l.append(n)
    t = tuple(l)
    l2 = []
    l2.append(shape)
    l2.append(t)
    return l2

def readData(n):
    dataList = []
    for i in range(n):
        s = input("도형의 종류를 입력하시오: ")
#        print(s)
        if s == "원":
            l = readShape(s, 3, circleStrLst)
#            print("l = ", end ="")
#            print(l)
            dataList += l
        elif s == "사각형":
            l = readShape(s, 4, rectStrLst)
#            print("l = ", end ="")
#            print(l)
            dataList += l
        elif s == "삼각형":
            l = readShape(s, 6, triangleStrLst)
#            print("l = ", end ="")
#            print(l)
            dataList += l
#        print(dataList)
    return dataList

def calcRectArea(t):
    return (t[2] - t[0]) * (t[1] - t[3])

def calcTriangleArea(t):
    return (t[4] - t[2]) * (t[1] - t[5]) / 2

def calcCircleArea(t):
    return math.pi * t[2] * t[2]

#['원', (...), "사각형", (...), ... ]
def calcAreas(lst):
    for i in range(0, len(lst), 2):
        shapeName = lst[i] # 모양의 이름
        shapeTuple = lst[i + 1] # 좌표 튜플
        if shapeName == "사각형":
            area = calcRectArea(shapeTuple)
        elif shapeName == "삼각형":
            area = calcTriangleArea(shapeTuple)
        elif shapeName == "원":
            area = calcCircleArea(shapeTuple)
        print(shapeName)
        print("면적:", area)

#readShape("사각형", 4, rectStrLst)
lst = readData(5)
#print(lst)
calcAreas(lst)
