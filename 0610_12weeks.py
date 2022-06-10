def shapeCircle():
    x = int(input("x 좌표를 입력하시오: "))
    y = int(input("y 좌표를 입력하시오: "))
    b = int(input("반지름을 입력하시오: "))
    t = (x,y,b)
    return t


def shapeTriangle():
    pass

def shapeRectangle():
    pass

answer = input("도형을 입력하세요: ")
if answer == '원':
    l = []
    s1 = shapeCircle()
    l.append(answer)
    l.append(s1)
    print(l)
elif answer == '사각형':
    l = []
    s2 = shapeRectangle()
    t = (s2,)
    l.append(answer)
    l.append(t)
elif answer == '삼각형':
    l = []
    s3 = shapeTriangle()
    t = (s3,)
    l.append(answer)
    l.append(t)