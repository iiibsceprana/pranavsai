'''try:
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
for i in range(1,11):
    if i==5:
        continue
    print(i,end=" ")
print()
for i in range(11):
    print(i,end=" ") '''
'''j=0
print()
print("In while loop...")
print()
while True:
    print(j,end=" ")
    if j>=10:
        break 
    j+=1
else:
    print("done")'''

try:
    print()
    x=int(input("enter an integer:"))
    while(x==5):
        print()
        print("you entered:",x)
        break
    else:
        print()
        print("you entered:",x)
except:
    print("input should be an integer")

