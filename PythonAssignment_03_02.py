def yoon(year1):
    if(year1 % 4 == 0) or (year1 % 400 == 0):
        if(year1 % 4 == 0) and (year1 % 100 == 0) and (year1 % 400 != 0):
            return False
        else:
            return True
    else:
        return False

year = int(input("년도를 입력하세요: "))
month = int(input("월을 입력하세요: "))
day = int(input("일을 입력하세요: "))

dayOfYear1_2 = (month-1) * 31 + day
dayOfYear3_12 = dayOfYear1_2 - ((4 * month + 23)//10)

if month <= 2:
    print("통일: "+str(dayOfYear1_2))
elif month >= 3:
    if yoon(year) == True:
        print("통일: " + str(dayOfYear3_12+1))
    else:
        print("통일: " + str(dayOfYear3_12))