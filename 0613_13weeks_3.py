f1 = open("/Users/kimminwook/Downloads/MP09/MP09Data1.txt", "r")
f2 = open("/Users/kimminwook/Downloads/MP09/MP09Data2.txt", "r")

files1 = f1.readlines()
files2 = f2.readlines()

length1 = len(files1)
length2 = len(files2)

l = []
idx1 = 0
idx2 = 0

while idx1 < length1 and idx2 < length2:
    if float(files1[idx1]) > float(files2[idx2]):
        l.append(float(files1[idx1]))
        idx1 += 1
    else:
        l.append(float(files2[idx2]))
        idx2 += 1

while idx1 < length1:
    l.append(float(files1[idx1]))
    idx1 += 1

while idx2 < length2:
    l.append(float(files1[idx2]))
    idx2 += 1

print(length1)
print(length2)

for i in l:
    print(i)