import sys
import random
text = sys.argv[1]
lista = list(open(text).read().split("%"))
print(random.choice(lista))
