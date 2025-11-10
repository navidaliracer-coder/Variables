CostPrice = int(input("enter the cost price:  "))
SellingPrice = int(input("enter the selling price:  "))

if(SellingPrice>CostPrice):
    print("Your profit is")
    pt=SellingPrice-CostPrice
    print(pt)
else:
    print("You have no profit")
