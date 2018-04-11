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
    #print(n)
    sum=sum+n*n*n
    #print(sum)
    inp=inp//10   
    #print(n)
    


#print(sum)
if sum==num:
    print("Given number is Armstrong")
else:
    print("Given number is not an Armstrong")



