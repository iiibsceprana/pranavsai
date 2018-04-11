inp=int(input("Enter an Integer:"))
num=inp
print("num:",num)
sum=0

while inp>0:

    n=inp%10
    print("n:",n)
    sum+=n*n*n
    print("sum:",sum)
    inp=inp//10
    print("inp:",inp)
if num==sum:

    print("Given number is Armtrong")

else:

    print("Given number is not Armstrong")




