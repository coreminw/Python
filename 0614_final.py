# 파이썬 코드 파일을 읽고 사용자로부터 입력 받은 단어를 검색해서 결과를 출력하는 프로그램을 작성한다.
import sys

# 파일에서 모든 내용을 읽어서 리스트를 구성한 후에 반환하는 함수 구현(이름과 매개변수는 본인이 정할 것) (10점)
# 데이터 파일은 ANSI(cp949) 또는 utf-8로 저장됨(어떤 형식으로 저장될 지 모르므로 예외 처리를 통해서 두 가지 형식 모두 처리 가능하도록 만들 것)
# 파일이 없는 경우 예외 처리를 통해 파일이 없음을 화면에 출력하고 스크립트를 종료(프로그램 실행을 종료)시킬 것
# 파일에 있는 각 줄(line)의 내용(줄바꿈 문자(‘\n’) 제거할 것)을 리스트의 요소로 구성하고, 리스트를 반환

def AllFileLst(file):
    lst = []
    try:
        f = open(file)
        lst = f.readlines()
        f.close()
    except UnicodeDecodeError:
        f = open(file, encoding="utf-8")
        lst = f.readlines()
        f.close()
    except FileNotFoundError:
        print("파일이 없습니다.")
        sys.exit()
    for i in range(len(lst)):
        lst[i] = lst[i].rstrip()
    return lst

# 리스트에 있는 각 요소(한 줄(line)의 문자열)에 대해 다음 작업을 처리할 것 (총 25점)
# 한 줄(line)의 문자열과 검색할 문자열을 매개 변수를 통해 입력 받고 해당 단어가 나타나는 위치를 튜플(tuple)로 구성해서 반환하는 함수 구현 (이름은 본인이 정하고, 필요하면 매개 변수 추가 가능) (12점)
# 한 줄의 문자열에 단어가 반복되어 나올 수 있음(그런 경우 모든 위치를 튜플의 요소로 구성)
# 단어가 여러 번 나옴에도 불구하고 가장 첫 번째 단어의 위치만 튜플로 구성하는 경우는 7 점 감점(한 문장에서 한 개의 위치만 포함시키는 경우)
# 단어의 위치는 문자열에서 해당 단어가 시작하는 문자열의 인덱스 + 1 (첫 번째 글자의 위치가 1 부터 시작됨)
#     예를 들어 “문자열 문자”라는 문자열에서 “문자”를 검색하는 경우 튜플 (1, 5)가 반환됨
# 주어진 문자열에 검색할 문자열이 없으면 빈 튜플(empty tuple) 또는 None 반환

def lineSurf(line, findstr):
    t = ()
    a = line.find(findstr) # 검색해서 찾은 문자열
    location = 0  # 문자열의 해당 위치

    while a != -1: # line 이 끝나면 False
        t = t + (location + (a + 1),)
        location += (a + len(findstr))
        line = line[a + len(findstr):]
        a = line.find(findstr)
    return t


# 사용자로부터 파일 이름을 입력 받기
# 사용자가 빈 문자열을 입력하는 경우(내용 없이 엔터 키만 입력하는 경우) 제대로 입력할 때까지 다시 입력 받을 것

fileName = input("파일 이름을 입력하세요: ")

while fileName == '':
    fileName = input("빈 문자열을 입력하였습니다. 다시 입력하세요: ")

lst = AllFileLst(fileName)


# 사용자로부터 검색할 문자열을 입력 받기 (5점)
# 사용자가 빈 문자열을 입력하는 경우(내용 없이 엔터 키만 입력하는 경우) 제대로 입력할 때까지 다시 입력 받을 것

findStr = input("검색할 문자열을 입력하세요: ")
while findStr == '':
    findStr = input("빈 문자열 입니다. 다시 입력하세요: ")


# 앞에서 만든 함수로부터 반환되는 튜플은 한 줄의 문자열과 묶어서 리스트로 구성할 것 (5 점)
# 문자열에서 검색할 문자열이 존재하는 경우에 대해서만 리스트로 구성할 것
# 리스트의 첫 번째 요소는 튜플, 두 번째 요소는 문자열임. 예를 들어 앞에서 보인 것처럼
# “문자열 문자”에서 “문자”를 검색했다면, 여기서 구성되는 리스트는 [(1, 5), “문자열 문자”]가 됨
# 파일에서의 줄(line) 번호를 키(key)로 앞에서 구성한 리스트를 값(value)으로 딕셔너리(dictionary)에 넣을 것 (5 점)
# 줄 번호는 1 부터 시작됨

d = {}
for i in range(len(lst)):
    l = []
    tp = lineSurf(lst[i], findStr)
    if len(tp) > 0:
        l.append(tp)
        l.append(lst[i])
        d[i + 1] = l


# 딕셔너리에 내용이 있으면 > 줄_번호 : (위치 정보 튜플) : 문자열(한 줄에 해당되는 문자열)
# 딕셔너리에 내용이 없으면 > “검색할_문자열” 을(를) 파일에서 찾을 수 없습니다
if len(d) == 0:
    print(findStr + " 을(를) 파일에서 찾을 수 없습니다")
else:
    for i in d:
        print(i, " : ", d[i][0], " : ", d[i][1])


# /Users/kimminwook/Downloads/MP09/MP07data.utf8.txt




