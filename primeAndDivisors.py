def readNumber():
    num = int(input("2 이상의 정수를 입력하세요: "))

    if num >=2:
        return num
    else:
        while num <= 1:
            print("2이상의 정수를 입력하세요!")
            num2 = int(input("2 이상의 정수를 입력하세요: "))
            if num2 >= 2:
                return num2
            else:
                continue

def getDivisors(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor

def isPrime(num):
    prime = 0
    for i in range(1, num + 1):
        if num % i == 0:
            prime = prime + 1
    if prime == 2:
        return True
    else:
        return False

def func():
    num = int(readNumber())
    if num >= 2:
        for i in range(2, num+1):
            print("정수: ", i, "약수 개수: " + str(len(getDivisors(i))) + "소수: " + str(isPrime(i)))


print(func())
