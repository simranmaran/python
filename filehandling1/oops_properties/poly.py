class Addition:
  def add (self,x,y):
    return x+y
  def add(self,x,y,z):
    return x+y+z
  def add(self,x,y,z,p):
    return x+y+z+p
  def add(self,*n):
    sum=0
    for i in n:
      sum=sum+i
    return(sum)
print(sum)