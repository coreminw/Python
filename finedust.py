chome = (29+21+18+34+67+79+18)/7
mese = (44+44+32+60+84+112+41)/7

if chome >=0 and chome <= 15:
    print("초미세먼지 좋음")
elif chome > 15 and chome <= 35:
    print("초미세먼지 보통")
elif chome > 35 and chome <= 75:
    print("초미세먼지 나쁨")
elif chome > 75:
    print("초미세먼지 매우 나쁨")


if mese >=0 and mese <= 30:
    print("미세먼지 좋음")
elif mese > 30 and mese <= 80:
    print("미세먼지 보통")
elif mese > 80 and mese <= 100:
    print("미세먼지 나쁨")
elif mese > 100:
    print("미세먼지 매우 나쁨")