import functools

#Question 3

#a
def lessThan1(x, lst):
    return [n for n in lst if n < x]

#b
def lessThan2(x, lst):
    if len(lst) == 0:
        return []
    elif lst[0] < x:
        return [lst[0]] + lessThan2(x,lst[1:])
    else:
        return lessThan2(x,lst[1:])

#c
def lessThan3(x, lst):
    return list(filter(lambda n: n < x, lst))

print(lessThan1(50, [1,55,6,2]))
print(lessThan2(50, [1,55,6,2]))
print(lessThan3(50, [1,55,6,2]))



