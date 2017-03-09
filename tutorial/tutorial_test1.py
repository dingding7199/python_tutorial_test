#!/usr/bin/env python
#coding=utf-8
from collections import deque


print 'C:\some\name'
print r'C:\some\name'

print 3 * 'un' + 'ium'

a, b = 0, 1
while b < 10:
    print a, b
    a, b = b, a+b #前面的值赋给后面

x = -4
if x < 0:
    x = 0
    print 'Negative changed to zero'
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'Single'
else:
    print 'More'

words = ['cat', 'window', 'defenestrate']
for w in words:
    print w, len(w)

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
        print w, len(w)

print words


print range(10)
print range(5, 10)
print range(0, 10, 3)
print range(-10, -100, -10)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print i, a[i]

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
            break
    else:
        print n, 'is a prime number'
for n in range(2, 10):
    if n % 2 ==0:
        print n, 'is a even number'
        continue
    print "Found a number", n

def fib(n):
    a, b = 0, 1
    try:
        while a < n:
            print a, b
            a, b = b, a + b
    except:
        print 'error'
        return
fib(200)

def fib2(n):
    result = []
    a, b = 0, 1
    try:
        while a < n:
            result.append(a)
            a, b = b, a+b
    except:
        print 'error'
        return result
f = fib2(100)
print f

#using Lists as Stacks 栈
#("last-in, first-out")
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print stack
stack.pop()
print stack


#using lists as Queues
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()
print queue














































