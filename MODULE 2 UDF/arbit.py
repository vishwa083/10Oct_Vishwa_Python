def getdata(*data):
    print("ID:",data[0])
    print("Name:",data[1])
    print("Subject:",data[2])
#getdata(101,'vishwa','python')
    
stid=input("Enter ID:")
stnm=input("Enter name:")
stsub=input("Enter subject:")
getdata(stid,stnm,stsub)