while True:
    avg=float(input("Enter your average"))
    if avg>=75 and avg<=100:
        print("Your average is", avg, "You are Above level")
    elif avg>=60 and avg<75:
        print("Your average is", avg,"You are On level")
    elif avg>=1 and avg<60:
        print("Your average os", avg, "You are Below level")
    else:
        print("Invalid average")
    
