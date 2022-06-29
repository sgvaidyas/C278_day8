try:
    fileptr = open("file","r")
    try:
        fileptr.write("Hi I am good")
        #print(fileptr.read())
    except Exception as e:
        print("Exception = ",e)
    finally:
        fileptr.close()
        print("file closed")
except:
    print("Error")
finally:
    print("I will be there for you!!!")

