import time
start = time.time()

def factorial(n):
    if n == 1 :
        return 1
    else:
        return n* factorial(n -1)

def factorial_for(n):
    result = 1
    for k in range(n,0,-1):
        result *= k
    return result 



print(factorial_for(100))

print("time :", time.time()) 