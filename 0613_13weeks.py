# 예외처리

try:
    fname = "/Users/kimminwook/PycharmProjects/pythonProgramming/venv/0609_9weeks.py"
    f = open(fname)
except FileNotFoundError:
    print(fname + " 파일이 없습니다. 파일 이름을 다시 확인하세요.")
except UnicodeDecodeError:
    print(fname + " 파일 저장 인코딩 방법을 확인해주세요.")
except:
    print("다른 종류의 오류 발생 "+ fname)