def compose(*g):
    def h(args):
        return reduce(lambda x, y: y(x), reversed(g), args)
    return h
    
def squ(x):
    return x * x
def inc(x):
    return x + 1
def dou(x):
    return x * 2
    
m = compose(squ, inc, dou)
print(m(5))