import sys
filename = sys.argv[1]
lines = open(filename).read().split("\n")
lines = lines[:5]
for line in lines:
    print(line)
