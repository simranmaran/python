# Conditional -> if,if-else,if-elif,if-elif-else
# iterative-> while,for
# transfer-> continue,break,pass

# conditonal --> if 
# x=10
# if x>8:
#     print("this is if body")


# print("this is main body")

# x=input(str("enter your name :"))
# x=False
# if x :
#     print("hello" ,x)

# print("bye",x)

# to check if no is odd or not
# n=int(input("enter value of n :"))
# if(n%2==0):
#     print(f'{n} is even')
# else:
#     print(f'{n} is odd')

# x=int(input("enter val of x :"))
# y=int(input("enter val of y :"))
# z=int(input("enter val of z :"))

# if x>y and x>z:
#     print("x is greater")
# elif(y>x and y>z):
#     print("y is greater")
# else:
#     print("z is greater")

# dry principle:don't repeat the code:, to avoid sequential repetition of block of code we use iterative/looping statements

# iterative/looping: while n for loop

# while loop: for infinite iteration
# for loop; finite iteration

#  while:
# n=int(input("enter value of n "))
# i=1
# while i<=n:
#     print(i)

#     i=i+1
# n=int(input("enter value of n "))
# i=1
# summ=0
# while i<=n:
#     summ=summ+i
#     if i<n:
#         print(i,end="+")
#     else:
#         print(i,end="=")


#     i=i+1

# print(summ)
# n=int(input("enter value of n "))
# i=1
# mult=1
# summ=0
# while i<=n:
#     mult=mult*i
#     if i<n:
#         print(i,end="*")
#     else:
#         print(i,end="=")


#     i=i+1

# print(mult)

n=int(input("enter val of n "))
mult=1
while n>0:
    mult=mult*n
    if n >1:
        print(n,end="*")
    else:
        print(n,end="=")
    n=n-1

print(mult)


# n=int(input("enter val of n"))
# while n>0:
#     print(n)
#     n=n-1

