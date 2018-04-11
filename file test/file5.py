hi=open("readme.txt","r+")
str= hi.read(10)
print("read string is :",str)

position=hi.tell()
print("current file position:",str)

position= hi.seek(0,0)
str=hi.read(20)
print("again read string is :",str)

hi.close()

