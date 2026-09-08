while True:
    name=input("Enter your username:")
    passw=input("Enter your password:")
    if name=="admin" and passw=="1234":
        print("Login successful!")
    elif name=="admin" and passw!="1234":
        print("Incorrect password")
    elif name!="admin" and passw=="1234":
        print("Username not found")
    
