num=int(input("Enter a number:"))
if num>0:
    if num<100:
        print(num,"is positive and less than 100")
    elif num>100:
        print(num,"is positive and more than 100")
else:
    print(num,"is zero or negative")
