# 실습 03-01
# 사용자로부터 월(month)을 영어단어로 입력받고
# 해당 월이 몇일까지 있는지 화면에 출력하는 프로그램
s = input("month 를 영어 단어로 입력 하세요. 단, 첫 글자는 대문자 : ")

if s == 'January':
    print("1월은 31일까지 있습니다.")
elif s== 'February':
    print("2월은 28일까지 있습니다.")
elif s== 'March':
    print("3월은 31일까지 있습니다.")
elif s== 'February':
    print("4월은 30일까지 있습니다.")
else:
    print("잘못된 입력입니다.")

# 실습 03-02
# 컴퓨터와 사람의 주사위 던지기
import random

computer = random.randint(1,6)
person = int(input("1~6 사이의 정수를 입력하세요: "))
if person > 6:
    print("1-6 사이의 숫자가 아닙니다. 다시 입력하세요.")
elif person > computer:
    print("사용자 승")
else:
    print("컴퓨터 승")