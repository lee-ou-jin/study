import time
def fib_itar(n) :
    if(n<2): return n


    last = 0
    current =1
    for i in range (2,n+1) :
        tmp = current
        current += last
        last = tmp
    return current

def fib(n):
    if n == 0: return 0
    elif n==1: return 1
    else :
        return fib(n-1)+fib(n-2)
    

start = time.time()
for i in range(100000):
    fib_itar(6)
end = time.time()
print(end-start)


start = time.time()
for i in range(100000):
    fib(6)
end = time.time()
print(end-start)