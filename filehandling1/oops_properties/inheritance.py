# MRO Logic appply in inheritance


# class Parent1:
#   def home1(self):
#     print("home from GP")
#   def car1(self):
#     print("car from GP")
    
# class Parent2:
#    def home2(self):
#     print("home from GP")
   
#    def car2(self):
#     print("car from GP")
    
# class Child(Parent1,Parent2):
#   pass

# obj=Child()
# obj.home1()
# obj.home2()
# obj.car1()
# obj.car2()





class Parent1:
  def home(self):
    print("home from GP")
  def car1(self):
    print("car from GP")
    
class Parent2:
   def home(self):
    print("home from GP")
   
   def car2(self):
    print("car from GP")
    
class Child(Parent1,Parent2):
  pass

obj=Child()
obj.home()
obj.car1()
obj.car2()

