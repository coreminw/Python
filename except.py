try:
    fname = "/Users/kimminwook/Desktop/nodejs/1.html"
    f = open(fname)
except FileExistsError:
    print("Could not Exist " + fname)
except FileNotFoundError:
    print("Could not open " + fname)
except UnicodeDecodeError:
    print("파일 저장 인코딩방법을 확인해주세요 " + fname)
except :
    print("다른 종류의 오류 발생" + fname)