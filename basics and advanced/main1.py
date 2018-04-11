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
#print("Welcome")

#Main method caling condition
if __name__=="__main__":main()

#Second function
def sec():
        print()
        print("Second")
        print()
        inp=int(input("Enter any input:"))
        print()
        print(inp,id(inp),type(inp))

sec()





