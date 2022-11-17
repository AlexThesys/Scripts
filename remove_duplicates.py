import os, sys

if len(sys.argv) < 2:
    raise Exception("Please provide the path to the file!")

fp = sys.argv[1]

f = open(fp, 'r')
unique_list = []
while True:
    line = f.readline()
    if not line:
        break
    unique_list.append(line)

i = 0
while i < (len(unique_list) - 1):
    j = i + 1
    while j < (len(unique_list)):
        if unique_list[i] == unique_list[j]:
            print(unique_list[j])
            del unique_list[j]
        else:
            j += 1
    i += 1
            
f.close()
fp = sys.argv[1] + ".edit"
f = open(fp, 'w')
for line in unique_list:
    f.write(line)
