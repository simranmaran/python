#jitni bhi real world entites contectecd he
#class-dummy model/design/blueprint  of an object,ek class se n num of object bana sakte he
#classs me atehe======> behavior-methods , or properties-variables
#clas ka name capital letter se hota he hmesa




#OBject======= physical existence of class ,

#class syntax
#class Class_name:
#   "doc string"
#  varible are three category--class varible,instance variable , local variable


#constructor 
#method=instnace method,class method ,static method



# class Demo:
#     "this is the class "
#     pass
# print(id(Demo))
# print(dir(Demo))   #yeh sareee inbuilt method dikhata heeeee 
# print(Demo.__doc__)



# class Demo:
#     "this is the class "
#     x=10
#     y=20
#     def new(self):
#         pass
# print(Demo.__dict__)
#isme jo main he wo file ki enetrry point hoti he




# class Demo:
#     "this is the class "
#     x=10
#     y=20
#     def new(self):
#         pass
# print(id(Demo))
# obj=Demo
# print(id(obj))
#yeh same adrewsss dega qki abi hamne kisi ko assign nahi kiya he




# class Demo:
#     "this is the class "
#     x=10
#     y=20
#     def new(self):
#         pass
# print(id(Demo))
# obj=Demo() #yaha per jo paranthersis he wo external constructor ko call kr rh he
# print(id(obj))



class Student:
    def __init__(self,name,gread):
        self.n=name
        self.g =gread
        print(id(self))
#obj=Student
obj=Student('simmi','btech')
print(id(obj))
#self ek referece variable he jo cufrrent obj ka adresss hold krta he 
