import random

def rollDice(num):
    n1 = 0  # 앞면이 나온 횟수
    n2 = 0  # 뒷면이 나온 횟수
    for i in range(num):
        n = random.randint(1,2)
        if n == 1:
            n1 += 1
        else: # n == 2
            n2 += 1
    print("앞면 = ", n1)
    print("뒷면 = ", n2)

print(rollDice(10))
