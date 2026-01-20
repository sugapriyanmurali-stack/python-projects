def mail(m):
    spam_words=['Won','prize','lottery','Free','Claim your reward','Congratulations',]
    m=m.lower()
    for i in spam_words:
        if i in m:
            print("**********SPAM**********")
            return

        
        print("**********NOT SPAM**********")

while True:
    Mail=input("Enter paste the mail received:")
    y=mail(Mail)
    c=input("Do u wish to continue:")
    if c!="yes":
        print("Exiting...")
        break