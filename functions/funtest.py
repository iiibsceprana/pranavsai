'''def add(a,b):
    z=a+b
    return z
n1=int(input("enter any integer:"))
n2=int(input("enter any integer:"))
sum=add(n1,n2)
print(sum)'''

def changeme(mylist):
    "this changes a passed list into this function"
    mylist=[1,2,3,4]
    print ("values inside the function:",mylist)
    return

mylist = [20,20,30,42]
changeme(mylist)
print("values outside the function:",mylist)

