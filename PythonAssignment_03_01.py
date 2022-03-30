#201610976 김민욱

#03-01
def yoon(year):
    if(year % 4 == 0) or (year % 400 == 0):
        if(year % 4 == 0) and (year % 100 == 0) and (year % 400 != 0):
            print(str(year)+"는 윤년이 아닙니다.")
        else:
            return print(str(year)+"는 윤년입니다.")
    else:
        print(str(year)+"는 윤년이 아닙니다.")

year1 = int(input(" 년도를 입력하세요: "))
print(yoon(year1))




