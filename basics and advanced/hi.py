try:
    print()
    inp=float(input("enter any number:"))
    print(inp,id(inp),type(inp))
except:
    print("input shoud be integer type")
def third():
    pass
try:
    print()
    a=int(input("Enter an integer"))
    b=int(input("Enter an integer"))
    if a > b:
        print(a,"is greater than",b)
    elif b > a:
        print(b,"is greater than",a)
    else:
        print(a," is equals to ",b)
except:
    print("input should be integer type")
for i in range(0,11,2):
    print(i,end=" ")
else:
    print("loop range is over")
