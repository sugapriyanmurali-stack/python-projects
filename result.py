def marks(x):
    if x<34:
        print("Fail")
    elif 35<=x<=65:
        print("C Grade")
    elif 66<=x<=85:
        print("B Grade")
    elif 86<=x<=95:
        print("A Grade")
    elif 96<=x<=100:
        print("A+ Grade")
while True:    
    x=int(input("Enter the Marks:"))
    y=marks(x)
    c=input("Do u wish to continue:")
    if c!="yes":
        print("Exiting...")
        break
