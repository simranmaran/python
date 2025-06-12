import pickle
#python object ko binary file me store krne ke liye pickle ka use hota he
#dump()---yeh python object ko binary file create karke usko byte me store kr deta he
#load()--byte code ko read karke python object me convert kr deta he

# f=open('n1.pkl','ab+')
# #ab+ mode me file open kiya he, ab+ ka matlab append and read
# data={'name':'simran','city':'delhi'}
# pickle.dump(data,f)  #data ko file me store kr diya
# f.close() 




f=open('n1.pkl','rb+')
data=pickle.load(f)  #file se data ko read kiya
print(data)  
f.close()  


#total 16 modes hotw he file me
#text file me a+ #binary file me ab+ mode use hota he
# ham likhne ke liye kisi bhi file me w mode ka use nahi karte he 
# kyuki w mode me file create hoti he, agar file exist karti he to uska content delete ho jata he
# isliye ham hamesha a+ mode ka use karte he, jisse file create ho jati he agar exist nahi karti    
