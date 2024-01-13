techdata=[]
n=int(input("Enter number of students:"))
for i in range(n):
    x=input("Enter the names of students:")
    techdata.append(x)
#print(techdata)
print(tuple(techdata))