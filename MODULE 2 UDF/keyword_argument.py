def getdata(id,name,sub):
    print("ID:",id)
    print("Name:",name)
    print("Subject:",sub)

#getdata(1,'sanket','python') #positional argument
    
#getdata('vishwa',2,'python') #positional argument
    
getdata(id=101,name='vishwa',sub='python') #keyword argument

getdata(name='vishwa',id=101,sub='python') #keyword argument