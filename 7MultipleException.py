try:
    a=10/0
except(ArithmeticError, IOError):
    print("there is Arithmetic/IO Error Exception")
else:
    print("Successfully Done")
