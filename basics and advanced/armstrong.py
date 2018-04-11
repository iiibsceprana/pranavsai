try:
    inp=int(input("Enter any integer:"))
except:
    print("input should be an integer")
a=inp
print(a)
s=0
while inp>0:
    n=inp%10
    s=s+n*n*n
    print(s)
    inp=inp/10
    print(n)
if s==a:
    print("given no. is Armstrong")
else:
    print("given no is not an armstrong")

