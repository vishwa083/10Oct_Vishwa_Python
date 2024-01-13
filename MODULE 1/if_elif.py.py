"""a=int(input("Enter number:"))
if a>0:
    print("A is positive")
elif a<0:
    print("A is negative")
else:
    print("A is Zero")"""

'''a=int(input("Enter number:"))
if a%2==0:
    print("Number is even")
else:
    print("Number is odd")'''

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b and a>c:
    print("Max number is",a)
elif b>a and b>c:
    print("Max number is",b)
else:
    print("Max number is",c)