def onefoot(time):
    if time >= 80:
        return "균형 나이는 20대 입니다."
    elif time >= 75 and time < 80:
        return "균형 나이는 30대 입니다."
    elif time >= 50 and time < 75:
        return "균형 나이는 40대 입니다."
    elif time >= 35 and time < 50:
        return "균형 나이는 50대 입니다."
    elif time >= 10 and time < 35:
        return "균형 나이는 60대 입니다."
    elif time >= 5 and time < 10:
        return "균형 나이는 70대 입니다."
    elif time < 5:
        return "균형 나이는 80대 입니다."


age = int(input("나이를 입력하세요: "))
time = int(input("눈을 감고 양팔을 벌리고 외발로 서있을 수 있는 시간을 입력하세요: "))

# if age >= 10 and age < 20:
#     age = 10
# elif age >= 20 and age < 30:
#     age = 20
# elif age >= 30 and age < 40:
#     age = 30
# elif age >= 40 and age < 50:
#     age = 40
# elif age >= 50 and age < 60:
#     age = 50
# elif age >= 60 and age < 70:
#     age = 60
# elif age >= 70 and age < 80:
#     age = 70
# else:
#     age = 80


# print("당신의 나이는 " + str(age) + "대 이지만, ", end='')
# onefoot(time)

print("당신의 나이는 " + str((age//10)*10) + "대 이지만, " + onefoot(time))