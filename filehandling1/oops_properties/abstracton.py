from abc import ABC, abstractmethod
class Senior(ABC):
  def add (self,x,y):
    return x+y
  def sub(self,x,y):
    return x-y
  @abstractmethod
  def multi(self):
    pass
class Junior(Senior):
  
  def multi(self,x,y):
    return x*y
  
obj=Junior()
x = obj.multi(5,4)
print(x)
 