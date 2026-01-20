def cel_to_fah(temp):
    return (temp*9/5)+32

def fah_to_cel(temp):
    return (temp-32)*5/9

while True:
    t=float(input("Enter the temperature:"))
    d=input("Enter the unit of measure(c/f):")
    if d=="c":
        t=cel_to_fah(t)
        print("Converted the celsius to fahrenheit:",t)

    elif d=="f":
        t=fah_to_cel(t)
        print("Converted Fahrenheit to celsius:",t)
    else:
        print("Invalid unit.")
    c=input("Do u wish to continue:")
    if c!="yes":
        print("Exiting...")
        break
