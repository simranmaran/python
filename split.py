# s='simran'
# print(s.isascii())
# print(s.isdigit())
# print(s.isspace())
# print(s.isnumeric())
# print(s.isnumeric())

# #orderd data type
# # python inbuilt functions apply in list
# l=['python','java','php']
# l2=[10,20,30,40]
# print(max(l))
# print(max(l2))
# print(min(l))
# print(min(l2))
# print(sum(l2))
# print(len(l))
# print(len(l2))
# print(id(l))


# method of lists
# m=[10,10,20,30]
# print(m.count(10))
# print(m.count(100))    #calculate frequency

# m.sort()
# print(m)

# m.reverse()
# print(m)

#arrange descending
# s=[10,20,50,60]
# s.sort()
# s.reverse()
# print(s)


#one more way to arrange descending
s=[10,20,50,60]
s.sort(reverse=True)
print(s)

t=[1,2,3,4,5,5]
t1=t.copy()
print(t)
print(t1)
print(id(t),id(t1))

t.clear()
print(t)

#yaha pee hamne clear method ko ek variable me store krdiya heee
t.clear()
x=t
print(t)
print(id(t))

#.....................
del t
print(t)












# m.append("java")
# print(m)
# m.append([2,4,6,8,10])
# print(m)
# m.extend(['php','java'])
# print(m)
# m.extend('python')
# print(m)
# m.extend('p')
# print(m)
# m.insert(0,[1,2,3,4,4])
# print(m)
# m.pop()
# print(m)
# m.remove(30)
# print(m)
