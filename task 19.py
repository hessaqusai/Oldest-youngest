
while True:
    user=input("Enter username:")
    passw=int(input("Enter password:"))
    uc="admin"
    pc=1234
    if user==uc and passw==pc:
        print("Login successful")
    elif user==uc and passw!=pc:
        print("Incorrect password")
    else:
        print("Username not found")

