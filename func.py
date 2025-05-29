# write one calls multiple 
# to achieve code reusability
# avoid sqqentially or non sequentially block of code repeatation

#function hs two types
# user defined function
# pre defined fucntion


#lemda function jiska koi name nahi hota he

# required in finctions ===== def, fun-name, () , :
# optional in finctions ===== parameters ,arguments ,return


#function wihtout parameter
#koi bhi function return per terminate hota he
# def first():
#     return
# first()
# print(first())

#....................................

# def first():
#     pass
# first()
# print(first())
#..................................

#this is the odd  number function
# def odd(n):
#     for i in range(1,n+1):
#         if i%2!=0:
#             if i<n:
#                 print(i,end=' ,')
#             else:
#                 print(i)
# print("od number")
# n=odd(int(input("enter the number:")))

#........................................
# def odd(n):
#     for i in range(1,n+1):
#         if i<n:
#             print(2*i-1,end=' ')
#         else:
#             print(2*i)
# print("hlww")
# print("hello")
# n=odd(int(input("enter the number:")))
        

#.............................................
# def Eno(n):
#     for i in range(1,n+1):
#         if i<n:
#             print(2*i,end=' ')
#         else:
#             print(2*i)
# print("hlww")
# print("hello")
# n=Eno(int(input("enter the number:")))
        
        
#.......................................................................
# def Eno(n):
#     for i in range(1,n+1):
#         if i<n:
#             print(2*i,end=' ')
#         else:
#             print(2*i)
# print("hlww")
# print("hello")
# n=Eno(int(input("enter the number:")))


#............................................

#ek way yeh he but isme time complezity zyada he 
# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i 
#     print(f'factorial of{n}is{fact}')     
# n=int(input("enter the  num"))
# fact(n)


def fact(n):
    fact=1
    for i in range(n,0,-1):
        fact=fact*i 
        if i>1:
             print(f'{i}*',end='*')
        else:
            print(f'{i}*',end='*')
            print(fact)
print("hello")
n=int(input("enter the  num"))
    





