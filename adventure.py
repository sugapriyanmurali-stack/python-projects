name=input("Enter your name:")
print("Welcome",name)
print("Your are stuck in deep woods plan your escape....")
print("There are two paths ahead of you choose one......The one on the right leads to a empty desert and the one  on the right leads to a crocodile river")
path1=input("Choose right or left:")
if path1=="right":
    print("You have entered the desert....")
    print("You have minimal amount of water find a source for water......")
    print("You can either walk till you find a oasis or dissect the cactus and use its fleshy part to stay hydrated....")
    path2=input("Choose whether its oasis or cactus:")
    if path2=="oasis":
        print("You have run out of water.....")
        print("There are no oasis nearby.....")
        print("YOU DIED.....")
    if path2=="cactus":
        print("You got poked by the thorns in the cactus..")
        print("You are bleeding!!!!!")
        print("You have 3 hours left to escape or you will bleed to death...")
        print("You see a man in a camel and hes headed towards you....you talk with and he tells you that hes headed opposite to the hospital and hes not willing otherwise....")
        path3=input("You can either go with the man to his village or beat him and take his camel.CHOOSE->Village or Hospital:").lower()
        if path3=="village":
            print("You died..")
        elif path3=="hospital":
            print("You survived and escaped")

elif path1=="left":
    print("You have reached the river....")
    print("You got eaten by the crocodiles....")