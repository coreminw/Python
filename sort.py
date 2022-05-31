file_path_MP09Data1 = "/Users/kimminwook/Downloads/MP09/MP09Data1.txt"
file_path_MP09Data2 = "/Users/kimminwook/Downloads/MP09/MP09Data2.txt"

f1 = open(file_path_MP09Data1)
f2 = open(file_path_MP09Data2)

lines1 = f1.readlines()
lines2 = f2.readlines()
lines = lines1 + lines2


for i in range(len(lines)):
     max = i
     for j in range(i + 1, len(lines)):
        if lines[j] > lines[max]:
            max = j
     lines[i], lines[max] = lines[max], lines[i]

print(lines)

