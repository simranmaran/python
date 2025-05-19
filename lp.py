#while loop-(finite as well as infinite iteration)
#for loop(finite iteration)


#while loop syntax 
#intializ     i=0
#while conditon:  ...
#statwmwnt .....
#incre/decre
# n=int(input("enter a num="))
# i=1    #intialization
# while(i<n):  #condition
#     print(i)
#     i=i+1  #incre/decre



# m=int(input("enter a num="))
# while(m>0):
#     print(m,)
#     m=m-1
    
    
# v=int(input("enter a num="))
# i,sum=1,0
# while i<=v:
#     sum=sum+i
#     if i<v:
#         print(i,end='*')
#     else:
#         print(i,end='=',)
#     i=i+1
# print(sum)
    
    
    
# a=int(input("enter a num="))
# i,mult=1,1
# while i<=a:
#     mult=mult*i
#     if i<a:
#         print(i,end='*')
#     else:
#         print(i,end='=',)
#     i=i+1
# print(mult)


# z=5
# multi=1
# while z>0:
#     multi=multi*z
#     if z>1:
#         print(z,end="*")
#     else:
#         print(z,end='=')
#     z=z-1
# print(multi)    
    
    
    #10 tk ke even num   2,4,6,8 ,10
    #10 even num     2,4,6,8,10,12,14,16,18,20
    #inkaa dono ka sum bhi to yeh 8 question even or odd ke krke lane heee
    #odd #even
    #h.w heeee yeehh


# i = 2
# while i <= 10:
#     print(i,end=",")
#     i = i + 2
    
i,sum = 2,0
while i <= 10:
    print(i)
    sum = sum + i
    i = i + 2
print("Sum =", sum)
