import os
class Bank_Account:
    def __init__(self,acc_no,name,password,balance=0):
        self.acc_no=acc_no
        self.name=name
        self.password=password
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Amount deposited successfully.")
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")
    
    def display(self):
        print("You have",self.balance,"in your bank account.")
    
    
File_name ="accounts.txt"

def load_account():
    accounts=[]
    if os.path.exists(File_name):
        with open ("accounts.txt","r") as file:
            for line in file:
                acc_no,name,password,balance=line.strip().split(",")
                accounts.append(Bank_Account(acc_no,name,password,float(balance)))
        
    return accounts
    
def save_account(accounts):
    with open("File_name.txt","w") as file:
        for acc in accounts:
            file.write(f"{acc.acc_no},{acc.name},{acc.password},{acc.balance}\n")
    
accounts=load_account()

def Create_acc():
    acc_no=input("Enter your account number:")
    name=input("Enter your name:")
    password=input("Create Password:")
    for acc in accounts:
        if acc.acc_no==acc_no:
            print("Account already exists.")
            return
    account=Bank_Account(acc_no,name,password)
    accounts.append(account)
    save_account(accounts)
    print("Account created successfully.")
    
def login():
    acc_no=input("Enter the account number:")
    password=input("Enter the password:")
    for acc in accounts:
        if acc.acc_no==acc_no and acc.password==password:
            print(f"Welcome {acc.name}")
            user_menu(acc)
            save_account(accounts)
            return
        else:
            print("Invalid account number or password") 

def user_menu(account):
    while True:
        print("***********ACCOUNT MENU*************")
        print("1.deposit.\n2.withdraw.\n3.check balance\n4.logout")
        choice=input("Enter your choice:")
        if choice=="1":
                amt=float(input("Enter amount:"))
                account.deposit(amt)
        elif choice=="2":
                amt=float(input("Enter amount:"))
                account.withdraw(amt)
        elif choice=="3":
                account.display()
        elif choice=="4":
                print("Logged out successfully.")
                break
        else:
                print("INVALID")

while True:
    print("**************BANK MANAGEMENT SYSTEM******************")
    print("1.Create Account.\n2.Login.\n3.Exit")
    ch=input("Enter your choice:")

    if ch=="1":
        Create_acc()
           
    elif ch=="2":
        login()
        
    elif ch=="3":
        print("Thank you for using....")
        break
    else:
        print("INVALID OPTION")

