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



f=open('n.text','wb+')
print(f.name)
print(f.mode)
print(f.encoding)
print(f.readable())
print(f.writable())
print(f.closed)
f.close
f.close