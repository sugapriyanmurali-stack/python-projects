import re
def valid(str1):
    email=re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-z0-9.-]+\.[a-zA-z]{2,}$')
    if email.match(str1):
        return True
    else:
        return False
    
while True:
    email=input("Enter the Email:")
    if valid(email):
        print("Valid Email.")

    else:
        print("Invalid Email.")
    cnt=input("Do you wish to continue:")
    if cnt!="yes":
        print("Exiting....")
        break
