# class Parent:
#   def home(self):
#     print("home from parent")
#   def car(self):
#     print("car from parent")
    
# class son(Parent):
#   pass
# class Daughter(Parent):
#   pass

# obj=son()
# obj.home()
# obj.car()
# obj1=Daughter
# obj1.home()




# class Parent:
#   def home(self):
#     print("home from parent")
#   def car(self):
#     print("car from parent") 
# class son(Parent):
#   pass
# class Daughter(Parent):
#   pass

# class child():
#   pass
# obj=child()





class Parent:
  def home(self):
    print("home from parent")
  def car(self):
    print("car from parent") 
class child(Parent):
 def home(self):
   print("home from child")
   super().home()   #use for method over riding
obj=child()
obj.home()


