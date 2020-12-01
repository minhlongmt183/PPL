import os

# ret1 = exec(open("./test.py").read())
ret1 = os.system('python3 test.py')
print(type(ret1))