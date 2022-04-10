#201610976 김민욱

def yoon(year): #윤년확인
    if year % 400 ==0 or (year % 4 == 0 and year % 100 !=0):
        return "윤년입니다."
    return "윤년이 아닙니다."

def checkY(jumin):
    if jumin[:2].isdigit():
        if int(jumin[:2]) <= 22:
            return int('20' + jumin[:2])
        elif int(jumin[:2]) >= 23 and int(jumin[:2]) <= 99:
            return int('19' + jumin[:2])
        else:
            return False
    else:
        print("년도가 위치한 자리의 글자가 숫자가 아닙니다.")
        return 0

def checkM(jumin):
    if jumin[2:4].isdigit():
        if int(jumin[2:4]) >= 1 and int(jumin[2:4]) <= 12:
            return int(jumin[2:4])
        else:
            return 0

def checkD(jumin, year, month):
    if jumin[4:6].isdigit():
        if year != 0 and month >= 1 and month <= 12:
            if (month == 1 or month == 3 or month ==5 or month == 7 or month == 8 or month == 10 or month == 12) and int(jumin[4:6] <= 31):
                return int(jumin[4:6])
            elif (month == 4 or month == 6  or month == 9 or month == 11 ) and int(jumin[4:6]) <= 30:
                return int(jumin[4:6])
            elif month == 2 and (yoon(year)==True) and month <=29:
                return int(jumin[4:6])
            elif month == 2 and (yoon(year)==False) and month <=28:
                return int(jumin[4:6])
            else:
                return 0


def ManOrGirl(jumin, year):
    if jumin[7:8].isdigit():
        if (int(jumin[7:8]) == 1 or int(jumin[7:8]) == 2) and (year >= 1900 and year <= 1999) :
            return jumin[7:8]
        elif (int(jumin[7:8]) == 3 or int(jumin[7:8]) == 4) and year >= 2000:
            return jumin[7:8]
        else:
            return 0
    else:
        return 0



# def isValid(jumin):
#     if len(jumin) == 14 and jumin[6] == '-':
#         return True
#     else:
#         print("주민등록 번호의 길이가 맞지 않습니다.")
#         return False

def isValid(jumin, year):
    if year % 400 ==0 or (year % 4 == 0 and year % 100 !=0):
        print("윤년입니다.")
    else:
        print("윤년이 아닙니다.")

    if jumin[2:4].isdigit():
        if int(jumin[2:4]) >= 1 and int(jumin[2:4]) <= 12:
            print("올바른 월 입니다.")
        else:
            print("월이 1~12의 범위 내에 포함되지 않습니다.")
            return False

    if jumin[4:6].isdigit():
        month = int(jumin[2:4])
        if year != 0:
            if (month == 1 or month == 3 or month ==5 or month == 7 or month == 8 or month == 10 or month == 12) and int(jumin[4:6] <= 31):
                print("날짜가 올바릅니다.")
            elif (month == 4 or month == 6  or month == 9 or month == 11 ) and int(jumin[4:6]) <= 30:
                print("날짜가 올바릅니다.")
            elif month == 2 and (yoon(year)==True) and month <=29:
                print("날짜가 올바릅니다.")
            elif month == 2 and (yoon(year)==False) and month <=28:
                print("날짜가 올바릅니다.")
            else:
                print("날짜가 올바르지 않습니다.")
                return False

    if jumin[7:8].isdigit():
        if (int(jumin[7:8]) == 1 or int(jumin[7:8]) == 2) and (year >= 1900 and year <= 1999):
            print("2000년 이전 출생자 입니다.")
        elif (int(jumin[7:8]) == 3 or int(jumin[7:8]) == 4) and year >= 2000:
            print("2000년 이후 출생자 입니다.")
        else:
            print("다시입력하세요. 2000년 이전 출생자는 1 or 2 로 시작합니다. 2000년 이후 출생자는 3 or 4 로 시작합니다.")
            return False
    else:
        print("뒷번호를 잘못 입력하였습니다.")
        return False


    if len(jumin) == 14 and jumin[6] == '-':
        return("주민등록번호로 적합해 보입니다.")
    else:
        print("주민등록번호로 적합하지 않습니다.")
        return False

#isValid()
jumin = input("주민등록번호를 입력하세요: ")
year = int(input('년도를 입력하세요'))
print(isValid(jumin, year))


# 첫번째 함수
# year = int(input("연도를 입력하세요: "))
# print(yoon(year))
#
# # 두번째 함수
# jumin = input("주민등록번호를 입력하세요: ")
# print(checkY(jumin))
#
# #세번째 함수
# jumin2 = input("주민등록번호를 입력하세요: ")
# print(checkM(jumin2))

# #네번째 함수
# jumin3 = input("주민등록번호를 입력하세요: ")
# year = int(input('년도를 입력하세요'))
# month = int(input('월을 입력하세요'))
# print(checkD(jumin3,year,month))

#다섯번째 함수
# jumin4 = input("주민등록번호를 입력하세요: ")
# year = int(input('년도를 입력하세요'))
# print(ManOrGirl(jumin4, year))

#여섯번째 함수
# jumin5 = input("주민등록번호를 입력하세요: ")
# print(isValid(jumin5))
