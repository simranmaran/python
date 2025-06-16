# we can create n number of const but the recent one will be executed
# constructor overload is not supported in py, const can be called explicitly
# class Student:
#     def _init_(self):
#         print("const called")
#     def _init(self,x):
#         print("2nd const called")
#     def _init_(self,x,y,z):
#         print("3rd const called ")
#     def _init_(self):
#         print("4th const called")
# obj=Student()

# class Student:
#     # variable with self is instance variable
#     # method with first parameter as self is known as instance method
#     # n,a,r,c is instance variable
#     def _init_(self,name,age,roll_no,city):
#         self.n=name
#         self.a=age
#         self.r=roll_no
#         self.c=city
#     def show(self):
#         print(self.n)
#         print(self.a)
#         print(self.r)
#         print(self.c)
#         print(self.school)
#         # another method to variable
#     def  add (self,principal):
#         self.p=principal
# x=str(input("enter your name "))
# y=int(input("enter your age "))
# z=int(input("enter your roll no "))
# w=str(input("enter your city "))
# stu1=Student(x,y,z,w)
# accessing instance variable outside class
# print(stu1.n)
# print(stu1.a)
# print(stu1.r)
# print(stu1.c)
# obj=Student('pradhyumn',19,100,'idr')
# # obj.show()
# # we can define an instance variable outside the const as the add is same of obj and self 
# obj.school='SPS'
# obj.show()
# obj.add('mac')
# print(obj.p)