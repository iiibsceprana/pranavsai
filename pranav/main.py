########################################################
# __Author__:Vineel
# Version:1.0
########################################################
#main method
def main():
    print()
    print("Hello,World")
    print()
    print("In Main")
    print()

#Print Statement Outside main method
print()
print("Welcome")

#Main method caling condition
if __name__=="__main__":main()

#Second function
def sec():
        print()
        print("Second")


#if __name__=="__sec__":
sec()

#Accepting input from the User
try:
   print()
   inp=int(input("Enter any input:"))
   print()
   print(inp,id(inp),type(inp))

except:
    print("Input should be integer type")
#Third function With no body
def third():

   pass


#If else condition
try:

    print()
    a=int(input("Enter an Integer:"))
    print()
    b=int(input("Enter an Integer:"))

    if a > b:
        print()
        print(a," is greater than ",b)

    elif b > a:
        print()
        print(b," is greater than ",a)

    else:
        print()
        print(a," is equals to ",b)

except:

     print("Input should be integer type")
#for loop example 1
for i in range(0,11,2):
    
    print(i,end=" ")

else:
    print()
    print("Loop Range is Over")

#for loop example 2

for i in range(1,11):

    if i==5:

        continue
    print(i,end=" ")

#for loop example 3
print()
for i in range(11):

    print(i,end=" ")

#while loop example 1
j=0
print()
print("In While loop......")
print()
while True:
    print(j,end=" ")
    if j>=10:
       break
    j+=1

else:

    print("Done")
    
#while loop example2
try:
    print()
    x=int(input("Enter an integer:"))

    while(x==5):
       print()
       print("You Entered:",x)
       break

    else:
       print()
       print("You Entered:",x)

except:
    print("Input should be Integer")

