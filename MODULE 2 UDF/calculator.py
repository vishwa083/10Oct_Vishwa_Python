a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("1 for Add")
print("2 for mul")
print("3 for div")
print("4 for sub")
c=int(input("Enter your choice:"))

def getadd():
    print("Sum :",a+b)
def getmul():
    print("Mul :",a*b)
def getdiv():
    print("Div :",a//b)
def getsub():
    print("Sub :",a-b)

if c==1:
    getadd()
elif c==2:
    getmul()
elif c==3:
    getdiv()
elif c==4:
    getsub()
else:
    print("Error")
