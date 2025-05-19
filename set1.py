#unorderd colllection of unique elements
#represented {} and  comma seprated ,
#indexing not supported
#slicing not suppported
#mutable in nature
# st={2,3,4,5,6,'python','java','php'}
# print(st)
# print(id(st))
# # print(st.max())
# print(len(st))





# s={2,4,6,8,'python','java','php'}
# s.add('sql')
# print(s)

# s.update('simran') #iterable value ko letaa
# print(s)

# s.update((1,3,'maran'),'sharma')
# print(s)
# s.pop()
# print(s)

# s.remove('java')
# print(s)

# s.remove('Java')
# print(s)  #yeh errorr dega qki j captial hee is error ko correct krne ke liyee discart ka use krtey heee

# s.discard('Java')
# print(s)

# s.clear()
# print(s)    #outputtt iska set()  ayega

# s1=s.copy()
# print(s,s1)

#single set or double set 2 type ki methods hoti he yeh set ki\

# m={2,4,6,8,'python','java','php'}
# n={2,4,6,8,'python','java','php','simran'}
# print(m.union(n))
# print(m.intersection(n))
# print(m.difference(n))   #iske liye this se pehle set define krungi like {2,3,4,5,5} {3,4,46,477,568,}
# print(m.symmetric_difference(n))
# m.intersection_update(n)
# print(m)
# print(n)

# m.difference_update(n)
# print(m)
# print(n)


# m.symmetric_difference_update(n)
# print(m)
# print(n)



s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.isdisjoint(s2))

print(s1.issuperset(s2))
print(s2.issuperset(s1))
print(s2.issubset(s1))

