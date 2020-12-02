# #  class là bảng mô tả, còn object là thực thể bảng mô tả đó
# # instance method: method belongs to the instance

# class Employee:
#     empCount = 0
#     # def __init__(self, n, s):
#     #     self.name = n
#     #     self.salary = s
#     #     Employee.empCount += 1
    
#     def displayEmployee(self):
#         print("Name : " , self.name, ", Salary: ", self.salary)

#     @classmethod
#     def create(cls,n, s):
#         print(cls.empCount)
#         return cls(n, s)
    
#     @staticmethod
#     def isHighSal(s):
#         if s > 8:
#             print("High Salary")
    
# x = Employee()
# print(type(x))

# # obj = Employee.create("Nam", 30)
# # Employee.isHighSal(30)

## Parametric Polymorphism

class A:
    def func1(self):
        print("A")

class B(A):
    def func1(self):
        print("B")
i = B()
print(id(i))