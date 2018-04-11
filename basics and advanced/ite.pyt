def squares(start,stop):
    for i in range(start,stop):
        yield i*i



gen=squares(1,10)
print("Generator Object:",gen)
for i in gen:
    print(i,end=" ")
#for i in gen:
#    print("gen:",i,end=" ")

