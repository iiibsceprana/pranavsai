a=0
for i in range(1,1001):
    s=0
    t=i
    while(i>0):
        a=i%10
        s=s+(a*a*a)
        i=i//10

    if(t==s):
        print("")
        print("Armstrong numbers:",s)
