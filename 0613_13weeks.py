# 예외처리
import sys
try:
    fname = "/Users/kimminwook/PycharmProjects/pythonProgramming/venv/0609_9weeks.py"
    f = open(fname)
except FileNotFoundError:
    print(fname + " 파일이 없습니다. 파일 이름을 다시 확인하세요.")
except UnicodeDecodeError:
    print(fname + " 파일 저장 인코딩 방법을 확인해주세요.")
except:
    print("다른 종류의 오류 발생 "+ fname)


try:
    s = "123a"
    num = int(s)
except ValueError:
    print("Faild converting " + s + " to int")
    sys.exit()
except IOError:
    print("IOError occur")
    sys.exit()
except:
    print("다른 종류의 오류 발생 ")
    sys.exit()

print("end")