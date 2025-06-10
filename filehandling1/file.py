#open()
#syntax===== open('file name', mode)
#x mode exitisting file per kam nahi krta heh
# f=open('n.text','x')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close


#w mode exitisting file per kam  krta hei
# f=open('n.text','w')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close

#r file ko read krne ke lie hota he 
# f=open('n.text','r')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close 



#akhiri me jake append hogaaa cursor position last me hoga
#yeh ek new file ko create bhi krta he 
# f=open('n.text','a')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close 



# r+ he to  isme read bhi kr sktey he or write bhi kr skty he 
# f=open('n.text','w+')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close 



# f=open('n.text','wb+')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close
# f.close


# f=open('n1.txt','a+')
# data=['python\n','django\n']
# f.writelines(data)



# f=open('n1.txt','a+')
# data='''
#       n=int(input("enter a num))
#       i=1;
#       while i<n:
#             print(i)
#             i=i+1
# '''
# f.writelines(data)
# f.close()


# f=open('n1.txt','a+')
# data='''
#       n=int(input("enter a num"))
#       i=1
#       while i<n:
#             print(i)
#             i=i+1
# '''
# f.write(data)
# f.close()



#read()
#yeh kiisi bhi file ke  all data ko  read krta he eek ek character ke format me 

#read(n)== read(5) mtlb sirf 5 hi character read krne he 
#readline()=read single lines of data
#readlines()=read lines multiples liens of data


# f=open('n1.txt','r+')
# data=f.read()
# print(data)




# f=open('n1.txt','r+')
# data=f.read(10)
# print(data)


# f=open('n1.txt','r+')
# data=f.readline()
# print(data)


# f=open('n1.txt','r+')
# data=f.readlines()
# print(data)




# f=open('n1.txt','r+')
# data1=f.read(5)
# data2=f.read(10)
# print(data1)
# print(data2)


# f=open('n1.txt','r+')
# f.write("hello")
# f.close


# f=open('n1.txt','r+')
# f.readline()
# f.write("hello")

#cursor movement 
#tell()=to check current poaition on cursor
#seak()= how many positions move from where (0,1,2,) 0 is the starting point , 1 is the currenmt position , 2 is the last postion 
# f=open('n1.txt','r+')
# print(f.tell())
# f.read(5)
# print(f.tell())



f=open('n1.txt','r+')
print(f.tell())
f.read(5)
f.seek(0)
f.seek(1)
print(f.tell())
