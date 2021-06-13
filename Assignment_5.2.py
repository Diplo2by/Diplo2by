larg = None
smol = None
while True:
    num = input("Enter a Number ")
    if num == "done" :
        break
    try:
        n = float(num)
        if larg is None:
            larg=n
        elif n > larg:
            larg=n
        a= float(num)
        if smol is None:
            smol=a
        elif a < smol:
            smol=a
    except: 
        print("Invalid input")

print("Maximum is ", larg)
print("Minimum is ", smol)
