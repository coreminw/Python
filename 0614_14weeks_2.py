# 딕셔너리(Dictionary)
# { 키1 : 값1, 키2 : 값2 }
# 키는 수정 불가능, 값은 변경 가능, 중복된 키가 포함될 수 없음

d = { 'a': 3 , 'b' : 3, 3 : 5}
print(d)

print(d['a'])
print(d[3]) # print(d.get(3)) 과 똑같음
d[3] = 7 # 키 3의 값을 바꿈
print(d)

d['5'] = 5 # 새로운 값 추
print(d)

# update() 함수를 쓰면 새로 바꾸는 것과 추가도 가능

print("------------")

lst = ["국어", 90, "수학", 80, "영어", 70]

d2 = {}
for i in range(0, len(lst), 2):
    d2[lst[i]] = int(lst[i + 1])

sum = 0
for n in d2:
    print(n + ":", d2[n])
    sum += d2[n]
print("평균 :", sum/3)

print("------------")

s = input("영문 문자열을 입력하세요: ")
d3 = {}
for ch in s:
    if ch in d3:
        d3[ch] += 1
    else:
        d3[ch] = 1
print(d3)

print("------------")

st = input("영문 문자열을 입력하세요: ")
lst1 = []
lst2 = []
for ch in st:
    if ch.isdigit():
        lst1 += ch
    elif ch.isalpha():
        lst2 += ch

print("숫자 개수: ", len(lst1))
print("알파벳 개수", len(lst2))

d = {"동대문구" : 165924, "은평구": 212725, "종로구" :156567 , "중구": 133708, "용산구" : 112881, "성동구" : 135883}

s = input("자치구를 입력하세요: ")

for i in d:
    if s == i:
        print(d[i])