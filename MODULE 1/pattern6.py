#ascii values for small a-z is between 97-122
for r in range(97,102):
    for c in range(97,r+1):
        print(chr(c),end=" ")
    print(" ")