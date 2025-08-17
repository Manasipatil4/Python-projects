menu = {
    'pizza':40,
    'Pasta':50,
    'Orange juice':30,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
}
print("welcometo ora cafe")
print(" Pizza : Rs40 \n  Pasta: Rs50 \n  Orange juice: Rs30 \n Burger:Rs60 \n Salad:70 \n Coffee:Rs80 ")
order_total =0

item_1 = input("enter name of item you want to order=")
if item_1 in menu:
    order_total += menu[item_1]
    print("your item {item_1} has been added to your order")

else:
    print("order item {item_1} is not available yet")


another_order = input("DO you want to add another item? (yes/no)")
if another_order == "yes":
    item_2 = input("enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not available!")    

print(f"the total amount is {order_total}")