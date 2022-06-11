def shape(shape,n):
    l = []
    for i in range(n):
        n = int(input("정수를 입력하세요: "))
        l.append(n)
    t = tuple(l)
    l2 = []
    l2.append(shape)
    l2.append(t)
    return l2



def areaCircle():
    pass

def areaRectangle():
    pass

def areaTriangle():
    pass

# def readData(n):
#     dataList = []
#     for i in range(n):
#         answer = input("도형을 입력하세요: ")
#         if answer == '원':
#             s = shape(answer, 3)
#             dataList += s
#         elif answer == '사각형':
#             s = shape(answer, 4)
#             dataList += s
#         elif answer == '삼각형':
#             s = shape(answer, 6)
#             dataList += s
#     return dataList
#
# print(readData(5))



def shapeCircle():
    x = int(input("x 좌표를 입력하세요: "))
    y = int(input("y 좌표를 입력하세요: "))
    r = int(input("반지름을 입력하세요: "))
    area = 3.14 * x * y
    # t = (x, y, r)
    # l = []
    # l.append(shape)
    # l.append(t)
    return area

def shapeTriangle():
    x1 = int(input("x1 좌표를 입력하세요: "))
    y1 = int(input("y1 좌표를 입력하세요: "))
    x2 = int(input("x2 좌표를 입력하세요: "))
    y2 = int(input("y2 좌표를 입력하세요: "))
    x3 = int(input("x3 좌표를 입력하세요: "))
    y3 = int(input("y3 좌표를 입력하세요: "))
    if x1 > x2:
        area = ((x1 - x2) * (y3 - y1)) / 2
    elif x2 > x1:
        area = ((x2 - x1) * (y3 - y2)) / 2
    # t = (x1, y1, x2, y2, x3, y3)
    # l = []
    # l.append(shape)
    # l.append(t)
    print(type(area))
    return area

print(shapeTriangle())

def shapeRectangle():
    x1 = int(input("x1 좌표를 입력하세요: "))
    y1 = int(input("y1 좌표를 입력하세요: "))
    x2 = int(input("x2 좌표를 입력하세요: "))
    y2 = int(input("y2 좌표를 입력하세요: "))
    area = (x1 - x2) * (y1 - y2)
    # t = (x1, y1, x2, y2)
    # l = []
    # l.append(shape)
    # l.append(t)
    print("면적: ", area)

def readData(n):
    # dataList = []
    for i in range(n):
        answer = input("도형을 입력하세요: ")
        if answer == '원':
            sc = shapeCircle()
            print(sc)
            # dataList += sc
        elif answer == '사각형':
            sc = shapeRectangle()
            print(sc)
            # dataList += sc
        elif answer == '삼각형':
            sc = shapeTriangle()
            print(sc)
            # dataList += sc


print(readData(5))