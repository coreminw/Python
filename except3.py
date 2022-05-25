import sys

try:
    fname = "/Users/kimminwook/Desktop/nodejs/1.html"
    f = open(fname)
    lines = f.readlines()
    f.close()
except FileNotFoundError:
    print("Could not open" + fname)
    sys.exit()
except:
    print("other error occurred")
print("End of the program")
