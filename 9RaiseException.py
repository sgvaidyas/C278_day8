try:
    age = eval(input("Enter the age:"))
    if(age<18):
        raise ArithmeticError
    else:
        print("the age is valid")
except ArithmeticError:
    print("The age is not valid")
except Exception as e:
    print("generic exception = ",e)
