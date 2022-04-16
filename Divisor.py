def getSumOfDivisors(num):
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0: # 약수
            sum += i
        return sum

n = int(input("1000이하의 정수 입력: "))
print(getSumOfDivisors(n))