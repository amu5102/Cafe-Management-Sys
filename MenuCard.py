menu = {
    "Pizza" : 110,
    "Pasta" : 90,
    "Burger" : 70,
    "Fries" : 60,
    "Sandwitch" : 50,
    "Cold Coffee" : 40,
}

print("****WELCOME****")
print("      to")
print("***Mau's_Cafe***")
print("Pizza : 110Rs\nPasta : 90Rs\nBurger : 70Rs\nFries : 60Rs\nSandwitch : 50Rs\nCold Coffee : 40Rs")

Total_Orders = 0

Item_1 = input("Enter the name of item you want to order = ")
if Item_1 in menu:
    Total_Orders += menu[Item_1]
    print(f"Your item {Item_1} has been added to your order")
else:
    print("This item is not available, Please order something else")
    
Something_else = input("Do you want to add something else? (Yes/No) = ")
if Something_else == "Yes":
    Item_2 = input("Enter the name of item you want to order = ")
    if Item_2 in menu:
        Total_Orders += menu[Item_2]
        print(f"Your item {Item_2} has been added to your order")
    else:
        print("This item is not available, Please order something else")
else:
    print("Thank you for your order")

print(f"The total amount of your order is {Total_Orders}Rs" )
    
