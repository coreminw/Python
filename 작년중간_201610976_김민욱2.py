# 세 개 단어 이상으로 구성된 문자열에서 첫 번째와 세 번째 단어를 이어 붙여 새로운 문자열을 만들어서 반환
def three(str):
    s = str.strip()
    idx = s.find(' ')
    first = s[:idx]
    daum = s[idx + 1:].strip()
    idx = daum.find(' ')
    if idx == -1:
        return first
    daum = daum[idx + 1:].strip()
    idx = daum.find(' ')
    if idx == -1:
        print(first + ' ' + daum + ',', len(first + ' ' + daum))




str = input("단어를 입력하세요:")
if str.find(' ') == -1:  # 주어진 문자열이 없다면
    print("최소 두개 단어로 입력하세요")
else:
    print(three(str))


