try:
    inp=int(input("Enter any integer:"))

except:
    print("Input should be integer")
        
num=inp
#print(num)

sum=0
#print(sum)
while inp>0:
    #print("Hello")
    n=inp%10
    print("n=:",n)
    #print(n)
    for i in range(1,n):
        #print("i:",i)
        n=n*i
        print("Factorial:",n)
        #print("n:",n)   
    sum=sum+n
    print("sum:",sum)
    #print("sum:",sum)
       
    #print(sum)
    inp=inp//10
    print("inp:",inp)   
    #print(inp)

#print(sum)
if sum==num:
    print("Given number is Strong")
else:
    print("Given number is not Strong")



