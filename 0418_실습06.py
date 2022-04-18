# 실습 06-01
# 사용자로부터 숫자 5개를 입력받고, 가장 큰 값을 찾아서 반환하는 함수를 작성하고 이를 활용하는 프로그램을 구현
num = int(input("숫자 5개 입력 하기: "))
for i in range(4):
    num2 = int(input("숫자 5개 입력 하기: "))
    if num < num2:
        num = num2

print(num)

number = int(input("숫자 5개 입력 하기: "))
number2 = int(input("숫자 5개 입력 하기: "))
number3 = int(input("숫자 5개 입력 하기: "))
number4 = int(input("숫자 5개 입력 하기: "))
number5 = int(input("숫자 5개 입력 하기: "))

print(max(number, number2, number3, number4, number5))


# 실습 06-02
# 동전을 던져서 앞/뒷면이 나오는 횟수를 세고, ½확률에 수렴하는지 확인하는 프로그램을 작성
import random

def coins(coin):
    ap = 0
    d = 0
    for i in range(coin):
        n = random.randint(1,2)
        if n == 1:
            ap += 1
        else:
            d += 1
    print("앞면 = ", ap)
    print("뒷면 = ", d)

print(coins(100))

# 실습 06-03
# 1000이하의 숫자를 사용자로부터 입력받고,
# 해당숫자의 모든 약수의 합을 화면에 출력하는 프로그램을 작성
def getSum(num):
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sum += i
    return sum

n = int(input("1000이하의 정수 입력: "))
print(getSum(n))


# 실습 06-04
# 사용자가 1000을 입력할때까지 정수를 지속적으로 입력받고,
# 가장 큰 수를 찾아서 화면에 출력하는 프로그램을 작성

number = int(input("입력: "))

while(number != 1000):
    number2 = int(input("입력: "))
    if number < number2:
        number = number2

print(number)
