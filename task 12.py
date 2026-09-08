while True:
    wd=int(input("Enter amount of withdraw:"))
    balance=1000
    amount=1000-wd
    if wd<=1000:
        print("Withdrawal successful. Remaining balance:", amount )
    else:
        print("Insufficient, you'r balance is", balance)
