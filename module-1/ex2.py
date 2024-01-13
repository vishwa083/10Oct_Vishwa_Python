a1=int(input("Maths:"))
a2=int(input("Science:"))
a3=int(input("English:"))
a4=int(input("SS:"))

if a1<=40 and a2<=40 and a3<=40 and a4<=40 :

    total=a1+a2+a3+a4
    print("Total:",total)

    percentage=total/4
    print("percentage",percentage)

    if percentage>=70:
        print("Result:A+")
    elif percentage>=60:
        print("Result:A")
    elif percentage>=50:
        print("Result:B")
    elif percentage>=40:
        print("Result:c")
else:
    print("Result:FAIL")
