# 예외처리

try:
    fname = "/Users/kimminwook/PycharmProjects/pythonProgramming/venv/0609_9weeks.py"
    f = open(fname)
except:
    print("Could not open ", fname)