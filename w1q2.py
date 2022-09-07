print("*** multiplication or sum ***")
x, y = input("Enter num1 num2 : ").split()
if int(x)*int(y)>1000:
    total = int(x)+int(y)
    print("The result is",total)
elif int(x)*int(y)<=1000:
    total = int(x)*int(y)
    print("The result is",total)
