try:
    fh=open("testfile","w")
    fh.write("Love All Serve All\nHelp Ever Hurt Never")
finally:
    print("data is added in the textfile")
    fh.close()
