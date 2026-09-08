price=int(input("Enter the price of the item:"))
disc=price*10/100
if price<=100:
    print("No discount aplied.")
else: 
    print("Final price", price-disc)
