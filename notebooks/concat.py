import sys
a = sys.argv[1]
b = sys.argv[2]
ab = sys.argv[3]
reada = open(a).read()
readb = open(b).read()
with open (ab,"w") as f:
    f.write(reada)
    f.write(readb)
print(open(ab).read())
