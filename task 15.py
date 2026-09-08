while True:
    print("*************************************************************************")
    print("Welcome to the Insurance Premium Calculator")
    print("If the vehicle value is less than 100,000 the premium is 5% of the value")
    print("If the vehicle value is 100,000 or more the preium is 8% of the value")
    print("*************************************************************************")
    value=int(input("enter vehicle value"))
    insurance5=(5/100)*value
    insurance8=(8/100)*value
    if value>0:
        if value<100000:
            print("the vehicle value is less than 100,000")      
            print("insurance premium is:", insurance5)
        else:
            print("the vehicle value is more than 100,000")
            print("insurance premium is:", insurance8)
    else:
        print("Please enter a positive value")

    
