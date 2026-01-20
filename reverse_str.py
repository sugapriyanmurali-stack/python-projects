def reverse(s):
    return s[::-1]

while True:
    str1=input("Enter the string:")
    rev=reverse(str1)
    print("Reversed string is:",rev)
    cnt=input("Do you wish to continue:")
    if cnt!="yes":
        print("Exiting....")
        break