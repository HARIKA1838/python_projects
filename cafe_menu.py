menu={
    'Instant Coffee':80,
    'Latte':90,
    'Americano':120,
    'Mocha':70,
    'Cappuccino':80,
    'Black Coffee':60,
    'Macchiato':100,
    'White Mocha':80,
    'Dark mocha':90,
}

print("Welcome to COFFEE HOUSE CAFE")
print("    ")
print("Instant Cofee: Rs.80\nLatte: Rs.90\nAmericano: Rs.120\nMocha:Rs.70\nCappucciano: Rs.80\nBlack Coffee:Rs.60\nMacchiato: Rs.100\nWhite Mocha: Rs.80\nDark Mocha: Rs.90")

order_total=0

item_1=input("Enter the name of the item:")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available")
print("  ")
another_order=input("Do you want to add another item?(yes/no)")
if another_order=="yes":
    item_2=input("Enter the name of the second item:")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available")
print("  ")
print(f"The total amount:{order_total}")
