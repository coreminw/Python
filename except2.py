try:
    str = "123a"
    num = int(str)
except ValueError:
    print("Failed converting"+ str + "to int")
except IOError:
    print("입출력 에러")
except:
    print("다른 에러")