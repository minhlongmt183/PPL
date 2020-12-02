from functools import reduce
def nhan2(x):
    return x*2
def cong1(x):
    return x+1
def nhan4(x):
    return x*4
def compose(f,g):
    return lambda x:f(g(x))
def composeb(*fun):
    return reduce(compose,fun,lambda x:x)
# q4 = compose(nhan2,cong1)
# print(q4(3))
# t4b = composeb(nhan2,cong1,nhan4)
# print(t4b(1)) #10


def composea(*fun):
    if (len(fun)==1):
        return fun[0]
    else:
        return fun[-1](composea(fun[:-1]))
t4a = composea(nhan2,cong1,nhan4)
print(t4a(1)) #10
