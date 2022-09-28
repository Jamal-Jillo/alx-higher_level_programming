#!/usr/bin/python3
import time
start = time.time()
def factors(x):
    new = 0
    for i in range(1, x):
        if x % i == 0:
            if new > i:
                new = new
            else:
                new = i
        n = x // new
    
print("{:d} = {} * {}".format(x, new, n))
end = time.time()
tt = end - start
print("\n"+ str(tt))

def factor(x):
    new = 0
    i = 1
    while i in range(1, x):
        if x % i == 0:
            new = new
        else:
            new = i
    n = x // new
print("{:d} = {} * {}".format(x, new, n))
    






factors(20)
factors(4)
factors(12)
factors(34)
factors(128)
factors(1024)
factors(4598)
#factors(1718944270642558716715)
factors(9)
factors(99)
factors(999)
factors(9999)
#factors(9797973)
factors(49)
#factors(239809320265259)


def helo():
    x = 5
    for i in range(1, 10):
        print(i)
    return
    for i in range(
        
    )