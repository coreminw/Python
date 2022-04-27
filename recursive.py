# 재귀함수
# 탈출 조건을 꼭 만들어줘야함

# Factorial 구하는 재귀함수
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(1))
print(factorial(10))


# 최대공약수 구하는 알고리즘
def gcd(m, n): #정의가 다 되어있음
    if m == n:
        return m
    elif m > n:
        return gcd(m-n, n)
    else:
        return gcd(m, n-m)

print(gcd(12, 8))


# 피보나치 수열
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n - 2)