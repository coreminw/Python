# 불쾌지수 계산
def bulque(temp, humid):
    DI = 0.81 * temp + 0.01 * humid * (0.99 * temp - 14.3) + 46.3
    if DI > 83:
        print("대부분의 사람들이 불쾌감을 느낌")
    elif DI >= 80 and DI <= 83:
        print("50% 정도의 사람들이 불쾌감을 느낌")
    elif DI >= 70 and DI < 80:
        print("일부 사람들이 불쾌감을 느낄 수 있음")
    elif DI < 70:
        print("쾌적함")

temp = int(input("온도를 입력하세요: "))
humid = int(input("습도를 입력하세요: "))

print(bulque(temp, humid))