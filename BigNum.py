def maxIntOutOf5():
    n1 = int(input("정수 입력: "))
    n2 = int(input("정수 입력: "))
    n3 = int(input("정수 입력: "))
    n4 = int(input("정수 입력: "))
    n5 = int(input("정수 입력: "))
    n = max(n1, n2, n3, n4, n5)
    return n

print(maxintoutof5())

def maxIntOutOf5_2():
    n1 = int(input("정수 입력: "))
    n2 = int(input("정수 입력: "))
    n3 = int(input("정수 입력: "))
    n4 = int(input("정수 입력: "))
    n5 = int(input("정수 입력: "))
    m = n1
    if m < n2:
        m = n2
    if m < n3:
        m = n3
    if m < n4:
        m = n4
    if m < n5:
        m = n5
    return m
print(maxIntOutOf5_2())

def maxIntOutOf5_3():
    m = int(input("정수 입력: "))
    for i in range(4):
        n = int(input("정수 입력: "))
        if m < n:
            m = n
    return m
