#indexing not supported
#slicing not supported
#mutable in nature


#python inbuilt methods
# d={
#     'name':'simran','age':22,'quali':'Btech'
# }
# print(len(d))
# print(max(d))
# print(min(d))

# n={2:'simran',1:22,3:'Btech'} 
# print(sum(n))
# print(type(n))
# print(id(n))


# m={2:'simran',2:56, '3':"mtech"}
# print(m)


#dict method

# d={
#   'name':'simran','age':22,'quali':'Btech'  
# }
# print(d.keys())  #yeh sirf key dega
# print(d.values())  #yeh sirf value dega
# print(d.items())   # yeh key value dono dega
# print(d.get('name')) #yaha se ek key ki value acess kr sktye he get ke through
# # d.pop('age')
# # print(d)
# # d.popitem()
# # print(d)  #is bale case me last bala jo bhi key value pair hoga wo remove ho jayega

# l=[1,2,4,6,7,'simran']
# d=dict.fromkeys(l,10)
# print(d)
 
 
d={
   'name':'simran','age':22,'quali':'Btech'  
 }
# d.setdefault(('name1','rahul'))
# print(d)
# print(d.setdefault('name1','rahul'))
 
# d.clear()
# print(d)

d1={
    'name':"sakshi maran",
    'age':19,
    'deg':'mtech',
}
d.update(d1)
print(d)

