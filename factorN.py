import sys
import math
from time import perf_counter

res = []
r = []

#def sortbySUM():

def factorN(num, last):
    for i in range(last, int(math.sqrt(num))+1):
        if (num%i == 0):
            r.append(i)
            if (len(r) == amount-1):
                res.append(' '.join([str(el) for el in r]) + ' ' + str(num//i))
            else:
                factorN(num//i, i)
            r.pop()
            
number, amount = input().split()
number = int(number)
amount = int(amount)

start = perf_counter()
factorN(number, 1)
end = perf_counter()
print("time elapsed: ", end-start)

with open('factors.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file
    print('\n'.join(res))
