from functools import reduce

#question a
def flatten1(lst):
    return [elem for sublst in lst for elem in sublst]

#question b
def flatten2(lst):

    if len(lst) == 0:
        return []
    return lst[0] + flatten2(lst[1:])



# sentence c
def flatten3(lst):
    return reduce(lambda x,y: x+y, lst, [])
lst = list(flatten3([[1,2,3],["a","b","c"],[1.1,2.1,3.1]]))
print(lst)