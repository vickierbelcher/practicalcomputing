import sys
text = sys.argv[1]
lista = list(open(text).readlines())
reverselist = lista[::-1]
for item in reverselist:
    print(item)
