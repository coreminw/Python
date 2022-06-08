# 9주차
# 재귀호출


# n! = n x (n-1) x (n-2) x ... x 1
#    = n x (n-1)!
def factorial(n):
    ft = 1
    for i in range(n, 0, -1):
        ft *= i
    return ft

def factorial2(n):
    if n < 1 and n >= 0:
        return 1 #재귀호출 탈출 조건
    else:
        return n * factorial(n - 1)
print(factorial(10))
print(factorial2(10))

def gcd(m,n):
    if m == n:
        return m
    elif m > n:
        return gcd(m-n, n)
    else: # m < n
        return gcd(m, n-m)