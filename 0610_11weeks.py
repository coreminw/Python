# readline
f = open("/Users/kimminwook/PycharmProjects/pythonProgramming/venv/0609_9weeks.py", "r")
line = f.readline()

while line:
    print(line, end = "")
    line = f.readline()
f.close()

# readlines => 파일 전체를 읽어서 리스트에 저장
f = open("/Users/kimminwook/PycharmProjects/pythonProgramming/venv/0609_9weeks.py", "r")
lines = f.readlines()

for line in lines:
    print(line, end = "")

f.close()


f = open("/Users/kimminwook/Desktop/Convert.rtf", "r")
folderName = f.readline()
fileName = f.readline()
f.close()

f2 = open(folderName.strip() + "/" + fileName.strip(), "r")
lines = f2.readlines()

for line in lines:
    print(line, end = "")