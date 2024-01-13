data={}
n=int(input("Enter no. of students:"))
for i in range(n):
    newdata=input("Enter your child dictionary name:")
    data[newdata]={}

    name=input("Enter name:")
    city=input("Enter city:")

    data[newdata]["name"]=name
    data[newdata]["city"]=city
print(data)