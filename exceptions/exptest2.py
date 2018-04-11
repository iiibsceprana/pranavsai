try:
    fh = open("testfile","r")
    fh.read()
except IOError:
    print("error can't find file or read data")
else:
    print("reading content from the file successfully")
    fh.close()

