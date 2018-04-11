total = 100
def sum(arg1,arg2):
    total=arg1+arg2;
    print("inside the function local total:",total)
    s=35
    print("local variable value:",s)
    return total
sum(20,80)
print("outside the function global total:",total)
