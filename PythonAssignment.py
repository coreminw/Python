#201610976 김민욱

import math
# Humid, Temp 는 float형
# 결과값은 소수점 첫 째 자리까지만 출력(다른 함수 사용 x)

Humid = float(input("습도를 입력하세요: "))
Temp = float(input("섭씨 온도를 입력하세요: "))

common = math.log(Humid/100) + (17.62*Temp)/(243.12+Temp)
dewPoint = (243.12*common)/(17.62-common)

dewP = int(dewPoint*10)
print(dewp/10)