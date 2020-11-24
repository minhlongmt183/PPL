#  Quiz 1
# def lessThan(lst,n):
#     return [x for x in lst if x < n]

# print(lessThan([1,2,3,4,5], 4))

# Quiz 2
# def lessThan(lst, n):
#     return list(filter(lambda x: x < n, lst))

# print(lessThan([1,2,3,4,5], 4))

#Quiz 3
# def lstSquare(n):
#     if n == 1:
#         return [1]
    
#     return lstSquare(n-1) + [n*n]

# print(lstSquare(3))


#Quiz 4
# def lstSquare(n):
#     return [x**2 for x in range(1,n+1)]

# print(lstSquare(3))

# Quiz 5
# def flatten(lst):
#     if len(lst) == 0:
#         return []
#     return lst[0] + flatten(lst[1:])

# print(flatten([[1,2,3],[4,5],[6,7]])) 

# # Quiz6
# from functools import reduce
# def flatten(lst):
#     return list(reduce(lambda x, y: x + y, lst, []))

# print(flatten([])) 

# # Quiz 7
# def dist(lst, n):
#     if len(lst) == 0:
#         return []
    
#     return [(lst[0], n)] + dist(lst[1:], n)

# print(dist([1,2,3],4))

# # Quiz 8
# def dist(lst, n):
#     return list(map(lambda x: (x, n), lst))

# print(dist([1,2,3],4))


# # Quiz 9
# def powGen(y):
#     def inner(x):
#         return x ** y
#     return inner

# square = powGen(2)
# print(square(4))

# Quiz 10

from functools import reduce
def compose1(f, g):
    return lambda *a, **kw: f(g(*a, **kw))

def compose(*fs):
    return reduce(compose1, fs)



def increase(n):
    return n+1

def square(n):
    return n**2

f = compose(increase, square)
print(f(3))
