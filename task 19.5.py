counter=3
uc="admin"
pc="1234"
while counter>0:
    user=input("Enter username:")
    passw=input("Enter password:")
    if user==uc and passw==pc:
        print("Login successful")
        break
    elif user==uc and passw!=pc:
        print("Incorrect password")
        counter=counter-1
        print("You have", counter,"trials left")
    else:
        print("Username not found")
        counter=counter-1
        print("You have", counter,"trials left")
        
else:
    print("You can not login to the system anymore, you have used all your trials")
