#filter
# yaha per coollectiion ek hi bhej saktey he multiple collection nahi
# isme duolication allow he
# syntax
# filter(funname,iterator)

# l1=[2,4,6,8,10]
# l2=[1,2,3,4,5,6,7,8,9,10]
# def even_no(n):
#     if n%2==0:
#         return n
# x=filter(even_no,l1)
# print(list(x))
# y=filter(even_no,l2)
# print(list((y)))


#................................................
#reduce
#syntax
#reduce(func_name,iterator,intialvalue)
# from functools import reduce
# l1=[2,4,6,8,10]
# l2=[1,2,3,4,5,6,7,8,9,10]
# def min_no(x,y):
#     if x<y:
#         return x
#     else:
#         return y
# x=reduce(min_no,l1,0)
# print(x)
#.......................................

#for maximum
# from functools import reduce
# l1=[2,4,6,8,10]
# l2=[1,2,3,4,5,6,7,8,9,10]
# def min_no(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# x=reduce(min_no,l1,0)
# print(x)
#........................................


#sum...................................
# from functools import reduce
# l1=[2,4,6,8,10]
# l2=[1,2,3,4,5,6,7,8,9,10]
# def min_no(x,y):
#         return x+y
# x=reduce(min_no,l1)
# print(x)


#multiplicatin...............................
# from functools import reduce
# l1=[2,4,6,8,10]
# l2=[1,2,3,4,5,6,7,8,9,10]
# def min_no(x,y):
#         return x*y
# x=reduce(min_no,l1)
# print(x)


#square krke sum krna he
# from functools import reduce
# l1=[1,2,3,4,5]
# l2=[1,2,3,4,5,6,7,8,9,10]
# def min_no(sum,x):
#         return sum+(x**2)
# x=reduce(min_no,l1,0)
# print(x)

# from functools import reduce
# l1=[1,2,3,4,5]
# l2=[1,2,3,4,5,6,7,8,9,10]
# def min_no(sum,x):
#         return sum+x
# x=reduce(min_no,l1,0)
# print(x)
#................................................................
#  Lembda function...............................
#lemba function=esa function jiska koi name nahi hota he ,or yeh keyword he
#single line ka exoression solve krne ke liye hota he

# lambda(parameters):expression
# x=lambda x,y:print(x+y)
# p=int(input("enter num"))
# q=int(input("enter num"))
# x(p,q) 

#............................................

# x=lambda x,y:x+y
# p=int(input("enter num"))
# q=int(input("enter num"))
# z=x(p,q) 
# print(z)
#........................................

# x=lambda x,y: print(x+y)
# p=int(input("enter num"))
# q=int(input("enter num"))
# z=x(p,q) 
# print(z)
# print(z)
# print(z)

#........................................

