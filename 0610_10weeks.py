txt = """There are many variations of passages of Lorem Ipsum available,
but the majority have suffered alteration in some form, by
injected humour, or randomised words which don't look even
slightly believable. If you are going to use a passage of;
Lorem Ipsum, you need to be? sure there isn't anything embarrassing
hidden in the middle of text. All the Lorem Ipsum generators on the
Internet tend to repeat predefined chunks as necessary, making this
the first true generator on the Internet. It uses a dictionary of
over 200 Latin words, combined with a handful of model sentence
structures, to generate Lorem Ipsum which looks reasonable.
The generated Lorem Ipsum is therefore always free from repetition,
injected humour, or non-characteristic words etc!
"""


# 다음 함수들에서 pass를 지우고 본인 코드를 작성할 것

def getNextPeriodPos(txt, startPos):
    return txt[startPos:].find('.')

# print(getNextPeriodPos("Hi. I am Tom. I am a boy", 0))  # 2 출력
# print(getNextPeriodPos("Hi. I am Tom. I am a boy", 3))  # 9 출력
# print(getNextPeriodPos("Hi. I am Tom. I am a boy", 13)) # -1 출력



def getNextLine(txt, startPos):
    if startPos >= len(txt):
        return "" # 빈 문자열
    idx = getNextPeriodPos(txt, startPos)
    if idx == -1:
        return txt[startPos:].strip()
    else:
        return txt[startPos:startPos + idx + 1].strip()

# print(getNextLine("Hi. I am Tom. I am a boy", 0))  # Hi. 출력
# print(getNextLine("Hi. I am Tom. I am a boy", 3))  # I am Tom. 출력
# print(getNextLine("Hi. I am Tom. I am a boy", 13)) # I am a boy 출력


def countWordsInLine(line):
    # s = line.strip().count(' ') + line.strip().count('\n') +line.strip().count('\t')
    # return s + 1
    # 공백의 개수를 세고 +1을 하면 단어 수 세기
    newLine = line.strip()
    count = 0
    for ch in newLine:
        if ch == ' ' or ch == '\n' or ch == '\t':
            count += 1
    return count + 1
# print(countWordsInLine("I am Tom.")) # 3 출력



def countPunctuationsInLine(line):
    count = 0
    for ch in line:
        if ch == '.' or ch == '?' or ch == '!' or ch == ',':
            count += 1
    return count

print(countPunctuationsInLine("Hi, I am Tom.")) # 2 출력


def main(txt):
    lineNum = 1 # 줄번호
    newTxt = txt.strip()
    startPos = 0
    line = getNextLine(newTxt, startPos)
    while line != "":
        print(str(lineNum) + ": " + line)
        print("Number of words in line #" + str(lineNum) + ": " + str(countWordsInLine(line)))
        print("Number of Puctuations in line #" + str(lineNum) + ": " + str(countWordsInLine(line)))
        lineNum += 1
        idx = getNextPeriodPos(newTxt, startPos)
        if idx != -1:
            startPos += (idx+1)
            line = getNextLine(newTxt, startPos)
        else:
            line = ""

main(txt)
