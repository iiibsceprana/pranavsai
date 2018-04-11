def cubes(start,stop):
    for i in range(start,stop):
        yield i*i*i



gen=cubes(1,10)
print("Generator Object:",gen)
#for i in gen:
#    print(i,end=" ")
for i in gen:
    print(i,end=" ")
gen1=cubes(1,10)
gen2=cubes(1,10)
for i in gen1:
    print(i,end=" ")
for i in gen2:
    print(i,end=" ")

