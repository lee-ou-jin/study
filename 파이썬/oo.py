import time
start = time.time()

def contains(bag,e) :
    return e in bag
def insert(bag, e) :
    bag.append(e)

def remove(bag,e) :
    bag.remove(e)

def count(bag) :
    return len(bag)
bag=[]


insert(bag,"니얼굴")

print(contains(bag,"니얼굴"))
print(bag)

a = count(bag)
print(a)

print("time :", time.time() - start) 