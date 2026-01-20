def palindrome(str1):
    return str1==str1[::-1]

while True:
    str1=input("Enter the string:")
    pd=palindrome(str1)
    if pd==True:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")
    cnt=input("Do you wish to find the palindrome:")
    if cnt!="yes":
        print("Exiting....")
        break