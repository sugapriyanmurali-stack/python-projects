import re
print("Enter a password with atleast \n1 uppercase  \n1 lowercase  \n1 number and \n1 special symbol..")
pw=input("Enter the passwaord.")
if pw not in re.compile(r'^[a-zA-Z0-9._%+-]'):
    print("Incorrect")
else:
    print(pw)