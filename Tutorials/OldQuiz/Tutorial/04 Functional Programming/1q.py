from functools import *
def lstSquare_1(n):
    if n == 0:
        return []
    return lstSquare_1(n-1) + [n ** 2]

print(lstSquare_1(3))

def lstSquare_2(n):
    return map(lambda x: (x+1)**2, range(n))

def pow_1(x, y):
    if n == 0:
        return 1
    return x * pow_1(x, y - 1)

def pow_2(x, y):
    return reduce(lambda a, b: a * b, list(map(lambda a: x, range(y))))

def append_1(a, b):
    if b == []:
        return a
    return append_1(a + [b[0]], b[1:])

def append_2(a, b):
    return reduce(lambda x, y: x + [y], b, a)

def reverse_1(a):
    if a == []:
        return a
    return reverse_1(a[1:]) + [a[0]]

def reverse_2(a):
    return list(map(lambda x: a[len(a) - x - 1], range(len(a))))

def lessThan_1(n, l):
    if l == []:
        return []
    if l[0] < n:
        return [l[0]] + lessThan_1(n, l[1:])
    return lessThan_1(n, l[1:])

def lessThan_2(n, l):
    return list(filter(lambda x: x < n, l))

def lookup(st, ls, func):
    return list(filter(lambda x: func(x) == st, ls))

print(lookup("c", [{'a':'a','b':1},{'a':'b','b':2},{'a':'c','b':3}], lambda x: x['a']))
    
reduce(a, b, c)

reduce(phep_cong(x, y) x + y, [1,2,3,4], 0)

    
#print(reverse_2([1,2,3,4,5]))
#print(append_2([1,2,3],[4,5]))
#print(int(0==0))
    