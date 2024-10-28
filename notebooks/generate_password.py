import sys
import string
import random
n = int(sys.argv[1])
possiblevalues = (list(string.ascii_letters) + list(string.digits))
passwordlength = list(range(1,n+1,1))
password = []
for p in passwordlength:
    randomvalue = random.choice(possiblevalues)
    password.append(randomvalue)
print("".join(password))
