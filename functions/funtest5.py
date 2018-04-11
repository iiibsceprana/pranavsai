def printinfo( arg1,*vartuple):
    "this prints a variable passed arguments"
    print("output is:")
    print(arg1)
    print(vartuple)
    for var in vartuple:
        print(var)
    return

printinfo(10)
printinfo(20,30,40)
printinfo(21,23,25,27,29,31,33)
