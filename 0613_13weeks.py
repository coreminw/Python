# 예외처리

try:
    fname = "/Users/kimminwook/PycharmProjects/pythonProgramming/venv/0609_9weeks.py"
    f = open(fname)
except FileNotFoundError:
    print(fname + "파일이 없습니다. 파일 이름을 다시 확인하세요")
except:
    print("Could not open "+ fname)