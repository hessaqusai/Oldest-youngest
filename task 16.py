while True:
    num=66
    gnum=int(input("Guess the number"))
    if gnum==num:
        print("You won!!")
    else:
        print("You failed, my secret num is", num)
