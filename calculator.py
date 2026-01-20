def addn(a,b):
    return a+b
def subn(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def moddiv(a,b):
    return a%b
def fldiv(a,b):
    return a//b
def exp(a,b):
    return a**b
while True:

    num1=int(input("Enter the 1st num:"))
    num2=int(input("Enter the 2nd num:"))
    exp=input("Enter the operation to be done:")
    if exp=="+":
        print("The Answer is",addn(num1,num2))
    elif exp=="-":
        print("The Answer is",subn(num1,num2))
    elif exp=="*":
        print("The Answer is",mult(num1,num2))
    elif exp=="/":
        print("The Answer is",div(num1,num2))
    elif exp=="%":
        print("The Answer is",moddiv(num1,num2))
    elif exp=="//":
        print("The Answer is",fldiv(num1,num2))
    elif exp=="**":
        print("The Answer is",exp(num1,num2))
    else:
        print("Invalid operation")
    cnt=input("Do you wish to continue:")
    if cnt!="yes":
        print("Exiting...")
        break