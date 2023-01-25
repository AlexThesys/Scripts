import os, sys

if len(sys.argv) < 3:
    raise Exception("Please provide the path to the log file and a match!")

fp = sys.argv[1]

f = open(fp, 'r')
match = sys.argv[2]
missing_list = []
while True:
    line = f.readline()
    if not line:
        break
    if match in line:
        stat_entry = line[line.find(match[0]):]
        if not stat_entry in missing_list:
            missing_list.append(stat_entry)

f.close()
fp = sys.argv[1] + ".stats"
f = open(fp, 'w')
for line in missing_list:
    f.write(line)
