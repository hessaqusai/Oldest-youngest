num=83
counter=3
while counter>0:
    gnum=int(input("Enter the number"))
    if gnum==num:
        print("You won!!")
        break
    else:
        counter=counter-1
        print("Wrong, you have",counter)
        if counter==0:
            print("You failed, my secret num is", num)
