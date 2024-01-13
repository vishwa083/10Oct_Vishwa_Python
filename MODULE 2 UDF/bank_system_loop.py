cont = "y"
while cont == 'y':
    print("Account Openning:")
    a=input("Enter account number:")
    b=input("Enter account holder name:")
    print("Enter your account type:")
    print("current account")
    print("savings account")
    c=(input("Enter account type:"))

    print("Deposit minimum amount 2000Rs")
    x=int(input("Enter deposit amount:"))
    def deposit():
        print(x)
    if x<2000:
        print("Insufficient balance")
    else:
        deposit()

    y=int(input("Enter withdrawl amount:"))
    def withdrawl():
        print(y)
    if y>x:
        print("Insufficient balance")
    else:
        withdrawl()

    def statements():
        print("Account Statements:")
        print("Account number =",a)
        print("Account name =",b)
        print("Account type =",c)
    statements()

    cont = input("Continue?y/n:")
    if cont == "n":
        break
