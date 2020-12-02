# sentence a
def double1(lst):
    return [2*x for x in lst]

ret_lst = double1([1,2,3,4])
print(ret_lst)

# # sentence b
def double2(lst):
    if len(lst) == 0:
        return []
    return [2*lst[0]] + double2(lst[1:])

    # return double2(lst[:-1]) + [2*lst[len(lst)-1]]

# sentence c
def double3(lst):
    return list(map(lambda x: 2*x, lst))

ret_lst = double3([1,2,3,4])
print(ret_lst)
    