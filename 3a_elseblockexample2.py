master = [11,22,33,44,55,99]

ind = int(input("Enter the index = "))
try:
    print("the element = " , master[ind])
except IndexError:
    print("Index out of range exception")
else:
    if(master[ind]>0):
        print("this is a positive value")
