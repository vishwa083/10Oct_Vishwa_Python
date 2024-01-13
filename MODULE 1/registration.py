print("USER REGISTRATION FORM")
a=input("ID:")
if a.isdigit():
    print(a)
    b=input("Name:")
    if b.isalpha():
        print(b)
        c=input("Email:")
        if c.lower():
            print(c)
            d=input("Password:")
            if d.isalnum():
                print(d)
                e=input("Confirm Password:")
                if d==e:
                    print(e)
                    f=input("Mobile Number:")
                    if f.isdigit() and len(f)==10:
                        print(f)
else:
    print("False")

'''a,b="pq"
b,c="rs"
print(a,b,c)'''