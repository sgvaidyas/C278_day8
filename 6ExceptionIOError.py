try:
    #this will throw an exception if the file doesn't exist.
    fileptr = open("file","r")
except IOError:
    print("File not found")
else:
    print("The file opened successfully")
    print(fileptr.read())
    fileptr.close()    
